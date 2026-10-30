class Mentor:
    def teaching(self):
        print("Mentor is Teaching")

    def __init__(self):
        self.name = "Deppu"
        self.tech = "Java"

m = Mentor()
print(m.name)
print(m.tech)
m.teaching()
