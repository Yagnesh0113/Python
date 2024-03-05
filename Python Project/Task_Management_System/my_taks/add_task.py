from .task import tasks
import json
def add_tasks(title, description, due_date, priority):
    tasks.append({
        'title': title,
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'status': 'Pending'
    })
    
    # with open('Task_Management_System\my_taks\credentials.json', 'w') as f:
    #     json.dump(tasks, f, indent=4)
    print("Task added successfully")