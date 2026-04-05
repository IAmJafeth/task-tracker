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
        

if __name__ == "__main__":
    main()
