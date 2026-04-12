from pathlib import Path
import sys
from typing import Sequence, TextIO

from .formatter import (
    format_add_message,
    format_delete_message,
    format_error_message,
    format_mark_done_message,
    format_mark_in_progress_message,
    format_update_message,
)
from .parser import build_parser
from .task import TaskStatus
from .tasklist import format_task_list
from .taskstorage import JsonTaskStorate, TaskStorage


def get_default_save_file() -> Path:
    return Path.home() / ".task-tracker" / "tasks.json"


def run(
    argv: Sequence[str] | None = None,
    storage: TaskStorage | None = None,
    out: TextIO | None = None,
    err: TextIO | None = None,
) -> int:
    out_stream = out or sys.stdout
    err_stream = err or sys.stderr
    args = build_parser().parse_args(argv)

    if storage is None:
        save_file = get_default_save_file()
        save_file.parent.mkdir(parents=True, exist_ok=True)
        storage = JsonTaskStorate(save_file)

    try:
        task_list = storage.load()
    except ValueError as e:
        print(format_error_message(str(e)), file=err_stream)
        return 1

    action: str = args.action

    match action:
        case "add":
            task = task_list.create_task(args.description)
            print(format_add_message(task, args.details), file=out_stream)

        case "list":
            status_filter = TaskStatus(args.status_filter) if args.status_filter else None
            print(
                format_task_list(task_list, args.details, status_filter),
                file=out_stream,
            )
            return 0

        case "delete":
            try:
                task = task_list.delete_task(args.task_id)
                print(format_delete_message(task, args.details), file=out_stream)
            except ValueError as e:
                print(format_error_message(str(e)), file=err_stream)
                return 1

        case "update":
            try:
                task = task_list.update_task(args.task_id, args.description)
                print(format_update_message(task, args.details), file=out_stream)
            except ValueError as e:
                print(format_error_message(str(e)), file=err_stream)
                return 1

        case "mark-in-progress":
            try:
                task = task_list.mark_task_in_progress(args.task_id)
                print(
                    format_mark_in_progress_message(task, args.details), file=out_stream
                )
            except ValueError as e:
                print(format_error_message(str(e)), file=err_stream)
                return 1

        case "mark-done":
            try:
                task = task_list.mark_task_done(args.task_id)
                print(format_mark_done_message(task, args.details), file=out_stream)
            except ValueError as e:
                print(format_error_message(str(e)), file=err_stream)
                return 1

        case _:
            print(format_error_message("Invalid command"), file=err_stream)
            return 1

    storage.save(task_list)
    return 0


def main() -> int:
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
