"""The State pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class. This pattern is useful when an object's behavior depends on its state, and it must change its behavior at runtime depending on that state."""


from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        print("Current State: A")
        context.set_state(ConcreteStateB())

class ConcreteStateB(State):
    def handle(self, context):
        print("Current State: B")
        context.set_state(ConcreteStateA())

class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle(self)

context = Context(ConcreteStateA())

for _ in range(5):
    context.request()
    
    
"""Output:

Current State: A
Current State: B
Current State: A
Current State: B
Current State: A
"""

"""Explanation: In this example, we define an abstract base class State with an abstract method handle. The ConcreteStateA and ConcreteStateB classes implement this method to define the behavior when the object is in state A or state B, respectively.

The Context class has a method set_state to set the current state, and a method request to call the handle method of the current state. The handle method of the concrete state classes also changes the state of the context to the next state.

We create a Context object with an initial state (ConcreteStateA). Then, we call the request method on the context multiple times, and the context changes its state and behavior accordingly."""