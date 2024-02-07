
from functions.load import load_tasks
from functions.display import display_tasks
from functions.add import add_task
from functions.change import change_task_status
from functions.edit import edit_task
from functions.save import save_tasks
from functions.delete import delete_task
from functions.progress import task_progress

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Change Task Status")
        print("5. Change the progress of the tasks")
        print("6. Delete Task")
        print("7. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            change_task_status(tasks)
        elif choice == '5':
            task_progress(tasks)
        elif choice == '6':
            delete_task(tasks)
        elif choice == '7':
            save_tasks(tasks, filename)
            print("Tasks saved. Exiting.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
