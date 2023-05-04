"""Observer (Behavioral Pattern):
The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. This pattern is useful when you want to establish a communication mechanism between objects that are loosely coupled."""

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class ConcreteSubject(Subject):
    def __init__(self, state):
        super().__init__()
        self._state = state

    def set_state(self, state):
        self._state = state
        self.notify()

    def get_state(self):
        return self._state

class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"Observer: Subject state changed to {subject.get_state()}")

subject = ConcreteSubject("initial")
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)
subject.set_state("updated")


"""In the example provided, the Subject class has methods to attach and detach observers, and a notify method to update all attached observers when the subject changes state. The ConcreteSubject class extends the Subject class and has a _state variable, along with setter and getter methods. The Observer class is an abstract base class with an abstract update method. The ConcreteObserver class implements the update method, which prints the new state when it is called."""