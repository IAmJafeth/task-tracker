from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    TODO = "todo"
    INPROGRESS = "in-progress"
    DONE = "done"


@dataclass
class Task:
    id: int
    description: str
    status: TaskStatus = field(default=TaskStatus.TODO)
    createdAt: datetime = field(default_factory=datetime.now)
    updatedAt: datetime = field(default_factory=datetime.now)

    def mark_in_progress(self) -> None:
        self.status = TaskStatus.INPROGRESS
        self.updatedAt = datetime.now()

    def mark_done(self) -> None:
        self.status = TaskStatus.DONE
        self.udpatedAt = datetime.now()

    def update_description(self, new_description: str) -> None:
        self.description = new_description
        self.udpatedAt = datetime.now()

    def get_details(self) -> str:
        created = self.createdAt.isoformat(sep=" ", timespec="minutes")
        updated = self.updatedAt.isoformat(sep=" ", timespec="minutes")
        return str(self) + f"\n\033[2mCreated:{created} Updated:{updated}\033[0m"
    
    def __status_color(self) -> str: 
        status_with_color = {
            TaskStatus.TODO: "\033[33mTodo\033[0m",
            TaskStatus.INPROGRESS: "\033[34mIn Progress\033[0m",
            TaskStatus.DONE: "\033[32mDone\033[0m",
        }
        
        return status_with_color[self.status]
        
    def __str__(self) -> str:
        return f"{self.id}: {self.description} | {self.__status_color()}"


@dataclass
class TaskList:
    _tasks: dict[int, Task] = field(default_factory=dict)
    _id_counter: int = field(default=1)

    def create_task(self, description: str) -> Task:
        task = Task(self._id_counter, description)
        self._tasks[self._id_counter] = task
        self._id_counter += 1

        return task

    def list_tasks(self) -> list[Task]:
        return list(self._tasks.values())

    def update_task(self, id: int, description: str) -> Task:
        task = self._tasks.get(id)

        if not task:
            raise ValueError(f"Task {id} does not exist")

        task.update_description(description)
        return task

    def delete_task(self, id: int) -> Task:
        task = self._tasks.pop(id, None)

        if not task:
            raise ValueError(f"Task {id} does not exist")

        return task

    def mark_task_in_progress(self, id: int) -> Task:
        task = self._tasks.get(id)

        if not task:
            raise ValueError(f"Task {id} does not exist")

        task.mark_in_progress()
        return task

    def mark_task_done(self, id: int) -> Task:
        task = self._tasks.get(id)

        if not task:
            raise ValueError(f"Task {id} does not exits")

        task.mark_done()
        return task

def format_task(task: Task, details: bool = False) -> str:
    return task.get_details() if details else str(task)

def format_task_list(task_list: TaskList, details: bool = False, status_filter: TaskStatus | None = None) -> str:
    tasks = task_list.list_tasks()

    if not tasks:
        return "No tasks saved yet!"
    
    if status_filter:
        formated_tasks = "\n".join(format_task(task, details) for task in tasks if task.status == status_filter)
    else:
       formated_tasks = "\n".join(format_task(task, details) for task in tasks)

    return formated_tasks
