class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def open_sunroof(self):
        print("Sunroof Opened")


car = Car()

car.start()
car.open_sunroof()