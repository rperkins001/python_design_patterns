"""Prototype (Creational Pattern):
The Prototype pattern specifies the kinds of objects to create using a prototypical instance and creates new objects by copying this prototype. This pattern is useful when object creation is expensive, and you want to avoid the cost of creating new objects from scratch."""

import copy

class Prototype:
    def __init__(self):
        self.objects = {}

    def register(self, name, obj):
        self.objects[name] = obj

    def unregister(self, name):
        del self.objects[name]

    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self.objects[name])
        obj.__dict__.update(kwargs)
        return obj

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.color} {self.make} {self.model}"

prototype = Prototype()
car1 = Car("Toyota", "Corolla", "Blue")
car2 = Car("Honda", "Civic", "Red")

prototype.register("Toyota", car1)
prototype.register("Honda", car2)

car3 = prototype.clone("Toyota", color="Green")
car4 = prototype.clone("Honda", color="Yellow")

print(car1)  # Output: Blue Toyota Corolla
print(car2)  # Output: Red Honda Civic
print(car3)  # Output: Green Toyota Corolla
print(car4)  # Output: Yellow Honda Civic

"""Explanation: In this example, the Prototype class maintains a registry of named prototype objects. The register and unregister methods add and remove prototypes from the registry, respectively. The clone method creates a new object by deep copying a prototype from the registry and updating its attributes with the provided keyword arguments. The Car class represents a sample object that can be cloned using the prototype pattern. In this case, new Car objects are created by cloning existing prototypes and modifying their color."""