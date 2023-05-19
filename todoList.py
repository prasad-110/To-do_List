def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: "))
    if task_number <= len(tasks):
        tasks[task_number - 1] = f"[DONE] {tasks[task_number - 1]}"
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: "))
    if task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task number.")

print("Welcome to the To-Do List App!")
todo_list = []

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task(todo_list)
    elif choice == "2":
        view_tasks(todo_list)
    elif choice == "3":
        mark_completed(todo_list)
    elif choice == "4":
        delete_task(todo_list)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
