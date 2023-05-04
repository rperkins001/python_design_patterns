"""Singleton (Creational Pattern):
The Singleton pattern ensures that a class has only 
one instance and provides a global point of access 
to that instance. This pattern is useful when you 
want to control access to shared resources, such as 
a database connection or a configuration object."""


class Singleton:
    _instance = None

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

singleton1 = Singleton.instance()
singleton2 = Singleton.instance()
print(singleton1 is singleton2)  # Output: True


"""In the example provided, the Singleton class has 
a private class-level variable _instance that holds 
the single instance of the class. The instance method 
is a class method that checks if the _instance variable 
is None. 

If it is None, it means that the class hasn't 
been instantiated yet, so a new instance is created and 
assigned to _instance. If _instance is not None, the 
method returns the existing instance. This ensures that 
there is only one instance of the Singleton class."""