class Parent:
    def fun(self):
        print("Parent function")

class Child(Parent):
    def fun(self):
        print("Child function")
        super().fun() # reffer to parent class function

c = Child()
c.fun()