import argparse

parser = argparse.ArgumentParser(
    prog="Task-Tracker",
    description="A simple CLI application to manage tasks",
    epilog="A project from @Roadmap.sh",
)

sub_parser = parser.add_subparsers(
    required=True,
    title="Action to take",
)

create_parser = sub_parser.add_parser("create", help="Create a new task")
create_parser.add_argument("description", help="Description for the new task", type=str)

update_parser = sub_parser.add_parser("update", help="Update a tasks decription")
update_parser.add_argument("task_id", help="ID of the task to update", type=int, metavar="Task ID")
update_parser.add_argument("decription", help="New description for the task", type=str, metavar="Description")

list_parser = sub_parser.add_parser("list", help="List all tasks")

delete_parser = sub_parser.add_parser("delete", help="Delete a task")
delete_parser.add_argument("task_id", help="ID of the task to be deleted", type=int, metavar="Task ID")

mark_in_progress_parser = sub_parser.add_parser("mark-in-progress", help="Mark a Task as in-progress")
mark_in_progress_parser.add_argument("task_id", help="ID of the task to be marked as in-progress", type=int, metavar="Task ID")

mark_done_parser = sub_parser.add_parser("mark-done", help= "Mark a task as done")
mark_done_parser.add_argument("task_id", help="ID of the task to be marked as done", type=int, metavar="Task ID")
