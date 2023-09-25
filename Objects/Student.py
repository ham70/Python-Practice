#HackBU Python WorkShop
#BasicOOP Section Challenge

class Student:
    def __init__(self, n, y, m, cl):
        self.name = n
        self.year = y
        self.major = m
        self.course_list = cl

    def add_course(self, course):
        self.course_list.append(course)

    def change_major(self, newMajor):
        self.major = newMajor

#Testing
courses = ["calc", "art", "comp sci", "basics of ee"]
ben = Student("Ben", "Freshman", "Computer Science", courses)
print(ben.major)
print(ben.name)
print(ben.course_list)
ben.change_major("EE")
print(ben.major)
ben.add_course("research")
print(ben.course_list)

