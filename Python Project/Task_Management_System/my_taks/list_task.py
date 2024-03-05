from .task import tasks
def list_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"Taks {i}")
        for key, value in task.items():
            print(f"{key.capitalize()}={value}")
        print()