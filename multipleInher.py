#multiple Inheritance
class Singer:
    def sing(self):
        print("Singer sing song")

class Painter:
    def paint(self):
        print("Painter paint the color")

class Artist(Singer,Painter):
    pass

a = Artist()
a.sing()
a.paint()

    