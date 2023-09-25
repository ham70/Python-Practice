food = ["apple", "orange", "grapes", "spinach", "carrot"]

print(food)

#removing the vegetables
food.remove("spinach")
food.remove("carrot")
print(food)

#adding pizza to the list
food.append("pizza")
print(food)

#replacing one fruit with an icecream flavor
index = food.index("grapes")
food[index] = "chocolate"
print(food)

#searching for vanilla and printing "basic" if found
if(food.count("vanilla") > 0):
    print("basic")


