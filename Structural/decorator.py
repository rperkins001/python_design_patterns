"""Decorator (Structural Pattern):
The Decorator pattern attaches additional responsibilities to an object dynamically, without affecting the other objects. This pattern is useful when you want to extend the functionality of an object, but inheritance is not feasible or desired."""

from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

component = ConcreteComponent()
decorator = ConcreteDecoratorA(component)
print(decorator.operation())  # Output: ConcreteDecoratorA(ConcreteComponent)

"""In the example provided, the Component class is an abstract base class with an abstract operation method. The ConcreteComponent class is a concrete implementation of the Component class. The Decorator class is also a subclass of Component, but it has a reference to a Component object, which can be any concrete component or another decorator. The ConcreteDecoratorA class extends the Decorator class and overrides the operation method to add new behavior or modify the behavior of the wrapped component."""