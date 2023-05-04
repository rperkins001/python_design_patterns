"""The Memento pattern is used to capture and externalize an object's internal state without violating encapsulation so that the object can be restored to this state later. This pattern is useful when you need to implement undo and redo functionality or take snapshots of the state of an object at different points in time."""

import copy

class Memento:
    def __init__(self, state):
        self._state = copy.deepcopy(state)

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def save_state_to_memento(self):
        return Memento(self._state)

    def restore_state_from_memento(self, memento):
        self._state = memento.get_state()

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

originator = Originator("State1")
caretaker = Caretaker()

caretaker.add_memento(originator.save_state_to_memento())

originator.set_state("State2")
caretaker.add_memento(originator.save_state_to_memento())

originator.set_state("State3")

print(f"Current State: {originator._state}")  # Output: Current State: State3

originator.restore_state_from_memento(caretaker.get_memento(1))
print(f"Restored State: {originator._state}")  # Output: Restored State: State2

originator.restore_state_from_memento(caretaker.get_memento(0))
print(f"Restored State: {originator._state}")  # Output: Restored State: State1


"""Explanation: In this example, we have three classes: Memento, Originator, and Caretaker. The Memento class is responsible for holding the state of the Originator object. The Originator class has a method save_state_to_memento that creates a Memento object with the current state, and a method restore_state_from_memento that sets the state of the Originator object to the state stored in a given Memento object.

The Caretaker class is responsible for managing the mementos. It has methods add_memento and get_memento to add and retrieve mementos, respectively.

In this example, we create an Originator object with an initial state, then create a Caretaker object to manage the mementos. We save the state of the Originator object to mementos and add them to the Caretaker. Then, we change the state of the Originator object and restore it to previous states using the mementos stored in the Caretaker."""