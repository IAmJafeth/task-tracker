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


