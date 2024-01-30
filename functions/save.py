

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        file.writelines(tasks)