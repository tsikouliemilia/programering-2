class Person:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.__ålder = ålder
    def get_ålder(self):
        return self.__ålder

person = Person("Anna", 25)


print(person.namn)
print(person.__ålder)
