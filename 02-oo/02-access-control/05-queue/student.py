class Queue:
    def __init__(self) -> None:
        self.__queue = []
        
    def add(self, item) -> None:
        self.__queue.append(item)
        
    def next(self):
        return self.__queue.pop(0)
        
    def is_empty(self):
        return len(self.__queue) == 0