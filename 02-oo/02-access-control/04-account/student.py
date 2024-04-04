class Account:
    def __init__(self, login, password) -> None:
        self.login = login
        self.__password = password
        
    def is_correct_password(self, pw) -> bool:
        return pw == self.__password