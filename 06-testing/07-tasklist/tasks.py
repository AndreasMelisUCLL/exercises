from datetime import date


class Task():
    
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
    


class TaskList():
    
    def __init__(self) -> None:
        self.tasks: list[Task] = []
        
        
    @property
    def finished_tasks(self):
        return [
            task 
            for task in self.tasks 
            if task.finished
        ]
        
    @property
    def due_tasks(self):
        return [
            task 
            for task in self.tasks 
            if not task.finished
        ]
    
    @property
    def overdue_tasks(self):
        return [
            task 
            for task in self.due_tasks 
            if task.due_date < date.today
        ]
        
        
    def add_task(self, task: Task) -> None:
        # assert due date is not in the past
        if task.due_date < date.today():
            raise RuntimeError()
        
        self.tasks.append(task)
        
        
    def __len__(self) -> int:
        return len(self.tasks)