# Tascy
a simple CLI to-do list made with Python &amp; SQLite

## Features
* CRUD operations (Create, Read, Update, Delete tasks)
* Interactive mode for menu-driven usage
* Argument-driven mode for quick commands
* Search and filter tasks by status or keywords
* Bulk update capabilities
* Persistent SQLite storage
* Input validation and confirmation prompts


## Installation

1. Clone the repository:
```
git clone https://github.com/silentfin/tascy.git
```

2. Navigate into the directory:
```
cd tascy
```

## Usage

### Interactive Mode
```bash
python tascy.py
```
Launches an interactive menu where you can choose operations.  
Enter `h` to see all available commands.
```
Enter your choice: h

All operations:
h  - Help
q  - Quit
a  - Add task
d  - Delete task
u  - Update task
f  - Mark task as finished
r  - Mark task as undone
fa - Mark all tasks done
ra - Mark all tasks undone
s  - Show all tasks
sp - Show pending tasks
sf - Show finished tasks
se - Search tasks
c  - Count total tasks
g  - Get task by ID
delall - Delete all tasks
```


### CLI Mode
Use flags for quick operations:
```bash
# Add a task
python tascy.py --add "Buy groceries"
python tascy.py -a "Finish homework"

# Show all tasks
python tascy.py --show
python tascy.py -s

# Show only pending tasks
python tascy.py --show-pending

# Show only finished tasks
python tascy.py --show-finished

# Mark task as done (by ID)
python tascy.py --done 1
python tascy.py -f 1

# Mark task as undone
python tascy.py --undone 1
python tascy.py -r 1

# Update task text
python tascy.py --update 1 "Updated task description"
python tascy.py -u 1 "New task text"

# Delete a task
python tascy.py --delete 1
python tascy.py -d 1

# Search tasks
python tascy.py --search "groceries"

# Count total tasks
python tascy.py --count

# Get specific task by ID
python tascy.py --get 1

# Bulk operations
python tascy.py --done-all       # Mark all as done
python tascy.py --undone-all     # Mark all as undone
python tascy.py --delete-all     # Delete all tasks (requires confirmation in interactive mode)
```

## License
This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for more details.

*Made this in September 2025*