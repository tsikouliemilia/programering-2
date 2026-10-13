class Animal:
    def __init__(self, name):
        self.name = name 
        self.__hunger = 5
        self.__happiness= 5
        self.__energy = 5

    def make_sound(self):
        print("djuret låter.")

    def feef(self):
        self.__hunger = max(0, self.__hunger - 2)
        print(self.name, "har fååt mat!")

    def play(self):
        self.__happiness = min(10, self.__happiness + 2)
        self.__energy = max(0,self.__energy - 2)
        print(self.name, "vilar nu.")

    def show_status(self):
        print(
            f"{self.name}"
            f"Hunger: {self.__hunger}/10"
            f"Happiness:{self.__happiness}/10"
            f"Energi{self.__energi}/10"

        )

    def ready_for_adoption(self):
        return(
            self.__hunger <= 2
            and self.__happines >= 7
            and self.__energy >=5
        )
    
    class Dog