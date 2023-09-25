#exercise 1
first = "John"
last = "Smith"
name = first + " " + last
print(name)

#exercise 2
lunch = "chicken and rice"
lunch = lunch[-5:]
print(lunch)

#Section Challenge
def stringsAreFun(string):
  #Implement me!
  if string[0].isupper():
    return string.upper()
  elif string.count("p") >= 2:
    return string[0:2]
  else:
    return string + " HackBu is cool"
  

assert(stringsAreFun("Pickles") == "PICKLES")
assert(stringsAreFun("apples") == "ap")
assert(stringsAreFun("It's true that"))
print("Good Job, you completed this exercise!")