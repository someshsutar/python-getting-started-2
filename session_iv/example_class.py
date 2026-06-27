class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} is starting")


car1 = Car("Toyota", "White")
car2 = Car("Honda", "Black")

print(car1.brand)
car2.start()