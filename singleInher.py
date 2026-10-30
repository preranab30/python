#Base class
class Vehical:
    def start(self):
        print("Vehical is starting")

#subclass
class Car(Vehical):
    def honk(self):
        print("Car hoking song bee bee")

c = Car()
c.start()
c.honk()