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

if __name__ == "__main__":
    main()