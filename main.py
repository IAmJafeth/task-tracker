from parser import parser
from task import Task, TaskList

def main():
    task_list = TaskList()
    task_list.create_task("Test Task")
    args = parser.parse_args()
    
    action: str = args.action
    
    match action:
        case "add":
            task: Task = task_list.create_task(args.description)
            print(f"Task added succesfully (ID: {task.id})")
        
        case _:
            print("Error: Invalid command")

if __name__ == "__main__":
    main()
