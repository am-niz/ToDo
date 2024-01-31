def edit_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter task number to edit: "))
    if 1 <= task_number <= len(tasks):
        description = input("Enter new description: ")
        status = "[Done]" if tasks[task_number - 1].startswith("[Done]") else "[Pending]"
        tasks[task_number - 1] = f"{status} {description}\n"
    else:
        print("Invalid task number.")
