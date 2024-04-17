from StudentRegistrationSystem.degree import Degree
from StudentRegistrationSystem.lectureHall import LectureHall
from StudentRegistrationSystem.professor import Professor
from StudentRegistrationSystem.student import Student
from StudentRegistrationSystem.address import Address
from StudentRegistrationSystem.course import Course

class Main:
    def __init__(self):
        oDegree = Degree(111, 'Computer Science', 3200)
        oLectureHall = LectureHall('Bloco 2, sala 14', 40)
        oAddressStudent = Address('Avenida San Francisco', 23, 'Serra Talhada', 'Pernambuco', 'Brasil')
        oAddressProfessor = Address('Travessa João Carlos', 55, 'Triunfo', 'Pernambuco', 'Brasil')
        oProfessor = Professor(222, 'John Stuart', oAddressProfessor, 'Software Engineer')
        oCourse = Course(333, 'Machine Learning', 2, 'Maths', 60, oProfessor, oLectureHall)
        oStudent = Student(1, 'Leuh', oDegree, oAddressStudent, oCourse)

        print(oStudent)


Main()

