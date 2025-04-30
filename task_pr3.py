def max_tasks(tasks):
    tasks.sort(key=lambda task: task['deadline'])
    
    current_time = 0
    completed_tasks = []

    for task in tasks:
        if current_time + task['duration'] <= task['deadline']:
            completed_tasks.append(task['name'])
            current_time += task['duration']
    
    return completed_tasks

tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

result = max_tasks(tasks)

print("Tasks that can be completed on time:")
for name in result:
    print(name)
