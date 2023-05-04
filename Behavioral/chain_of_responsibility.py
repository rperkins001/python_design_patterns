from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, request):
        pass

class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if 0 < request <= 10:
            print(f"ConcreteHandler1 handled request {request}")
        elif self._next_handler is not None:
            self._next_handler.handle_request(request)

class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if 10 < request <= 20:
            print(f"ConcreteHandler2 handled request {request}")
        elif self._next_handler is not None:
            self._next_handler.handle_request(request)

class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if 20 < request <= 30:
            print(f"ConcreteHandler3 handled request {request}")
        elif self._next_handler is not None:
            self._next_handler.handle_request(request)

handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2()
handler3 = ConcreteHandler3()

handler1.set_next(handler2).set_next(handler3)

requests = [5, 15, 25, 35]

for request in requests:
    handler1.handle_request(request)
    
    
"""Explanation: In this example, the Handler class is an abstract base class with an abstract method handle_request. The ConcreteHandler1, ConcreteHandler2, and ConcreteHandler3 classes implement the handle_request method to handle requests within specific ranges. If a handler cannot handle a request, it passes the request to the next handler in the chain. The set_next method of the Handler class sets the next handler in the chain. The example iterates through a list of requests and passes each request to the first handler in the chain, which then handles the request or passes it along the chain."""