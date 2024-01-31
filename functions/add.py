

def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append(f"[Pending] {description}\n")