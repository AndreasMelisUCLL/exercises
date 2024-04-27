class Student:
    
    def __init__(self, id:int):
        self.id = id;
        
    def __repr__(self) -> str:
        return f"Student: {self.id}"