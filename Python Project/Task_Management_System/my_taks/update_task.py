from .task import tasks

def update_tasks(task_index, key, value):
    if task_index >= 1 and task_index <= len(tasks):
        tasks[task_index - 1][key] = value
        print("Task updated successfully!")
    else:
        print("Invalid task index!")