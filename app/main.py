import sys
from pathlib import Path

# Add the 'functions' directory to sys.path
functions_path = r'C:\Users\nizam\OneDrive\Desktop\python\ToDo\functions'
sys.path.append(str(functions_path))
    
# from functions.load import load_tasks
# from functions.display import display_tasks
# from functions.add import add_task
# from functions.change import change_task_status
# from functions.edit import edit_task
# from functions.save import save_tasks
# from functions.delete import delete_task

from load import load_tasks
from display import display_tasks
from add import add_task
from change import change_task_status
from edit import edit_task
from save import save_tasks
from delete import delete_task

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Change Task Status")
        print("5. Delete Task")
        print("6. Save and Exit")

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
            delete_task(tasks)
        elif choice == '6':
            save_tasks(tasks, filename)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
