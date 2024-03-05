from my_taks import delete_task, update_task, add_task, list_task

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date: ")
            priority = input("Enter task priority: ")
            add_task.add_tasks(title, description, due_date, priority)
        elif choice == '2':
            list_task.list_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to update: "))
            key = input("Enter field to update (title/description/due_date/priority/status): ")
            value = input("Enter new value: ")
            update_task.update_tasks(task_index, key, value)
        elif choice == '4':
            task_index = int(input("Enter task index to delete: "))
            delete_task.delete_tasks(task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()