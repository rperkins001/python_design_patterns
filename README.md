# Design Patterns in Python

This repository contains an implementation of common design patterns in Python. The design patterns are organized into three categories: Behavioral, Creational, and Structural.

## File System Diagram

```plaintext
.
├── Behavioral
│   ├── chain_of_responsibility.py
│   ├── command.py
│   ├── interpreter.py
│   ├── iterator.py
│   ├── mediator.py
│   ├── memento.py
│   ├── observer.py
│   ├── state.py
│   ├── strategy.py
│   ├── template.py
│   └── visitor.py
├── Creational
│   ├── abstract.py
│   ├── builder.py
│   ├── factory.py
│   ├── prototype.py
│   └── singleton.py
└── Structural
    ├── adapter.py
    ├── bridge.py
    ├── composite.py
    ├── decorator.py
    ├── facade.py
    ├── flyweight.py
    └── proxy.py

Behavioral Design Patterns
Chain of Responsibility

The Chain of Responsibility pattern is used to achieve loose coupling in software design where a request from the client is passed to a chain of objects to process them.
Command

The Command pattern is used to encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
Interpreter

The Interpreter pattern is used to define a grammatical representation for a language and provides an interpreter to deal with this grammar.
Iterator

The Iterator pattern is used to provide a standard way to traverse through a group of objects.
Mediator

The Mediator pattern is used to define an object that encapsulates how a set of objects interact with each other.
Memento

The Memento pattern is used to capture and restore an object's internal state.
Observer

The Observer pattern is used to define a one-to-many dependency between objects where a state change in one object results in all its dependents being notified and updated automatically.
State

The State pattern is used to allow an object to alter its behavior when its internal state changes.
Strategy

The Strategy pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable.
Template Method

The Template Method pattern is used to define the skeleton of an algorithm in an operation, deferring some steps to subclasses.
Visitor

The Visitor pattern is used to define a new operation to a class without changing the class.
Creational Design Patterns
Abstract Factory

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.
Builder

The Builder pattern is used to separate the construction of a complex object from its representation, so that the same construction process can create different representations.
Factory Method

The Factory Method pattern is used to define an interface for creating objects, but let subclasses decide which classes to instantiate.
Prototype

The Prototype pattern is used to create new objects by copying an existing object.
Singleton

The Singleton pattern is used to ensure that a class has only one instance and provide a global point of access to it.
Structural Design Patterns
Adapter

The Adapter pattern is used to convert the interface of a class into another interface that clients expect.
Bridge

The Bridge pattern is used to decouple an abstraction from its implementation so that the two can vary independently.
Composite

The Composite pattern is used to treat a group of objects in the same way as a single object.
Decorator

The Decorator pattern is used to attach additional responsibilities to an object dynamically.
Facade

The Facade pattern is used to provide a simple interface to a complex system.

The Flyweight pattern is used to minimize memory usage and improve performance by sharing as much data as possible with other similar objects.
Proxy

The Proxy pattern is used to provide a surrogate or placeholder for another object to control access to it. This can be useful when you want to add additional behavior to an object without modifying its code directly.