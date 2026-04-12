from datetime import datetime
import json
from pathlib import Path
from typing import Protocol

from .task import Task, TaskStatus
from .tasklist import TaskList


class TaskStorage(Protocol):
    def save(self, task_list: TaskList) -> None: ...
    def load(self) -> TaskList: ...


class JsonTaskStorate:
    def __init__(self, path: Path | str) -> None:
        self.path = Path(path)

    def save(self, task_list: TaskList) -> None:
        data = {
            "id_counter": task_list._id_counter,
            "tasks": [
                {
                    "id": task.id,
                    "description": task.description,
                    "status": task.status,
                    "created_at": task.created_at.isoformat(),
                    "updated_at": task.updated_at.isoformat(),
                }
                for task in task_list.list_tasks()
            ],
        }
        self.path.write_text(json.dumps(data), encoding="utf-8")

    def load(self) -> TaskList:
        if not self.path.exists():
            return TaskList()
        try:
            data: dict = json.loads(self.path.read_text())
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON content in task storage: {self.path}") from None

        if not {"id_counter", "tasks"}.issubset(data) or not isinstance(
            data.get("tasks"), list
        ):
            raise ValueError(
                "Invalid task storage format. Required keys: id_counter (int), tasks (list)"
            )

        task_list = TaskList()

        if isinstance(data["id_counter"], int):
            task_list._id_counter = data.get("id_counter")
        elif not data["tasks"]:
            task_list._id_counter = 1
        else:
            task_list._id_counter = max([task["id"] for task in data["tasks"]]) + 1

        for item in data["tasks"]:
            try:
                created_at_raw = item.get("created_at")
                updated_at_raw = item.get("updated_at")
                created_at = datetime.fromisoformat(created_at_raw) if created_at_raw else datetime.now()
                updated_at = datetime.fromisoformat(updated_at_raw) if updated_at_raw else created_at
                
                task = Task(
                    item["id"],
                    item.get("description", "DEFAULT: Description not found"),
                    TaskStatus(item.get("status", TaskStatus.TODO)),
                    created_at,
                    updated_at
                )
                task_list._tasks[task.id] = task
            except KeyError:
                continue

        return task_list
