def display_tasks(tasks):
    
    if tasks is None or not tasks:

        print("No tasks in your to-do list.")
    else:
        print("Your To-Do List:")
        for i in range(len(tasks)):
            task = tasks[i]
            print(f"{i+1}. {task['name']} - {'Completed' if task['completed'] else 'Pending'}")

def add_task(tasks, task_name):
    tasks.append({"name": tasks "completed": False})
    print(f"Task '{task_name}' added.")

def mark_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter the task name: ")
            add_task(tasks, task_name)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            display_tasks(tasks)
            try:
                task_index = int(input("Enter the number of the task to mark as completed: "))
                mark_completed(tasks, task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()