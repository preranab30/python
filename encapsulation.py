class Student:
    #setter
    def set_roll(self, roll):
        if roll > 0 :
            self.roll = roll
        else:
            print("Invalid roll")
            self.roll = 0

    def set_name(self, name):
        if len(name) <= 10:
            self.name = name

        else:
            print("Invalid name")
            self.name = " "

    def get_roll(self):
        return self.roll
    
    def get_name(self):
        return self.name
    
s = Student()
s.set_roll(11)
s.set_name("Usha")
print("Roll: ", s.get_roll())
print("Name: ", s.get_name())