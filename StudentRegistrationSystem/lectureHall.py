class LectureHall:
    def __init__(self, name: str, seats: int):
        self.__name = name
        self.__seats = seats

    def getName(self):
        return self.__name

    def getSeats(self):
        return self.__seats

    def setName(self, name: str):
        self.__name = name

    def setSeats(self, seats: int):
        self.__seats = seats

    def __str__(self):
        return f'Name: {self.getName()}, Seats: {self.getSeats()}'
