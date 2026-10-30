#does constructor participate in inheritance
class Parent:
    def __int__(self):
        print("Parent constructor")

class Child1(Parent):
    pass

class Child2(Parent):
    def __init__(self):
        print("Child2 constructor")

    


c1 = Child1() # Parent constructor
c2 = Child2() #child constructor
        