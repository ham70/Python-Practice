#List exercise

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

#Challenge-------------------------------------------------------------
print("")
print("challenege----------------------------------")

list = [75, 97, 116, 101, 32, 83, 109, 101, 108, 108, 115]


def average(lis):
    return sum(lis) / len(lis)

# Leave this alone -- it'll make sure your function works!
assert average(list) == 95.0
