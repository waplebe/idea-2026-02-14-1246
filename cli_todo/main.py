import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("task", nargs='+', help="The task to add.")
    args = parser.parse_args()

    if not args.task:
        print("No tasks provided.")
        return

    print("Tasks:")
    for task in args.task:
        print(f"- {task}")

    # Add persistence using a simple file
    with open("todo.txt", "a") as f:
        for task in args.task:
            f.write(f"{task}\n")

    # Load tasks from file on startup
    try:
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
            print("\nLoaded tasks from file:")
            for task in tasks:
                print(f"- {task}")
    except FileNotFoundError:
        pass

    # Clear the todo list when the script is run without arguments
    if len(args.task) == 0:
        try:
            with open("todo.txt", "w") as f:
                f.write("")
            print("\nTodo list cleared.")
        except FileNotFoundError:
            pass

    # Add task to the list if it doesn't already exist
    for task in args.task:
        try:
            with open("todo.txt", "r") as f:
                existing_tasks = [line.strip() for line in f.readlines()]
                if task not in existing_tasks:
                    with open("todo.txt", "a") as f:
                        f.write(f"{task}\n")
                    print(f"Task '{task}' added.")
        except FileNotFoundError:
            with open("todo.txt", "w") as f:
                f.write(f"{task}\n")
            print(f"Task '{task}' added.")


if __name__ == "__main__":
    main()