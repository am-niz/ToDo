def display_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")
