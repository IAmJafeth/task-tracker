<div align="center">

# 📝 Task Tracker

![Status](https://img.shields.io/badge/status-work%20in%20progress-yellow)
![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**A simple and elegant command-line interface (CLI) application to manage your tasks**

Built with Python | Part of [Roadmap.sh Task Tracker Project](https://roadmap.sh/projects/task-tracker)

---

</div>

## ✨ Features

-  **Add, Update, Delete** - Full CRUD operations for task management
-  **Status Tracking** - Mark tasks as todo, in-progress, or done
-  **Task Filtering** - List all tasks or filter by specific status
-  **Persistent Storage** - All tasks saved automatically in JSON format *(TODO)*

## 📋 Requirements

- Python 3.13 or higher
- No external dependencies required!

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/IAmJafeth/task-tracker.git
   cd task-tracker
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Start tracking your tasks!** 🎉

## 💻 Usage

Run the task tracker using:

```bash
python main.py [command] [options]
```

### 📚 Available Commands

#### Add a new task
```bash
python main.py add "Task description"
python main.py add "Task description" -d  # Show details after adding
```

#### List tasks
```bash
python main.py list                    # List all tasks
python main.py list todo               # List tasks with status "todo"
python main.py list in-progress        # List tasks with status "in-progress"
python main.py list done               # List tasks with status "done"
python main.py list -d                 # List all tasks with details
```

#### Update a task
```bash
python main.py update <task_id> "New description"
python main.py update <task_id> "New description" -d  # Show details after updating
```

#### Delete a task
```bash
python main.py delete <task_id>
python main.py delete <task_id> -d  # Show details of deleted task
```

#### Mark task as in-progress
```bash
python main.py mark-in-progress <task_id>
python main.py mark-in-progress <task_id> -d  # Show details after marking
```

#### Mark task as done
```bash
python main.py mark-done <task_id>
python main.py mark-done <task_id> -d  # Show details after marking
```

### ⚙️ Options

| Option | Description |
|--------|-------------|
| `-d, --details` | Show detailed task information |
| `-v, --version` | Display the application version |
| `-h, --help` | Show help message |

### 📖 Examples

```bash
# Add a new task
python main.py add "Buy groceries"

# List all tasks
python main.py list

# Mark task 1 as in-progress
python main.py mark-in-progress 1

# Update task 2
python main.py update 2 "Buy groceries and cook dinner"

# Mark task 1 as done
python main.py mark-done 1

# List only done tasks with details
python main.py list done -d

# Delete task 3
python main.py delete 3
```

## 📁 Project Structure

```
task-tracker/
├── main.py          # Entry point and CLI command handlers
├── parser.py        # Command-line argument parsing
├── task.py          # Task and TaskList classes with core functionality
└── pyproject.toml   # Project metadata and configuration
```

## 📄 License

This project is created as part of the Roadmap.sh project series.

## 🔗 Links

- **Project Page:** [Roadmap.sh Task Tracker](https://roadmap.sh/projects/task-tracker)
- **Repository:** [GitHub](https://github.com/IAmJafeth/task-tracker)

---

<div align="center">

Made with ❤️ as part of the [Roadmap.sh](https://roadmap.sh) project series

</div>
