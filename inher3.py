class Parent:
    def __init__(self):
        print("Parent constructor")
        self.b = 10
    def fun(self):
        print("Parent function")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("child constructor")
        self.a = 20
        print("Child a = ", self.a)
        #print("Parent a = ", super().a) Error 
        print("Parent b = ", super().__getattribute__('b'))
    def fun(self):
        print("Child funstion")
        super().fun()

c = Child()
c.fun()