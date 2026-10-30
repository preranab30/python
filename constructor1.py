class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass
    def attend_class(self):
        print(f"{self.name} (age {self.age}) attended class")
s = Student("Amita", 22)
s.attend_class()