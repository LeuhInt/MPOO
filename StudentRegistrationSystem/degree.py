class Degree:
    def __init__(self, code: int, name: str, duration: int):
        self.__code = code
        self.__name = name
        self.__duration = duration

    def getCode(self):
        return self.__code

    def getName(self):
        return self.__name

    def getDuration(self):
        return self.__duration

    def setCode(self, code: int):
        self.__code = code

    def setName(self, name: str):
        self.__name = name

    def setDuration(self, duration: int):
        self.__duration = duration

