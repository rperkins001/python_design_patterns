"""Definition: The Proxy pattern provides a surrogate or placeholder for another object to control access to it. This pattern is useful when you need to add functionality to an object, such as access control or caching, without changing its implementation."""


from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def operation(self):
        pass

class RealSubject(Subject):
    def operation(self):
        return "RealSubject: Performing operation"

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def operation(self):
        if self.check_access():
            result = self._real_subject.operation()
            self.log_access()
            return result
        else:
            return "Proxy: Access denied"

    def check_access(self):
        print("Proxy: Checking access")
        return True

    def log_access(self):
        print("Proxy: Logging access")

real_subject = RealSubject()
proxy = Proxy(real_subject)

print(proxy.operation())


"""
Output:

Proxy: Checking access
Proxy: Logging access
RealSubject: Performing operation
"""

"""Explanation: In this example, we define an abstract base class Subject with an abstract method operation. The RealSubject class inherits from the Subject class and implements the operation method to perform an operation.

The Proxy class also inherits from the Subject class and implements the operation method. It has a reference to a RealSubject object, and its operation method checks access, calls the operation method on the real subject, and logs access. The check_access and log_access methods are examples of additional functionality provided by the proxy.

We create instances of RealSubject and Proxy, passing the real subject instance to the proxy. When we call the operation method on the proxy instance, it checks access, calls the operation method on the real subject, logs access, and returns the result."""