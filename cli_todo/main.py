```python
import argparse
import os
import datetime

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("task", nargs='*', help="The task to add.")
    parser.add_argument("-c", "--complete", nargs='?', help="Mark task as complete.")
    parser.add_argument("-l", "--list-completed", action="store_true", help="List completed tasks.")
    parser.add_argument("-f", "--filter", choices=['active', 'completed'], help="Filter tasks by status (active or completed)")
    parser.add_argument("-p", "--priority", choices=['High', 'Medium', 'Low'], help="Filter tasks by priority (High, Medium, Low)")
    parser.add_argument("-d", "--due-date", help="Set the due date for the task (YYYY-MM-DD)")

    args = parser.parse_args()

    if not args.task:
        print("No tasks provided.")
        return

    tasks = []
    completed_tasks = []
    priorities = {'High': 3, 'Medium': 2, 'Low': 1}  # Define priority order
    
    # Load tasks from file
    try:
        with open("todo.txt", "r") as f:
            lines = f.readlines()
            if lines:
                # Parse each line into task, priority, and due date
                for line in lines:
                    parts = line.strip().split(',')
                    if len(parts) >= 2:
                        task = parts[0]
                        priority = parts[1].strip()
                        due_date_str = parts[2].strip() if len(parts) > 2 else None
                        
                        try:
                            if due_date_str:
                                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
                            else:
                                due_date = None
                            tasks.append({"task": task, "priority": priority, "due_date": due_date})
                        except ValueError:
                            print(f"Invalid due date format: {due_date_str}. Skipping task.")
                    else:
                        print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        pass

    # Add tasks
    for task in args.task:
        if task not in tasks:
            new_task = {"task": task, "priority": "Medium", "due_date": None}
            tasks.append(new_task)
            try:
                with open("todo.txt", "a") as f:
                    f.write(f"{task},{new_task['priority']},{new_task['due_date']}\n")
                print(f"Task '{task}' added.")
            except Exception as e:
                print(f"Error adding task: {e}")
        else:
            print(f"Task '{task}' already exists.")

    # Mark task as complete
    if args.complete:
        if args.complete in [task['task'] for task in tasks]:
            task_to_complete = next(task for task in tasks if task['task'] == args.complete)
            task_to_complete['status'] = 'completed'
            try:
                with open("todo.txt", "w") as f:
                    for task in tasks:
                        f.write(f"{task['task']},{task['priority']},{task['due_date']}\n")
                print(f"Task '{args.complete}' marked as complete.")
            except Exception as e:
                print(f"Error marking task as complete: {e}")
        else:
            print(f"Task '{args.complete}' not found.")

    # List completed tasks
    if args.list_completed:
        print("Completed Tasks:")
        for task in completed_tasks:
            print(f"- {task['task']} (Priority: {task['priority']}, Due Date: {task['due_date']})")

    # Print all tasks
    print("\nAll Tasks:")
    for task in tasks:
        if task['status'] == 'completed':
            print(f"- {task['task']} (Priority: {task['priority']}, Due Date: {task['due_date']})")
        else:
            print(f"- {task['task']} (Priority: {task['priority']}, Due Date: {task['due_date']})")

if __name__ == '__main__':
    main()
```