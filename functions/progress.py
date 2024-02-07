from functions.display import display_tasks

def task_progress(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter task number to change progress: "))

    if 1 <= task_number <= len(tasks):
        status = input("enter task completion percentage : ")
        tasks[task_number-1] = tasks[task_number-1].strip() + f" - {status}%\n"
        print("status edited successfully.")
        

       
    
