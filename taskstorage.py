import datetime
import json
from pathlib import Path
from typing import Protocol

from task import Task, TaskStatus
from tasklist import TaskList


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
            return TaskList()

        if (
            not {"id_counter", "tasks"}.issubset(data)
            or not isinstance(data.get("tasks"), list)
            or not isinstance(data.get("id_counter"), int)
        ):
            return TaskList()

        task_list = TaskList()
        task_list._id_counter = data.get("id_counter")

        for item in data["tasks"]:
            try:
                task = Task(
                    item["id"],
                    item["description"],
                    TaskStatus(item["status"]),
                    datetime.datetime.fromisoformat(item["created_at"]),
                    datetime.datetime.fromisoformat(item["updated_at"]),
                )
                task_list._tasks[task.id] = task
            except KeyError:
                continue

        return task_list
