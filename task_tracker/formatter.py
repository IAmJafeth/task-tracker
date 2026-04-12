from .task import Task, format_task

GREEN = "32"
RED = "0;31"


def colorize(text: str, color_code: str) -> str:
    return f"\033[{color_code}m{text}\033[0m"


def success(text: str) -> str:
    return colorize(text, GREEN)


def error(text: str) -> str:
    return colorize(text, RED)


def format_add_message(task: Task, details: bool) -> str:
    task_info = f"\n{task.get_details()}" if details else f"(ID: {task.id})"
    return f"{success('Task added')} {task_info}"


def format_update_message(task: Task, details: bool) -> str:
    return f"{success('Task updated')}\n{format_task(task, details)}"


def format_mark_in_progress_message(task: Task, details: bool) -> str:
    return f"{success('Task marked in progress')}\n{format_task(task, details)}"


def format_mark_done_message(task: Task, details: bool) -> str:
    return f"{success('Task marked done')}\n{format_task(task, details)}"


def format_delete_message(task: Task, details: bool) -> str:
    return f"{error('Task DELETED')}\n{format_task(task, details)}"


def format_error_message(message: str) -> str:
    return f"{error('Error')}: {message}"
