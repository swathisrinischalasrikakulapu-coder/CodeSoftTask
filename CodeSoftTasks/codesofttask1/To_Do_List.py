tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add Task
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Update Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_num = int(input("Enter task number to update: "))
            
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_num = int(input("Enter task number to delete: "))

            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(removed_task, "deleted successfully!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":
        print("Thank you for using To-Do List App!")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")