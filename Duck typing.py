__author__ = "sarthak shah"
__maintainer__ = "sarthak shah"
__email__ = "er.sarthak@outlook.com"
__status__ = "Production"
__copyright__ = "Copyright 2023, Planet Earth"

"""
One thing -> multiple form is polymorphism.
Duck Typing - The way of doing Polymorhpism.
Python's dynamic typing makes it possible.

Duck typing in Python can be explained with the analogy of a duck in a zoo. Just like the zoo staff only cares about 
the duck's ability to swim and quack, rather than its specific breed or species, Python only cares about an object's 
ability to perform certain actions, rather than its specific type or class. As long as an object can swim (perform the 
necessary actions), it is considered a duck, regardless of its actual type or class.
"""


class Pycharm:
    def execute(self):
        print("This is execute() of Pycharm class.\ncompiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("This is execute() of MyEditor class.\nspell check")
        print("convention check")
        print("compiling")
        print("running")


class Laptop:
    def code(self, the_ide):
        the_ide.execute()


ide = Pycharm()
ide2 = MyEditor()

lap1 = Laptop()
lap1.code(ide)
print("\n----------------------------------------\n")
lap1.code(ide2)

"""
So, here we don't care about class type and its working, as far as it does have method named execute(), it's
good to go !! This is called duck typing. !
"""

"""
In this case, we call method len() gives the return value from __len__ method. Here __len__ method defines the property 
of the class Specialstring

The object’s type itself is not significant in this we do not declare the argument in method prototypes. This means that
 compilers can not do type-checking. Therefore, what really matters is if the object has particular attributes at run 
 time. Duck typing is hence implemented by dynamic languages. But now some of the static languages like Haskell also 
 supports it. But, Java/C# doesn’t have this ability yet.
"""


# Python program to demonstrate
# duck typing

"""
Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript, etc. 
where the type or the class of an object is less important than the method it defines. Using Duck Typing, we do not 
check types at all. Instead, we check for the presence of a given method or attribute.

The name Duck Typing comes from the phrase:
“If it looks like a duck and quacks like a duck, it’s a duck”
"""


class SpecialString:
    def __len__(self):
        return 21


# string = SpecialString()
# print(len(string))


class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Fish:
    def swim(self):
        print("fish swim in sea")


# Attributes having same name are
# considered as duck typing

# for obj in Bird(), Airplane(), Fish():
#     obj.fly()

"""
In this example, we can see a class supports some method we can modify it or give them new functionality. Duck-typing 
emphasis what the object can really do, rather than what the object is.
"""
