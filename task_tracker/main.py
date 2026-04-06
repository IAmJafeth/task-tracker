from .parser import parser
from .task import Task, format_task
from .tasklist import format_task_list
from .taskstorage import JsonTaskStorate
from pathlib import Path

def main():
    # Use user's home directory for tasks.json
    SAVE_FILE = Path.home() / ".task-tracker" / "tasks.json"
    SAVE_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    args = parser.parse_args()
    
    task_storage = JsonTaskStorate(SAVE_FILE)
    task_list = task_storage.load()
    
    action: str = args.action
    
    match action:
        case "add":
            task: Task = task_list.create_task(args.description)
            task_info = "\n"+task.get_details() if args.details else f"(ID: {task.id})"   
            print(f"\033[32mTask added\033[0m {task_info} ")
        
        case "list":
            print(format_task_list(task_list, args.details, args.status_filter))
        
        case "delete":
            try:
                task = task_list.delete_task(args.task_id)
                print(f"\033[0;31mTask DELETED\033[0m\n{format_task(task, args.details)}")
                
            except ValueError as e:
               print(f"\033[0;31mError\033[0m: {e}")
              
        case "update":
            try: 
                task = task_list.update_task(args.task_id, args.description)
                print(f"\033[32mTask updated\033[0m\n{format_task(task, args.details)}")
            except ValueError as e:
               print(f"\033[0;31mError\033[0m: {e}")
        
        case "mark-in-progress":
            try: 
                task = task_list.mark_task_in_progress(args.task_id)
                print(f"\033[32mTask marked in progress\033[0m\n{format_task(task, args.details)}")
            except ValueError as e:
               print(f"\033[0;31mError\033[0m: {e}")
        
        case "mark-done":
            try: 
                task = task_list.mark_task_done(args.task_id)
                print(f"\033[32mTask marked done\033[0m\n{format_task(task, args.details)}")
            except ValueError as e:
               print(f"\033[0;31mError\033[0m: {e}")
               
        case _:
            print("\033[0;31mError\033[0m: Invalid command")
    task_storage.save(task_list)

if __name__ == "__main__":
    main()
