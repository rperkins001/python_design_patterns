"""Strategy (Behavioral Pattern):
The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern is useful when you want to select an algorithm at runtime."""


from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute_algorithm(self, a, b):
        pass

class ConcreteStrategyA(Strategy):
    def execute_algorithm(self, a, b):
        return a + b

class ConcreteStrategyB(Strategy):
    def execute_algorithm(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute_algorithm(a, b)

strategy_addition = ConcreteStrategyA()
strategy_subtraction = ConcreteStrategyB()
context = Context(strategy_addition)

result1 = context.execute_strategy(3, 2)
print(result1)  # Output: 5

context.set_strategy(strategy_subtraction)
result2 = context.execute_strategy(3, 2)
print(result2)  # Output: 1


"""Explanation: In this example, the Strategy class is an abstract base class with an abstract execute_algorithm method. The ConcreteStrategyA and ConcreteStrategyB classes implement the execute_algorithm method, performing addition and subtraction, respectively. The Context class has a reference to a Strategy object and provides a method execute_strategy that calls the execute_algorithm method on the strategy object. The context can change the strategy at runtime using the set_strategy method."""