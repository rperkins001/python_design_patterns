"""Definition: The Flyweight pattern uses sharing to support a large number of fine-grained objects efficiently. This pattern is useful when you have a large number of objects with a shared state, and you want to minimize the memory usage by reusing the shared state among these objects."""

import weakref

class Flyweight:
    _pool = weakref.WeakValueDictionary()

    def __new__(cls, state):
        obj = cls._pool.get(state)
        if obj is None:
            obj = super().__new__(cls)
            cls._pool[state] = obj
        return obj

    def __init__(self, state):
        self._state = state

    def operation(self, unique_state):
        return f"Flyweight with shared state {self._state} and unique state {unique_state}"

def client_code(flyweight_factory):
    flyweight1 = Flyweight("shared_state1")
    flyweight2 = Flyweight("shared_state1")
    flyweight3 = Flyweight("shared_state2")

    print(flyweight1 is flyweight2)  # Output: True
    print(flyweight1 is flyweight3)  # Output: False

    print(flyweight1.operation("unique_state1"))  # Output: Flyweight with shared state shared_state1 and unique state unique_state1
    print(flyweight2.operation("unique_state2"))  # Output: Flyweight with shared state shared_state1 and unique state unique_state2
    print(flyweight3.operation("unique_state3"))  # Output: Flyweight with shared state shared_state2 and unique state unique_state3

client_code(Flyweight)

"""Explanation: In this example, the Flyweight class uses a weak value dictionary _pool to store instances of the class based on their shared state. The __new__ method checks if there is already an instance with the given shared state in the pool; if not, it creates a new instance and stores it in the pool.

The operation method demonstrates the usage of shared and unique state in the flyweight objects. The shared state is part of the flyweight object, while the unique state is passed to the operation method.

In the client_code function, we create three flyweight instances with shared states "shared_state1" and "shared_state2". The first two instances have the same shared state, so they are actually the same object, as shown by the is operator. We call the operation method on the flyweight instances, passing different unique states."""

