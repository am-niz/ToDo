def delete_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter task number to delete: "))
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
    else:
        print("Invalid task number.")
