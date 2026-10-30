class Student:
    def __init__(self, roll , name, cgpa):
        self.__roll = roll           # declaring roll as a Private
        self.name = name             #public
        self._cgpa = cgpa             #protected

s = Student(101,"deep", 8.6)
#print(s.__roll)  error
#Accesing private variable using : NAME MANGLING (_className + var)
print(s._Student__roll)
# Accsing public variable
print(s.name)
# Accesing protected variable
print(s._cgpa)