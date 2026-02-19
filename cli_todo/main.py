import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("task", nargs='*', help="The task to add.")
    parser.add_argument("-c", "--complete", nargs='?', help="Mark task as complete.")
    parser.add_argument("-l", "--list-completed", action="store_true", help="List completed tasks.")

    args = parser.parse_args()

    if not args.task:
        print("No tasks provided.")
        return

    tasks = []
    completed_tasks = []

    # Load tasks from file
    try:
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        pass

    # Add tasks
    for task in args.task:
        if task not in tasks:
            tasks.append(task)
            try:
                with open("todo.txt", "a") as f:
                    f.write(f"{task}\n")
                print(f"Task '{task}' added.")
            except Exception as e:
                print(f"Error adding task: {e}")
        else:
            print(f"Task '{task}' already exists.")

    # Mark task as complete
    if args.complete:
        if args.complete in tasks:
            tasks.remove(args.complete)
            try:
                with open("todo.txt", "w") as f:
                    f.write("\n".join(tasks))
                print(f"Task '{args.complete}' marked as complete.")
            except Exception as e:
                print(f"Error marking task as complete: {e}")
        else:
            print(f"Task '{args.complete}' not found.")

    # List completed tasks
    if args.list_completed:
        print("Completed Tasks:")
        for task in completed_tasks:
            print(f"- {task}")

    # Print all tasks
    print("\nAll Tasks:")
    for task in tasks:
        print(f"- {task}")


if __name__ == "__main__":
    main()