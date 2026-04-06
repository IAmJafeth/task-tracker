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
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def mark_in_progress(self) -> None:
        self.status = TaskStatus.INPROGRESS
        self.updated_at = datetime.now()

    def mark_done(self) -> None:
        self.status = TaskStatus.DONE
        self.updated_at = datetime.now()

    def update_description(self, new_description: str) -> None:
        self.description = new_description
        self.updated_at = datetime.now()

    def get_details(self) -> str:
        created = self.created_at.isoformat(sep=" ", timespec="minutes")
        updated = self.updated_at.isoformat(sep=" ", timespec="minutes")
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

def format_task(task: Task, details: bool = False) -> str:
    return task.get_details() if details else str(task)

