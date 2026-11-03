class Animal:
    def __init__(self, name):
        self.name = name 
        self.__hunger = 5
        self.__happiness= 5
        self.__energy = 5

    def make_sound(self):
        print("djuret låter.")

    def feed(self):
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
            f"Energi{self.__energy}/10"

        )

    def ready_for_adoption(self):
        return(
            self.__hunger <= 2
            and self.__happiness >= 7
            and self.__energy >=5
        )
    
class Dog(Animal):
    def make_sound(self):
        print("Vov vov!")

class Cat(Animal):
    def make_sound(self):
        print("Mjau!")

class Shelter:
    def __init__(self):
         self.animals = [
            Dog("inu"),
            Cat("herman")
        ]
    
    def show_animals(self):
        for i, animal in enumerate(self.animals, start=1):
            print(f"{i}.", end="")
            animal.show_status()
    
    def play_game(self):
        while True:
            print("\in --- Djurhemmet---")
            self.show_animals()
            print("0. Avsluta")

            try:
                choice = int(input("välj ett djur:"))
            except ValueError:
                print("Skriv ett numer.")
                continue

            if choice == 0:
                print ("Tack för att du tog hand om djuren!")
                break

            if choice < 1 or choice > len(self.animals):
                print("ogiltigt val.")
                continue

            animal= self.animals[choice - 1]

            while True:
                print(f"\n Du tar hand om {animal.name}")
                animal.make_sound()
                print("1. Mata")
                print("2. Lek")
                print("3. Vila")
                print("4. Tillbaka")

                Action = input(" Välj aktivitet:")

                if Action == "1":
                    animal.feed()
                elif Action == "2":
                    animal.play()
                elif Action =="3":
                    animal.rest()
                elif Action == "4":
                    break
                else:
                    print("ogiltig val.")
                    continue

                animal.show_status()

                if animal.ready_for_adoption():
                    print(
                        animal.name,
                        "är redu för adoption!"
                    
                    )


shelter= Shelter()
shelter.play_game()
