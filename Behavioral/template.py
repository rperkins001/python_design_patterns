"""ChatGPT

Definition: The Template pattern defines the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure. This pattern is useful when you have multiple algorithms that share some common steps, and you want to avoid code duplication."""


from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.operation1()
        self.operation2()
        self.operation3()

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def operation3(self):
        print("Operation 3 in AbstractClass")

class ConcreteClassA(AbstractClass):
    def operation1(self):
        print("Operation 1 in ConcreteClassA")

    def operation2(self):
        print("Operation 2 in ConcreteClassA")

class ConcreteClassB(AbstractClass):
    def operation1(self):
        print("Operation 1 in ConcreteClassB")

    def operation2(self):
        print("Operation 2 in ConcreteClassB")

concrete_class_a = ConcreteClassA()
concrete_class_a.template_method()

print()

concrete_class_b = ConcreteClassB()
concrete_class_b.template_method()


"""Output:

Operation 1 in ConcreteClassA
Operation 2 in ConcreteClassA
Operation 3 in AbstractClass

Operation 1 in ConcreteClassB
Operation 2 in ConcreteClassB
Operation 3 in AbstractClass"""

"""Explanation: In this example, we define an abstract base class AbstractClass with a template_method that calls three operations: operation1, operation2, and operation3. The operation1 and operation2 methods are abstract, while the operation3 method has a default implementation.

The ConcreteClassA and ConcreteClassB classes inherit from AbstractClass and implement the abstract methods operation1 and operation2 to define their specific behavior for these operations.

We create instances of ConcreteClassA and ConcreteClassB and call the template_method on them. The template_method executes the sequence of operations, and the behavior of operation1 and operation2 depends on the concrete class, while operation3 has the same behavior for all concrete classes."""