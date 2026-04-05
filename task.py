from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum
from pprint import pprint


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


@dataclass
class TaskManager:
    _tasks: dict[int, Task] = field(default_factory=dict)
    _id_counter: int = field(default=1)

    def create_task(self, description: str) -> Task:
        task = Task(self._id_counter, description)
        self._tasks[self._id_counter] = task
        self._id_counter += 1

        return task

    def list_tasks(self) -> dict[int, Task]:
        return self._tasks

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
