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
update_parser.add_argument("Task ID", help="ID of the task to update", type=int)
update_parser.add_argument("Decription", help="New description for the task", type=str)

list_parser = sub_parser.add_parser('list', help="List all tasks")