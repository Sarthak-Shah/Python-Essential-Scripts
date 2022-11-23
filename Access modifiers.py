"""
Public members (generally methods declared in a class) are accessible from outside the class.
The object of the same class is required to invoke a public method. This arrangement of private instance variables and
public methods ensures the principle of data encapsulation.

Protected Members:
Protected members of a class are accessible from within the class and are also available to its sub-classes.
No other environment is permitted access to it. This enables specific resources of the parent class to be inherited by
the child class.

Private Members:
Python doesn't have any mechanism that effectively restricts access to any instance variable or method.
Python prescribes a convention of prefixing the name of the variable/method with a single or double underscore to
emulate the behavior of protected and private access specifiers.

The double underscore __ prefixed to a variable makes it private. It gives a strong suggestion not to touch it from
outside the class. Any attempt to do so will result in an AttributeError:

Accessor and Mutator Methods
Typically, all of a class’s data attributes are private and provide methods to access and change them
Accessor methods: return a value from a class’s attribute without changing it
Safe way for code outside the class to retrieve the value of attributes
Mutator methods: store or change the value of a data attribute
"""


class Super:
    def __init__(self, public1, protected2, private3):
        self.public1 = public1
        self._protected2 = protected2
        self.__private3 = private3

    # public method
    def show_public_var(self):
        print("this is public variable from public method ==>> ", self.public1)

    # protected method
    def _show_protected_var(self):
        print("this is protected variable from protected method ==>> ", self._protected2)

    # private method
    def __show_private_var(self):
        print("this is private method variable from private method ==>> ", self.__private3)

    # method to access private method from outside
    def access_private_method(self):
        self.__show_private_var()


# Let's use derived class to access protected variable and method.
class Sub(Super):
    def __init__(self, public1, protected2, private3):
        Super.__init__(self, public1, protected2, private3)

    # method to access protected method of Super class
    def access_protected_method(self):
        self._show_protected_var()

# creating object from derived class
obj = Sub("surya", "kumar", "yadav")


# calling public member functions of the class
obj.show_public_var()
obj.access_protected_method()
obj.access_private_method()

# Object can access protected member
print("Object is accessing protected member:", obj._protected2)
print("*"*50,"\n")
# let's try to access private method. But this is not recomonded !
# obj.__show_private_var() --> this will now work as private method will be tagged with _classname of parent
obj._Super__show_private_var()
print("Direct access of private variable ==> ", obj._Super__private3) # smae applies for private variables.
