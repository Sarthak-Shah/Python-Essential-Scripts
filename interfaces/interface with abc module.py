from abc import ABC, abstractmethod
from typing import Protocol

"""
I used a standard Python library abc to define interfaces for the last 10 years of my career. But recently, I found that
relatively new Python Protocols are way nicer. People find uses for both technologies. But I want to convince you to 
completely jump ships and start using them instead of more traditional techniques.
"""

"""
At a high level, an interface acts as a blueprint for designing classes. Like classes, interfaces define methods. Unlike
classes, these methods are abstract. An abstract method is one that the interface simply defines. It doesn’t implement
 the methods. This is done by classes, which then implement the interface and give concrete meaning to the interface’s
abstract methods.

Python’s approach to interface design is somewhat different when compared to languages like Java, Go, and C++. These 
languages all have an interface keyword, while Python does not. Python further deviates from other languages in one 
other aspect. It doesn’t require the class that’s implementing the interface to define all of the interface’s abstract 
methods.
"""

"""
Python is somewhat different from other popular languages since there are no interfaces on a language level. 
But there are several library implementations. The abc package is probably the most popular:
"""


class Animal(ABC):

    @abstractmethod
    def eat(self, food) -> str:
        pass

    @abstractmethod
    def sleep(self, hours) -> float:
        pass


"""
A protocol is a formalization of Python’s “duck-typing” ideology. There are many great articles on structural typing 
in Python (for example, see this tutorial). Protocols and interfaces are different beasts in theory, but a protocol 
does the job. I had great success replacing abc with Protocols without any downsides.
"""


class NewAnimal(Protocol):
    def eat(self, food) -> float:
        pass

    def sleep(self, hours) -> float:
        pass


"""

"""
# https://levelup.gitconnected.com/python-interfaces-choose-protocols-over-abc-3982e112342e