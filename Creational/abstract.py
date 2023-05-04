"""Abstract Factory (Creational Pattern):
The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. This pattern is useful when you want to create a set of objects that belong to different families but share a common theme."""

from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

class ProductA(ABC):
    @abstractmethod
    def product_method(self):
        pass

class ProductB(ABC):
    @abstractmethod
    def product_method(self):
        pass

class ConcreteProductA1(ProductA):
    def product_method(self):
        return "ConcreteProductA1"

class ConcreteProductB1(ProductB):
    def product_method(self):
        return "ConcreteProductB1"

class ConcreteProductA2(ProductA):
    def product_method(self):
        return "ConcreteProductA2"

class ConcreteProductB2(ProductB):
    def product_method(self):
        return "ConcreteProductB2"

factory1 = ConcreteFactory1()
product_a1 = factory1.create_product_a()
product_b1 = factory1.create_product_b()
print(product_a1.product_method())  # Output: ConcreteProductA1
print(product_b1.product_method())  # Output: ConcreteProductB1

factory2 = ConcreteFactory2()
product_a2 = factory2.create_product_a()
product_b2 = factory2.create_product_b()
print(product_a2.product_method())  # Output: ConcreteProductA2
print(product_b2.product_method())  # Output: ConcreteProductB2

"""Explanation: In this example, AbstractFactory is an abstract base class with abstract methods create_product_a and create_product_b. The ConcreteFactory1 and ConcreteFactory2 classes implement these methods to create objects of ConcreteProductA1, ConcreteProductB1, ConcreteProductA2, and ConcreteProductB2 classes, respectively. The ProductA and ProductB classes are abstract base classes with an abstract product_method, while the concrete product classes implement this method."""