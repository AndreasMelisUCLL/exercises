import itertools


class Book():
    @staticmethod
    def __is_valid_title(title:str) -> None:
        return len(title.strip()) > 0
        
    @staticmethod
    def __is_valid_isbn(isbn:str) -> None:
        # collect digits
        digits = [int(char) for char in isbn if char.isdigit()]
            
        # verify digit count
        if len(digits) != 13:
            return False
        
        # verify checksum   
        checksum = sum(
            digit * weight
            for digit, weight in zip(digits, itertools.cycle([1, 3]))
        ) 
        if checksum % 10 != 0:
            raise RuntimeError(f'checksum is invalid. checksum: "{checksum}"')
        
        
    def __init__(self, title, isbn) -> None:
        # verify params
        if not Book.__is_valid_title(title):
            raise RuntimeError('invalid title')
        if not Book.__is_valid_isbn(isbn):
            raise RuntimeError('invalid isbn')
        
        # assign properties
        self.__title = title
        self.__isbn = isbn
    
    
    @property
    def title(self):
        return self.__title
    
    
    @property
    def isbn(self):
        return self.__isbn