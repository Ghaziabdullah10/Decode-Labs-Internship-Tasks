# Project 1 - To-Do List

my_tasks = []

def show_menu():
    print("\n----- TO-DO LIST -----")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete a task")
    print("5. Exit")


def add_task():
    title = input("Enter the task: ").strip()

    if title == "":
        print("Task cannot be empty.")
        return

    task = {"title": title, "done": False}
    my_tasks.append(task)
    print(f"'{title}' has been added to your list.")


def view_tasks():
    if len(my_tasks) == 0:
        print("Your to-do list is empty.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(my_tasks):
        status = "[X]" if task["done"] else "[ ]"
        print(f"{index + 1}. {status} {task['title']}")


def mark_done():
    view_tasks()
    if len(my_tasks) == 0:
        return

    choice = input("\nEnter task number to mark as done: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    position = int(choice) - 1

    if position < 0 or position >= len(my_tasks):
        print("That task number doesn't exist.")
        return

    my_tasks[position]["done"] = True
    print(f"Marked '{my_tasks[position]['title']}' as done.")


def delete_task():
    view_tasks()
    if len(my_tasks) == 0:
        return

    choice = input("\nEnter task number to delete: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    position = int(choice) - 1

    if position < 0 or position >= len(my_tasks):
        print("That task number doesn't exist.")
        return

    removed = my_tasks.pop(position)
    print(f"Deleted '{removed['title']}'.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
