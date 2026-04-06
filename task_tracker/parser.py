import argparse
from . import __version__


def get_app_version() -> str:
    return __version__


global_parser = argparse.ArgumentParser(add_help=False)
global_parser.add_argument(
    "-d", "--details", help="Show task details", action="store_true", default=False
)

parser = argparse.ArgumentParser(
    prog="Task-Tracker",
    description="A simple CLI application to manage tasks",
    epilog="A project from @Roadmap.sh",
    parents=[global_parser]
)

parser.add_argument(
    "-v",
    "--version",
    help="Return the task-tracker version installed",
    action="version",
    version=get_app_version(),
)

sub_parser = parser.add_subparsers(required=True, title="Action to take", dest="action")

add_parser = sub_parser.add_parser("add", help="Add a new task", parents=[global_parser])
add_parser.add_argument("description", help="Description for the new task", type=str)

update_parser = sub_parser.add_parser("update", help="Update a tasks decription", parents=[global_parser])
update_parser.add_argument(
    "task_id", help="ID of the task to update", type=int, metavar="Task ID"
)
update_parser.add_argument(
    "description", help="New description for the task", type=str, metavar="Description"
)

list_parser = sub_parser.add_parser("list", help="List all tasks", parents=[global_parser])
list_parser.add_argument("status_filter", help="Filter tasks by status", metavar="Status Filter", choices=["todo", "in-progress", "done"], nargs="?")

delete_parser = sub_parser.add_parser("delete", help="Delete a task", parents=[global_parser])
delete_parser.add_argument(
    "task_id", help="ID of the task to be deleted", type=int, metavar="Task ID"
)

mark_in_progress_parser = sub_parser.add_parser(
    "mark-in-progress", help="Mark a Task as in-progress", parents=[global_parser]
)
mark_in_progress_parser.add_argument(
    "task_id",
    help="ID of the task to be marked as in-progress",
    type=int,
    metavar="Task ID",
)

mark_done_parser = sub_parser.add_parser("mark-done", help="Mark a task as done", parents=[global_parser])
mark_done_parser.add_argument(
    "task_id", help="ID of the task to be marked as done", type=int, metavar="Task ID"
)
