from StudentRegistrationSystem.degree import Degree
from StudentRegistrationSystem.address import Address
from StudentRegistrationSystem.course import Course


class Student:
    def __init__(self, idNumber: int, name: str, degree: Degree, address: Address, course: Course):
        self.__idNumber = idNumber
        self.__name = name
        self.__degree = degree
        self.__address = address
        self.__course = course

    def getIdNumber(self):
        return self.__idNumber

    def getName(self):
        return self.__name

    def getDegree(self):
        return self.__degree

    def getAddress(self):
        return self.__address

    def getCourse(self):
        return self.__course

    def setIdNumber(self, idNumber: int):
        self.__idNumber = idNumber

    def setName(self, name: str):
        self.__name = name

    def setDegree(self, degree):
        self.__degree = degree

    def setAddress(self, address):
        self.__address = address

    def setCourse(self, course):
        self.__course = course

    def __str__(self):
        return (f'{'ENROLLMENT':^60}\n'
                f'{'-' * 60}\n'
                f'{'STUDENT INFORMATION':^30}\n'
                f'{'-' * 60}\n'
                f'ID Number: {self.getIdNumber()}\n'
                f'Student name: {self.getName()} \n'
                f'Address: {self.getAddress()} \n'
                f'{'-' * 60}\n'
                f'{'DEGREE INFORMATION':^30}\n'
                f'{'-' * 60}\n'
                f'{self.getDegree()}\n'
                f'{'-' * 60}\n'
                f'{'COURSE INFORMATION':^30}\n'
                f'{'-' * 60}\n'
                f'Course code: {self.getCourse().getCode()}\n'
                f'Course name: {self.getCourse().getName()}\n'
                f'Course duration: {self.getCourse().getContactHours()}h\n'
                f'Requisites: {self.getCourse().getRequisites()}\n'
                f'Professor name: {self.getCourse().getProfessor().getName()}\n'
                f'Lecture Hall: {self.getCourse().getLectureHall()}\n')
