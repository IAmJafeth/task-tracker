from parser import parser
from task import Task, TaskList, format_task_list

def main():
    task_list = TaskList()
    task_list.create_task("Test Task")
    args = parser.parse_args()
    
    action: str = args.action
    
    match action:
        case "add":
            task: Task = task_list.create_task(args.description)
            task_info = "\n"+task.get_details() if args.details else f"(ID: {task.id})"   
            print(f"\033[32mTask added succesfully\033[0m {task_info} ")
        
        case "list":
            print(format_task_list(task_list,args.details))
        
        case "delete":
            try:
                task = task_list.delete_task(args.task_id)
                task_info = task.get_details() if args.details else str(task)
                print(f"\033[0;31mTask DELETED\033[0m\n{task_info}")
            except ValueError as e:
               print(f"Error: {e}")

        case _:
            print("Error: Invalid command")

if __name__ == "__main__":
    main()
