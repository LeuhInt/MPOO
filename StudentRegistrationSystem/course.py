from StudentRegistrationSystem.lectureHall import LectureHall
from StudentRegistrationSystem.professor import Professor


class Course:
    def __init__(self, code: int, name: str, semester: int, requisites: str, contactHours: int, professor: Professor,
                 lectureHall: LectureHall):
        self.__code = code
        self.__name = name
        self.__semester = semester
        self.__requisites = requisites
        self.__contactHours = contactHours
        self.__professor = professor
        self.__lectureHall = lectureHall

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

    def getProfessor(self):
        return self.__professor

    def getLectureHall(self):
        return self.__lectureHall

    def setCode(self, code: int):
        self.__code = code

    def setName(self, name: str):
        self.__name = name

    def setSemester(self, semester: int):
        self.__semester = semester

    def setRequisites(self, requisites: str):
        self.__requisites = requisites

    def setContactHours(self, contactHours: int):
        self.__contactHours = contactHours

    def setProfessor(self, professor):
        self.__professor = professor

    def setLectureHall(self, lectureHall):
        self.__lectureHall = lectureHall
