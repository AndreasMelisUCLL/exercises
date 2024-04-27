from datetime import date
from calendars import *


class Task:
    def __init__(self, description, due_date: date) -> None:
        self.__description = description
        self.__due_date = due_date
        self.finished = False
        
    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date


class TaskList:
    def __init__(self, calendar: Calendar) -> None:
        self.__calendar = calendar
        self.__tasks: list[Task] = []
        
    def __len__(self) -> int:
        return len(self.__tasks)
        
        
    def add_task(self, task: Task) -> None:
        if task.due_date < self.__calendar.today: 
            raise RuntimeError()      
        self.__tasks.append(task) 
        
    @property
    def finished_tasks(self):
        return [task for task in self.__tasks if task.finished]
        
    @property
    def due_tasks(self):
        return [task for task in self.__tasks if not task.finished]
    
    @property
    def overdue_tasks(self):
        return [task for task in self.due_tasks if task.due_date < self.__calendar.today]
        