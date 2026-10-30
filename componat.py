class Employee :
    #Class Attribute
    ecomapny = "XYZ comapny"

    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        #self.ecomapny="XYZ company"
        pass
    def do_job(self, role):
        print(f"The employe {self.name} works in {role}")


    def intro(self):
        print(f"Employe Name: {self.name}")
        print(f"Employe salary: {self.salary}")
        #print("Employe company: {self.ecomapny}")
        print(f"Employe salary: {Employee.ecomapny}")

    @staticmethod
    def go_team_outing():
        print("Go to team outing")

    @classmethod
    def change_company_name(cls, new_name):
        Employee.ecomapny = new_name

Employee.change_company_name("Xyz pvt lmd")

e1 = Employee("Amita", 250000)
e1.do_job("Tester")
e1.intro()
Employee.go_team_outing()

e2 = Employee("Vishu", 290000)
e2.do_job("Developer")
e2.intro()
Employee.go_team_outing()

