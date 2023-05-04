"""Builder (Creational Pattern):
The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations. This pattern is useful when you want to create objects with many parts, and their construction order might vary."""


from abc import ABC, abstractmethod

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()

class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("PartA1")

    def build_part_b(self):
        self.product.add("PartB1")

class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("PartA2")

    def build_part_b(self):
        self.product.add("PartB2")

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def display(self):
        print("Product parts:", " ".join(self.parts))

director = Director()
builder1 = ConcreteBuilder1()
builder2 = ConcreteBuilder2()

director.set_builder(builder1)
director.construct()
product1 = builder1.product
product1.display()  # Output: Product parts: PartA1 PartB1

director.set_builder(builder2)
director.construct()
product2 = builder2.product
product2.display()  # Output: Product parts: PartA2 PartB2

"""Explanation: The Director class constructs the Product using the Builder interface. The Builder class is an abstract base class with abstract methods build_part_a and build_part_b. The ConcreteBuilder1 and ConcreteBuilder2 classes implement these methods to create and assemble parts of the product. The Product class stores the parts and has a display method to show the parts."""



