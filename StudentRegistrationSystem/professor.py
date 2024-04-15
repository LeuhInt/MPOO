from StudentRegistrationSystem.address import Address


class Professor:
    def __init__(self, idNumber: int, name: str, address: Address, background: str):
        self.__idNumber = idNumber
        self.__name = name
        self.__address = address
        self.__background = background

    def getIdNumber(self):
        return self.__idNumber

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getBackground(self):
        return self.__background

    def setIdNumber(self, idNumber: int):
        self.__idNumber = idNumber

    def setName(self, name: str):
        self.__name = name

    def setAddress(self, address):
        self.__address = address

    def setBackground(self, background: str):
        self.__background = background
