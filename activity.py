# Base class representing a general Vehicle
class Vehicle:
    def move(self):
        pass  # To be implemented by subclasses

# Car class inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Bike class inherits from Vehicle
class Bike(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# Base class representing an Animal
class Animal:
    def move(self):
        pass  # To be implemented by subclasses

# Dog class inherits from Animal
class Dog(Animal):
    def move(self):
        print("Running 🐕")

# Bird class inherits from Animal
class Bird(Animal):
    def move(self):
        print("Flying 🦅")

# Example usage
car = Car()
bike = Bike()
dog = Dog()
bird = Bird()

# Calling the move method on different objects.
car.move()  # Output: Driving 🚗
bike.move()  # Output: Pedaling 🚲
dog.move()  # Output: Running 🐕
bird.move()  # Output: Flying 🦅
