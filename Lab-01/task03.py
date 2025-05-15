import random

backup_tasks = {
    "Task1": "Completed",
    "Task2": "Failed",
    "Task3": "Completed",
    "Task4": "Failed",
    "Task5": "Failed",
}

def retry_backup(task_id):
    if random.random() < 0.5:
        return "Completed"
    else:
        return "Failed"

for task_id, status in backup_tasks.items():
    if status == "Failed":
        print(f"Retrying {task_id}...")
        backup_tasks[task_id] = retry_backup(task_id)

print("\nUpdated Backup Task Statuses:")
for task_id, status in backup_tasks.items():
    print(f"{task_id}: {status}")