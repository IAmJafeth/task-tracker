from .task import Task, TaskStatus, format_task
from dataclasses import dataclass, field

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
        
        
def format_task_list(task_list: TaskList, details: bool = False, status_filter: TaskStatus | None = None) -> str:
    tasks = task_list.list_tasks()

    if not tasks:
        return "No tasks saved yet!"
    
    if status_filter:
        formated_tasks = "\n".join(format_task(task, details) for task in tasks if task.status == status_filter)
    else:
       formated_tasks = "\n".join(format_task(task, details) for task in tasks)

    return formated_tasks
