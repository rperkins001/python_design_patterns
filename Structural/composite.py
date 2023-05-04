"""Definition: The Composite pattern allows you to compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly. This pattern is useful when you want to represent a hierarchy of objects that have a common interface, and you want to treat them uniformly, regardless of whether they are individual objects or groups of objects."""

from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def __init__(self, value):
        self._value = value

    def operation(self):
        return self._value

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, child):
        self._children.append(child)

    def remove(self, child):
        self._children.remove(child)

    def operation(self):
        results = [child.operation() for child in self._children]
        return f"Composite({', '.join(results)})"

leaf1 = Leaf("1")
leaf2 = Leaf("2")
leaf3 = Leaf("3")

composite1 = Composite()
composite1.add(leaf1)
composite1.add(leaf2)

composite2 = Composite()
composite2.add(composite1)
composite2.add(leaf3)

print(leaf1.operation())        # Output: 1
print(composite1.operation())   # Output: Composite(1, 2)
print(composite2.operation())   # Output: Composite(Composite(1, 2), 3)

"""Explanation: In this example, we define an abstract base class Component with an abstract method operation. The Leaf class inherits from the Component class and implements the operation method to return its value.

The Composite class also inherits from the Component class and implements the operation method. It maintains a list of child components, and its operation method calls the operation method on each child component and combines their results. The Composite class also has add and remove methods to manage its child components.

We create instances of Leaf and Composite classes and build a tree structure by adding child components to composite components. When we call the operation method on the leaf and composite instances, they return their values or the combined results of their child components, respectively."""
