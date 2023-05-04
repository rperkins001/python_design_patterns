
"""Command (Behavioral Pattern):
The Command pattern encapsulates a request as an object, allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations."""

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Receiver:
    def action(self):
        return "Receiver: Executing the action"

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        return self.receiver.action()

class Invoker:
    def __init__(self, command):
        self.command = command

    def call(self):
        return self.command.execute()

receiver = Receiver()
command = ConcreteCommand(receiver)
invoker = Invoker(command)
print(invoker.call())  # Output: Receiver: Executing the action


"""Explanation:
In this example, the Command class is an abstract base class with an abstract execute method. The Receiver class has an action method that returns a string. The ConcreteCommand class is a concrete implementation of the Command class, which takes an instance of Receiver and overrides the execute method to call the action method of Receiver. The Invoker class takes a Command object and has a call method that triggers the execute method of the command."""