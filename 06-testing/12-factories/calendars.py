from datetime import date


class Calendar():       
    @property
    def today(self) -> date:
        return date.today()


class CalendarStub(Calendar):
    def __init__(self, date: date) -> None:
        self.today = date
            
    @property
    def today(self) -> date:
        return self.__today
    
    @today.setter
    def today(self, value: date) -> None:
        self.__today = value