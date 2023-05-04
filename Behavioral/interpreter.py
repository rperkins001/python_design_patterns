"""The Interpreter pattern defines a representation for a grammar along with an interpreter to evaluate expressions defined in the grammar. This pattern is useful when you need to define a language to represent and manipulate complex structures, such as abstract syntax trees or parse trees."""

from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class TerminalExpression(Expression):
    def __init__(self, data):
        self.data = data

    def interpret(self, context):
        return self.data in context

class OrExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) or self.expr2.interpret(context)

class AndExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) and self.expr2.interpret(context)

def get_male_expression():
    robert = TerminalExpression("Robert")
    john = TerminalExpression("John")
    return OrExpression(robert, john)

def get_married_woman_expression():
    julie = TerminalExpression("Julie")
    married = TerminalExpression("Married")
    return AndExpression(julie, married)

male_expr = get_male_expression()
married_woman_expr = get_married_woman_expression()

context1 = "John"
context2 = "Married Julie"
context3 = "Lucy"

print(f"Is {context1} male? {male_expr.interpret(context1)}")  # Output: True
print(f"Is {context2} a married woman? {married_woman_expr.interpret(context2)}")  # Output: True
print(f"Is {context3} male? {male_expr.interpret(context3)}")  # Output: False

"""Explanation: In this example, we define an abstract base class Expression with an abstract method interpret. The TerminalExpression, OrExpression, and AndExpression classes implement the interpret method to evaluate simple expressions, logical OR expressions, and logical AND expressions, respectively.

The get_male_expression function creates an expression that checks if a given context contains either "Robert" or "John", and the get_married_woman_expression function creates an expression that checks if a given context contains both "Julie" and "Married".

We then create expressions male_expr and married_woman_expr using these functions and evaluate them using different contexts. The interpret method of the expressions evaluates the expressions based on the given context and returns the result."""