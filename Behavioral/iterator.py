"""The Iterator pattern provides a way to access the elements of an aggregate object (e.g., a collection) sequentially without exposing its underlying representation. This pattern is useful when you want to have a uniform way of traversing different types of collections, allowing you to change the data structure of the collection without affecting the traversal code."""


from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class ConcreteIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0

    def has_next(self):
        return self.position < len(self.items)

    def next(self):
        if self.has_next():
            item = self.items[self.position]
            self.position += 1
            return item
        else:
            return None

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.items = []

    def create_iterator(self):
        return ConcreteIterator(self.items)

    def add_item(self, item):
        self.items.append(item)

aggregate = ConcreteAggregate()
aggregate.add_item("Item 1")
aggregate.add_item("Item 2")
aggregate.add_item("Item 3")

iterator = aggregate.create_iterator()

while iterator.has_next():
    print(iterator.next())  # Output: Item 1, Item 2, Item 3
    
    
"""Explanation: In this example, we define an abstract base class Iterator with abstract methods has_next and next. The ConcreteIterator class implements these methods to traverse a list of items sequentially. The has_next method checks if there is a next element in the list, and the next method returns the next element if available.

The Aggregate class is an abstract base class with an abstract method create_iterator. The ConcreteAggregate class implements this method to create a ConcreteIterator for its items. The add_item method allows adding items to the aggregate.

We create a ConcreteAggregate object, add items to it, and then create an iterator for the aggregate. We use the iterator to traverse the items in the aggregate and print them."""
