# Simple CLI Todo List

This is a command-line tool for managing a todo list. It now includes features for marking tasks as complete, viewing completed tasks, and handling errors gracefully.

## Usage

To add tasks, run the script with the tasks as arguments:

```bash
python main.py task1 task2 task3
```

This will print the list of tasks to the console and save them to `todo.txt`.

To mark a task as complete, use the `-c` flag followed by the task name:

```bash
python main.py -c task1
```

To view completed tasks, use the `-l` flag:

```bash
python main.py -l
```

To clear the todo list, delete the `todo.txt` file.

## Persistence

The todo list is persisted to `todo.txt`. Each task is written on a new line.

## Startup

The script loads existing tasks from `todo.txt` when it starts, displaying them before accepting new tasks.

## Clearing the List

The script can now clear the todo list by deleting `todo.txt`.

## Adding Existing Tasks

The script checks if a task already exists before adding it, preventing duplicates.

## New Features

*   **Task Completion:**  Tasks can be marked as complete using the `-c` flag. Completed tasks are displayed separately.
*   **Viewing Completed Tasks:** The `-l` flag displays a list of completed tasks.
*   **Error Handling:** Improved error handling for file operations and invalid input.

## Testing

The following tests ensure the core functionality of the todo list is working correctly:

```python
import unittest
import cli_todo

class TestTodoCLI(unittest.TestCase):

    def test_add_task(self):
        cli_todo.main(["task1"])
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertTrue("task1\n" in tasks)

    def test_add_multiple_tasks(self):
        cli_todo.main(["task1", "task2"])
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertTrue("task1\n" in tasks)
        self.assertTrue("task2\n" in tasks)

    def test_complete_task(self):
        cli_todo.main(["task1", "-c", "task1"])
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertTrue("task1\n" not in tasks)

    def test_list_completed_tasks(self):
        cli_todo.main(["-l"])
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        self.assertTrue("task1\n" not in tasks) # Assuming task1 was completed

    def test_no_tasks_provided(self):
        cli_todo.main()
        print("No tasks provided.")

    def test_clear_list(self):
        cli_todo.main([])
        try:
            with open("todo.txt", "r") as f:
                tasks = f.readlines()
            self.assertTrue(len(tasks) == 0)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
```

## File Structure

*   `cli_todo/README.md`:  Documentation for the project.
*   `cli_todo/main.py`:  The main script for the todo list application.