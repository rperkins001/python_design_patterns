"""Definition: The Facade pattern provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use. This pattern is useful when you have a complex system with multiple subsystems and you want to provide a simplified interface to clients for ease of use."""

class Subsystem1:
    def operation1(self):
        return "Subsystem1: Operation 1"

    def operation2(self):
        return "Subsystem1: Operation 2"

class Subsystem2:
    def operation1(self):
        return "Subsystem2: Operation 1"

    def operation2(self):
        return "Subsystem2: Operation 2"

class Facade:
    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def simplified_operation(self):
        results = []
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem1.operation2())
        results.append(self._subsystem2.operation1())
        results.append(self._subsystem2.operation2())
        return "\n".join(results)

subsystem1 = Subsystem1()
subsystem2 = Subsystem2()

facade = Facade(subsystem1, subsystem2)

print(facade.simplified_operation())


"""
Output:

Subsystem1: Operation 1
Subsystem1: Operation 2
Subsystem2: Operation 1
Subsystem2: Operation 2
"""

"""Explanation: In this example, we have two subsystems, Subsystem1 and Subsystem2, each with their own operations. The Facade class provides a simplified interface by wrapping these subsystems and exposing a single simplified_operation method that internally calls the operations of the subsystems.

We create instances of Subsystem1, Subsystem2, and Facade, passing the subsystem instances to the facade. When we call the simplified_operation method on the facade instance, it calls the operations of the subsystems and returns the combined results. This way, the client can interact with the facade instead of dealing with the complexity of the subsystems directly."""