class Course:
    def __init__(self, code: int, name: str, semester: int, requisites: str, contactHours: int):
        self.__code = code
        self.__name = name
        self.__semester = semester
        self.__requisites = requisites
        self.__contactHours = contactHours

    def getCode(self):
        return self.__code

    def getName(self):
        return self.__name

    def getSemester(self):
        return self.__semester

    def getRequisites(self):
        return self.__requisites

    def getContactHours(self):
        return self.__contactHours

    def setCode(self, code):
        self.__code = code

    def setName(self, name):
        self.__name = name

    def setSemester(self, semester):
        self.__semester = semester

    def setRequisites(self, requisites):
        self.__requisites = requisites

    def setContactHours(self, contactHours):
        self.__contactHours = contactHours


