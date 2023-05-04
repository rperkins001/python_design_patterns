"""Factory Method (Creational Pattern):
The Factory Method pattern defines an interface for creating 
objects in a superclass but allows subclasses to decide which 
class to instantiate. 

This pattern is useful when you want to delegate the responsibility 
of object creation to a separate method or class, based on certain 
criteria or input."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

factory = AnimalFactory()
dog = factory.create_animal("Dog")
print(dog.speak())  # Output: Woof!


"""In the example provided, the Animal class is an abstract 
base class with an abstract speak method. The Dog and Cat classes 
are concrete implementations of the Animal class. 

The AnimalFactory class has a create_animal method that takes an 
animal type string as input and returns a new instance of the 
corresponding animal class."""