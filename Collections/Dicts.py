#dictionary practice

my_dict = {} #declartion of a dictionary

#Key: Value
pets = {"Dog": "Rufus", "Cat": "Ringo", "Fish": "Bubbles"}

my_dog = pets["Dog"]#note the closed barackets used to access the element
print(my_dog)#prints "Rufus" the value associated with the Key "Dog"

#adding another element
pets["Bird"] = "Polly"
print(pets)

#removing elements 
pets.pop("Fish")
print(pets)

#-------------------------------------------------------------------------------------
#dictionary exercise
print("")
print("exercise----------------------------------------")


classes = {"CS120": "Madden", "Math224": "Zeke", "Writ111": "Saloni"}
print(classes)

classes["CS101"] = "George"
classes["CS120"] = "Matt"

print(classes)

