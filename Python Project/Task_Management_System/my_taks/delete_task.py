from .task import tasks
def delete_tasks(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid task index!")