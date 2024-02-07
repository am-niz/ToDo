
from functions.display import display_tasks

def change_task_status(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter task number to change status: "))
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        if task.startswith("[Done]"):
            tasks[task_number - 1] = "[Pending]" + task[6:]
        else:
            tasks[task_number - 1] = "[Done]" + task[9:]
    else:
        print("Invalid task number.")
