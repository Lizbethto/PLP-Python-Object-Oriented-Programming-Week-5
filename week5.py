# Part 1: Smartphone Class Example
# Defining a class
class Smartphone:
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable


# Creating objects with unique attributes
smartphone1 = Smartphone("black", "Samsung")
smartphone2 = Smartphone("blue", "Tecno")

print(smartphone1.color)  
print(smartphone2.model) 


#Inheritance example
class Smartphone:
    def __init__(self, battery_life):
        self.battery_life = battery_life

class Smartphone(Smartphone):
    pass

smartphone = Smartphone(100)
print(smartphone.battery_life)  


# Part 2: Polymorphism Challenge
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚤")

class Bird:
    def move(self):
        print("Flying 🐦")