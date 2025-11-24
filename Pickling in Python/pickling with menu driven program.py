___author__ = "sarthak shah"
"""
1.	Write a Python program that displays a menu with the following options: a. Add a student record b. View all student records c.
Search for a student record d. Update a student record e. Delete a student record f. Quit
2.	Implement the necessary functions for each option in the menu. For example, if the user selects "Add a student
record," the program should prompt the user to enter data and save it to a file.
3.	Use the appropriate exception handling to ensure that the program doesn't crash if the user enters invalid input or
if there's an error in the file operations.
"""

"""
2.	A brief write-up explaining the design choices you made and the challenges you faced while completing the assignment.
Answer: As demonstrated in class, I was well confifent in designing menu driven options and trigger related methods.
It was pretty straight forward to developer Student class and inherit it for UG and G Student classes.
But once I started applying pickling, I made few mistakes. I used to open file descriptor at each and every methods related 
to Student data manipulations. Then I felt it seems cumbersome and heavysome task for RAM. So I initiated 1 list containing 
all pickled items prefilled, so it was cakewalk for me to apply manipulations on that list and at the time of exit I used
to dump it to overwrite existing picked file in ROM.

"""

import os
import pickle


class Student:
    def __init__(self, id:str, fname:str, lname:str, marks:list, street:str, city:str, postal:str, prov:str, con:str):
        self.student_id = id
        self.first_name = fname
        self.lname = lname
        self.marks = marks
        self.add = Address(street, city, postal, prov,con)

    def __str__(self):
        return f"Student with ID {self.student_id} Name: {self.first_name} {self.lname}\n lives at {self.add.street}, {self.add.city}"

    def average(self):
        return sum(self.marks)/len(self.marks)


class UndergradStudent(Student):
    def __init__(self, subject:str, entry_year:int, id:str, fname:str, lname:str, marks:list, street:str, city:str, postal:str, prov:str, con:str):
        Student.__init__(self, id, fname, lname, marks, street, city, postal, prov, con)
        self.subject = subject
        self.yearOfEntry = entry_year

    def graduate(self):
        return True if self.average() > 50 else False

    def __str__(self):
        return f"Student with ID {self.student_id} Name: {self.first_name} {self.lname}\nStart Year: {self.yearOfEntry} Main Subject: {self.subject} \nlives at {self.add.street}, {self.add.city}"


class GraduateStudent(Student):
    def __init__(self, thesis:str,  subject: str, entry_year: int, id:str, fname: str, lname: str, marks: list, street: str,
                 city: str, postal: str, prov: str, con: str):
        Student.__init__(self, id, fname, lname, marks, street, city, postal, prov, con)
        self.subject = subject
        self.yearOfEntry = entry_year
        self.thesis = thesis

    def graduate(self):
        return True if self.average() > 70 else False

    def __str__(self):
        return f"Student with ID {self.student_id} Name: {self.first_name} {self.lname}\nThesis topic: {self.thesis} Start Year: {self.yearOfEntry} Main Subject: {self.subject} \nlives at {self.add.street}, {self.add.city}"


class Address:
    def __init__(self, street:str, city:str, postal:str, prov:str, con:str):
        self.street = street
        self.city = city
        self.postalCode = postal
        self.province = prov
        self.con = con

    def __str__(self):
        return f"Student Address Info: {self.street}, {self.city} {self.postalCode}, {self.province}, {self.con}"


def menu():
    flag = True
    while flag:
        print("========== MENU ==============")
        print(
            "-----------------------------\nSelect your option and Enter accordingly in a to f,\na. Add a student record\nb. View all student "
            "records\nc. Search for a student record"
            "\nd. Update a student record\ne. Delete a student record\nf. Quit")
        user_input = input("\n==>> ")
        if user_input == "a":
            add_student()
        elif user_input == "b":
            view_all_students()
        elif user_input == "c":
            find_student()
        elif user_input == "d":
            update_student()
        elif user_input == "e":
            delete_student()
        elif user_input == "f":
            print("Thank you! See you soon !")
            with open("student_data.pickle", "wb") as fdscr:
                for new_data in pickled_object_loader:
                    pickle.dump(new_data, fdscr)
            break
        else:
            print("Try Again ! Please Enter Valid Input From Listed Options! ")


def add_student():
    print("Welcome to New Student Adding Section !")
    while True:
        type_of_student = input("Enter U for undergrad student and G for graduate student ! :: ")
        if type_of_student in ["U", "G", "u", "g"]:
            break
        else:
            print("Please enter U or G to proceed further !")
    while True:
        try:
            fname, lname = input("Enter student's first and last name separated by whitespace :: ").split(" ")
            break
        except:
            print("Please enter name properly ! ex, Sarthak Shah")

    while True:
        marks = input("Enter all marks separated by whitespace !").split(" ")
        try:
            proper_marks = [float(m) for m in marks]
            break
        except:
            print("Please enter marks properly !")

    street = input("Enter Street details :: ")
    city = input("Enter City details :: ")
    postalcode = input("Enter postalcode :: ")
    province = input("Enter province :: ")
    country = input("Enter Country :: ")

    subject = input("Enter Main Subject :: ")
    while True:
        try:
            entry_year = int(input("Enter year of Entry to College :: "))
            break
        except:
            print("Please enter valid year in numberical format. Ex, 2016")
    # id = input("Enter Student ID :: ")

    if len(pickled_object_loader) > 0:
        last_added_entry = pickled_object_loader[-1]
        last_id = int(last_added_entry.student_id)
        new_id = last_id + 1
        new_id = str(new_id)
    else:
        new_id = str(101000)
    student = None
    if type_of_student.lower() == "u":
        student = UndergradStudent(subject, entry_year, new_id, fname, lname, proper_marks, street, city, postalcode, province, country)
    elif type_of_student.lower() == "g":
        thesis = input("Please enter your thesis topic in brief ! :: ")
        student = GraduateStudent(thesis, subject, entry_year, new_id, fname, lname, proper_marks, street, city, postalcode, province, country)

    pickled_object_loader.append(student)


def view_all_students():
    if len(pickled_object_loader) > 0:
        for i in pickled_object_loader:
            print(i)
            print("----------------")
    else:
        print("Ooops! No data available to show ! \n")


def find_student():
    get_student_name = input("enter student's first name !")
    if len(pickled_object_loader) > 0:
        for data in pickled_object_loader:
            if data.first_name == get_student_name:
                print("data related to given name found: ")
                print(data)
                print("-----------------------")
    else:
        print("Ooops! No data available related to provided student name ! \n")


def update_student():
    get_id = input("Enter Student ID :: ")
    if len(pickled_object_loader) > 0:
        for data in pickled_object_loader:
            if data.student_id == get_id:
                print("Record found for requested student ID.. Now enter data again to update it !")
                pickled_object_loader.remove(data)
                add_student()
    else:
        print("Ooops! No data available related to provided student ID ! \n")


def delete_student():
    get_id = input("Enter Student ID to delete his/her data from record ! :: ")
    if len(pickled_object_loader) > 0:
        for data in pickled_object_loader:
            if str(data.student_id) == get_id:
                print("Record found for requested student ID.. Now deleteing data !")
                pickled_object_loader.remove(data)
    else:
        print("Ooops! No data available related to provided student ID ! \n")


if __name__ == "__main__":

    pickled_object_loader = []
    if os.path.exists("./student_data.pickle"):
        with open("./student_data.pickle", "rb") as fd:
            while True:
                try:
                    data = pickle.load(fd)
                    pickled_object_loader.append(data)
                except EOFError:
                    break
    menu()
