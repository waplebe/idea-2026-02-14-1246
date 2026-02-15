# Simple CLI Todo List

This is a very basic command-line tool for managing a todo list.

## Usage

To add tasks, run the script with the tasks as arguments:

```bash
python main.py task1 task2 task3
```

This will print the list of tasks to the console.  The tasks are also saved to a file named `todo.txt` in the project directory.

## Persistence

The todo list is now persisted to a file named `todo.txt`. Each task is written on a new line. To view the list, run the script again. To clear the list, delete the `todo.txt` file.

## Startup

The script now loads existing tasks from `todo.txt` when it starts, displaying them before accepting new tasks.

## Clearing the List

The script can now clear the todo list. If you run the script without any arguments, it will delete the `todo.txt` file, effectively clearing the list.

## Adding Existing Tasks

The script now checks if a task already exists in the todo list before adding it. This prevents duplicate entries.