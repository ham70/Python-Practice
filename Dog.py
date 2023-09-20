#Basic Object Oriented Programming with Python
#-----

class Dog:
    def __init__(self, n, c):
        self.name = n
        self.color = c
        self.tricks_kown = []

    def bark(self):
        print("Woof!")

    def train(self, new_trick):
        self.tricks_kown.append(new_trick)

    #getters
    def getName(self):
        return self.name
    def getColor(self):
        return self.color
    def getTricksKown(self):
        return self.tricks_kown
    


        
#exercise 1
greg = Dog("Greg", "brown")
print("this is my dog " + greg.name)
print("Greg is the color " + greg.color)
print(greg.name, greg.color)

#exercise 2
greg.bark()
greg.train("lay down")
print(greg.getTricksKown())



