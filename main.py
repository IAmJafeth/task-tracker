from parser import parser
from task import Task, TaskList, format_task, format_task_list

def main():
    task_list = TaskList()
    task_list.create_task("Test Task")
    task_list.create_task("Second Task")
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
                print(f"\033[0;31mTask DELETED\033[0m\n{format_task(task, args.details)}")
                
            except ValueError as e:
               print(f"\033[0;31mError\033[0m: {e}")
              
        case "update":
            try: 
                task = task_list.update_task(args.task_id, args.description)
                print(f"\033[32mTask updated succesfully\033[0m\n{format_task(task, args.details)}")
            except ValueError as e:
               print(f"\033[0;31mError\033[0m: {e}")
               
        case _:
            print("\033[0;31mError\033[0m: Invalid command")

if __name__ == "__main__":
    main()
