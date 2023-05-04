"""Definition: The Visitor pattern represents an operation to be performed on the elements of an object structure without changing the classes on which it operates. This pattern allows you to define a new operation without changing the classes of the elements on which it works. It is useful when you want to perform various operations on a set of objects with different interfaces but don't want to modify the object classes."""


from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

    def operation_a(self):
        return "Operation A in ConcreteElementA"

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

    def operation_b(self):
        return "Operation B in ConcreteElementB"

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"ConcreteVisitor1: {element.operation_a()}")

    def visit_concrete_element_b(self, element):
        print(f"ConcreteVisitor1: {element.operation_b()}")

class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"ConcreteVisitor2: {element.operation_a()}")

    def visit_concrete_element_b(self, element):
        print(f"ConcreteVisitor2: {element.operation_b()}")

element_a = ConcreteElementA()
element_b = ConcreteElementB()

visitor1 = ConcreteVisitor1()
visitor2 = ConcreteVisitor2()

element_a.accept(visitor1)  # Output: ConcreteVisitor1: Operation A in ConcreteElementA
element_a.accept(visitor2)  # Output: ConcreteVisitor2: Operation A in ConcreteElementA

element_b.accept(visitor1)  # Output: ConcreteVisitor1: Operation B in ConcreteElementB
element_b.accept(visitor2)  # Output: ConcreteVisitor2: Operation B in ConcreteElementB


"""Explanation: In this example, we define an abstract base class Element with an abstract method accept. The ConcreteElementA and ConcreteElementB classes implement this method to accept a visitor and perform an operation depending on the visitor.

The Visitor class is an abstract base class with abstract methods visit_concrete_element_a and visit_concrete_element_b. The ConcreteVisitor1 and ConcreteVisitor2 classes implement these methods to define the behavior when visiting concrete elements.

We create instances of ConcreteElementA, ConcreteElementB, ConcreteVisitor1, and ConcreteVisitor2. We use the accept method of the concrete elements to apply the visitors to them, and the visitors call the appropriate operation on the elements."""