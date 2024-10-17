# Utility functions for categorizing tasks
# utils/categorizer.py

def categorize_tasks(tasks):
    matrix = {
        'do_first': [],        # Urgent and Important
        'schedule': [],        # Not Urgent but Important
        'delegate': [],        # Urgent but Not Important
        'eliminate': []        # Neither Urgent nor Important
    }
    for task in tasks:
        importance = task['importance'] == 'True'
        urgency = task['urgency'] == 'True'

        if importance and urgency:
            matrix['do_first'].append(task)
        elif importance and not urgency:
            matrix['schedule'].append(task)
        elif not importance and urgency:
            matrix['delegate'].append(task)
        else:
            matrix['eliminate'].append(task)
    return matrix
