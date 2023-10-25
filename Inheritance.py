class Animal:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        self.health = 100
        self.hunger = 0

    def idle(self):
        #animals get hunger while idle
        #hungry animals lose health if they get too hungry
        self.hunger += 1
        if self.hunger >= 100:
            self.health -= 1

    def eat(self, food):
        #animals lose hunger based on the food's mass (rather calories but mass seems fair)
        self.hunger -= food.mass
    
    def report(self):
        print("Name:", self.name)
        print("Health:", self.health)
        print("Hunger:", self.hunger)

class Duck(Animal):
    def __init__(self, name, color):
        super().__init__(name, 30)# we pass 30 as the defualt mass for Ducks
        self.color = color

    def quak(self):
        print("Quack quack!")

    def eat (self, food):
        self.hunger -= food.mass
        print("nibble nibble quack")

    

quackers = Duck("quackers", "blue")
quackers.report()