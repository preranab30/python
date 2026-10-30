class SoftwareEng:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        pass
    def intro(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"salary: {self.salary}")

class Developer(SoftwareEng):
    def coding(self):
        print("Developer do coding")

class Tester(SoftwareEng):
    def debugg(self):
        print("Tster Debug the code")

d =  Developer("Rekha",30, 40000)
d.intro()
d.coding()

t = Tester("Renuka", 45, 500000)
t.intro()
t.debugg()

        