### Armazenamento de projetos

import json
from project import Project, Task

def save_project(project, file_path):
    data = {
        'name': project.name,
        'tasks': [{
            'task_id': task.task_id,
            'description': task.description,
            'responsible': task.responsible,
            'start_date': task.start_date.strftime('%d/%m/%Y') if task.start_date else None,
            'end_date': task.end_date.strftime('%d/%m/%Y') if task.end_date else None,
            'status': task.status,
            'priority': task.priority
        } for task in project.tasks]
    }