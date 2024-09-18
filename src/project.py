from datetime import datetime

class Task:
    def __init__(self, task_id, description, responsible, start_date, end_date, status, priority):
        self.task_id = task_id
        self.description = description
        self.responsible = responsible
        self.start_date = self.parse_date(start_date)
        self.end_date = self.parse_date(end_date)
        self.status = status
        self.priority = priority

    def parse_date(self, date_str): ## Conversor de data
        if isinstance(date_str, datetime):
            return date_str
        try:
            return datetime.strptime(date_str, '%d/%m/%Y')
        except ValueError:
            print(f"Formato de data inválido: {date_str}. Use DD/MM/AAAA.")
            return None
        
    def __repr__(self):
        return f"Task({self.task_id}, {self.description}, {self.status})"
    
class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status.lower() == status.lower()]

    def __repr__(self):
        return f"Project({self.name}, {len(self.tasks)} tasks)"