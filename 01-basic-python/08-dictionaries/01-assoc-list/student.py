# write your code here
class AssocList:
    def __init__(self):
        self.__items = []
        
    def __setitem__(self, key, value):
        for item in self.__items:
            if item[0] == key:
                item[1] = value
                return
        self.__items.append([key, value])
        
    def __getitem__(self, key):
        for item in self.__items:
            if item[0] == key:
                return item[1]
        raise KeyError()
        
    def __contains__(self, key) -> bool:
        for item in self.__items:
            if item[0] == key:
                return True
        return False
    
    def __len__(self) -> int:
        return len(self.__items)
    
    @property
    def keys(self):
        return [item[0] for item in self.__items]
    
    @property
    def values(self):
        return [item[1] for item in self.__items]
    
    
    
    