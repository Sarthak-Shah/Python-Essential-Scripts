"""
Serialize Python Objects With Pickle

Program:
input --->>      process --->>>      output
Ways of inputs:
    1) User (GUI/CONSOLE)
    2) Files (text, binary) [why csv still in use despite of having excel]

    Files ===> data file (binary) pickling
    # storages of data binary let you store the content of the RAM ---> object oriented database
    Text file which is string base let you store the content yet in form of strings.
    # since the input and output of any program is in form of string.

    --------------------------------------Data Science------------------------------
    # python is really great for manipulating , generating , analyzing and visualizing data

    # Xls and CSV files
    # what is the benefit of using CSV file over XLs?

    # CSV ----> this is a text file
    2,2,2

    - for xls you need a library. It's great to automate things property (part of automation)
    - CSV is text file, where xls is binary file.
    - Comparing CSV vs Xlsx, CSV files are faster and also consume less memory, whereas Excel consumes more memory while
    importing data. Comparing CSV vs Excel, CSV files can be opened with any text editor in windows, while Excel files
    can't be opened with text editors

    3) Database (sqlite, Mysql) --> serialization & deserialization (object to binary(byte stream) to object)

[Pickle in Python is primarily used in serializing and deserializing a Python object structure.
In other words, it's the process of converting a Python object into a byte stream to store it in a file/database,
maintain program state across sessions, or transport data over the network.]

object-oriented database (best for small businesses to avoid ERD/Normalization n all.)
(RAM based. need serialization)  vs DBMS (cost too much)

rb, wb is not possible without pickeling, as byte data can't be processed with strip () ! 
so pickeling used for that serialization deserialization .
"""

"""
Why it's required ?

when we want to store primitive datatypes after program execution, it's simple and easy to do it with 
normal file writing in text mode. 

But when you want to store dictionary, object, class, method into external space or need to share on network, it's
cumbersome with normal text based read/write, so in that scenario serialization de-serialization used to store python 
objects from RAM to external space or send it via network.
"""

astring = "this is going to be stored in text file !"
anumber = 19091994
abool = True

# to store this in file,
with open('primitiveDataStorage.txt', 'w') as fd:
    fd.write(astring + "\n")
    fd.write(str(anumber) + "\n")  # here typecasting requried as i/p o/p processed with string format only !
    fd.write(str(abool) + "\n")

# same it's simple to read that file also !

"""
Now imagine you need to store dictionary or class object or dataframe of pandas which has properties and methods ?
So some provision required to store those type of non primitive data in binary externally or send it via network. 
Here pickling comes to rescue by providing object serialization and de-serialization. !
"""


class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return self.name + " has weight of " + str(self.weight)

    def get_older(self):
        self.age += 1


p = Person("Sarthak", 28, 96)
# print(p)

"""
Now what if you want to store this object in file externally from RAM ?
"""
import pickle

# it's not necessary to store binary file with .pickle extension

with open("PythonObjectSerialization.pickle", "wb") as f:
    pickle.dump(p, f)

with open("PythonObjectSerialization.pickle", "rb") as f:
    readBinary = pickle.load(f)

print("Now reading binary file after opening it with pickle load.. ")
print(readBinary)
readBinary.get_older()
print(readBinary.age)
