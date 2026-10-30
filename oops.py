class Mentor:
    def define_state(self):
        self.name:"deep"
        self.age:30
        self.tech:"java"

    def teaching(self):
        print("Mentor is teaching")
    
    def groomin(self):
        print("mantor is grooming")

m = Mentor()
m.define_state()
m.teaching()
m.groomin()

#print(f"Name : {m.name}")
print(f"age : {m.age}")