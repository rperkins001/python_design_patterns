"""Definition: The Mediator pattern defines an object that encapsulates how a set of objects interact. This pattern promotes loose coupling by keeping objects from referring to each other explicitly, allowing you to vary their interaction independently. Mediator simplifies the communication between objects, centralizing the interaction in one place."""

from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def send(self, message, colleague):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self.colleague1 = None
        self.colleague2 = None

    def send(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.notify(message)
        else:
            self.colleague1.notify(message)

class Colleague(ABC):
    def __init__(self, mediator):
        self.mediator = mediator

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def notify(self, message):
        pass

class ConcreteColleague1(Colleague):
    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print(f"Colleague1 receives message: {message}")

class ConcreteColleague2(Colleague):
    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print(f"Colleague2 receives message: {message}")

mediator = ConcreteMediator()
colleague1 = ConcreteColleague1(mediator)
colleague2 = ConcreteColleague2(mediator)

mediator.colleague1 = colleague1
mediator.colleague2 = colleague2

colleague1.send("Hello from Colleague1")
colleague2.send("Hello from Colleague2")

# Output:
# Colleague2 receives message: Hello from Colleague1
# Colleague1 receives message: Hello from Colleague2


"""Explanation: In this example, we define an abstract base class Mediator with an abstract method send. The ConcreteMediator class implements this method to mediate communication between two colleagues. The send method takes a message and a colleague as parameters, and it notifies the other colleague with the message.

The Colleague class is an abstract base class with abstract methods send and notify. The ConcreteColleague1 and ConcreteColleague2 classes implement these methods. The send method sends a message through the mediator, and the notify method handles receiving a message.

We create a ConcreteMediator object, two ConcreteColleague objects, and associate the colleagues with the mediator. Then, we use the colleagues to send messages through the mediator, which notifies the other colleague with the message."""