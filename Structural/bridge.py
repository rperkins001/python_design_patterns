"""Definition: The Bridge pattern decouples an abstraction from its implementation so that the two can vary independently. This pattern is useful when you have a hierarchy of classes that you want to extend in two orthogonal dimensions, such as abstraction and implementation."""

from abc import ABC, abstractmethod

class Abstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def operation(self):
        return f"Abstraction: {self._implementation.operation_implementation()}"

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB"

concrete_implementation_a = ConcreteImplementationA()
abstraction1 = Abstraction(concrete_implementation_a)
print(abstraction1.operation())  # Output: Abstraction: ConcreteImplementationA

concrete_implementation_b = ConcreteImplementationB()
abstraction2 = Abstraction(concrete_implementation_b)
print(abstraction2.operation())  # Output: Abstraction: ConcreteImplementationB

"""Explanation: In this example, we have an Abstraction class and an abstract base class Implementation. The Abstraction class has a reference to an object of a class that inherits from Implementation. The operation method of the Abstraction class calls the operation_implementation method of the Implementation object.

The ConcreteImplementationA and ConcreteImplementationB classes inherit from the Implementation abstract base class and implement the operation_implementation method to define their specific behavior.

We create instances of ConcreteImplementationA and ConcreteImplementationB, and instances of the Abstraction class that use these concrete implementations. When we call the operation method on the abstraction instances, they delegate the call to the concrete implementations. This way, the abstraction is decoupled from the implementation, and they can vary independently."""
