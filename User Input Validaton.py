#!/usr/bin/env python
# coding: utf-8
__author__ = "Sarthak Shah"
__version__ = "1.0.1"
__maintainer__ = "Sarthak Shah"
__email__ = "er.sarthak@outlook.com"
__status__ = "Production"

"""
General Requirements:
Create a python application that inputs, processes, and stores student data using menu-driven programming
"""

import os
import re


def add_new_student():
    """
    Fetching file name and student data first and saving it to new file if not available or appending 
    the data into existing file named by user. 
    """
    filename = "StudentData"
    final_data = ""
    while True:
        try:
            filename = input("Enter File Name to store student data into it ==>> ")
            while True:
                StudentID = input("Enter Student ID ==>> ")
                if StudentID.isalnum():
                    break
                print("This seems Invalid ID ! Please Enter Valid ID !")
            while True:
                FirstName = input("Enter Student FirstName ==>> ")
                LastName = input("Enter Student LastName ==>> ")
                if FirstName.isalpha() and LastName.isalpha():
                    break
                print("This seems Invalid Name ! Please Enter Valid Name !")
            while True:
                Major = input("Enter Major ==>> ")
                if Major.isalnum():
                    break
                print("Please Enter Valid Major Name !")

            allowed_nondigits = ("-", "+", " ")
            while True:
                Phone = input("Enter Student Contact Number ==>> ")
                non_digits = re.findall('\D', Phone)
                for i in non_digits:
                    if i not in allowed_nondigits:
                        print("Please Enter Valid Phone Number !")
                        continue
                break
            while True:
                try:
                    GPA = float(input("Enter Student's overall GPA ==>> "))
                except ValueError:
                    print("It seems Invalid GPA, Please Enter Valid Value!")
                else:
                    GPA = str(GPA)
                    break
            while True:
                DOB = input("Enter Student's date of birth in below format. \nEx. October 15th, 1970 ==>> ")
                check_DOB = DOB.replace(" ", "")
                if re.findall('\w', check_DOB):
                    break
        except Exception as e:
            print("Please enter data properly ! ", e)
            continue
        else:
            final_data = " ".join([StudentID, FirstName, LastName, Major, Phone, GPA, DOB])
            break

    #     print("Printing list containing inputed data ", this_student_data)
    try:
        filename_with_extension = filename + ".txt"
        final_file_path = os.path.join(default_dir, filename_with_extension)
        if os.path.exists(final_file_path):
            with open(final_file_path, mode="a") as file:
                file.write(final_data + "\n")
                print("\nSuper ! Your inputted student data saved into your required filename")
        else:
            with open(final_file_path, mode="w") as file:
                file.write(final_data + "\n")
                print("\nSuper ! Your inputted student data saved into your required filename")
    except Exception as e:
        print("Some issue occurred during saving your data ! Please insert filename properly !")


def show_student_data():
    get_id = input("Enter Student ID to get his/her data ==>> ")
    get_all_files = os.listdir(default_dir)
    for single_file in get_all_files:
        final_file_path = os.path.join(default_dir, single_file)
        try:
            with open(final_file_path, mode="r") as read_file:
                data = read_file.readlines()
                #                 print("printing readlines output as in data ==>> ", data)
                for line in data:
                    split_line = line.split(" ")
                    if split_line[0].lower() == get_id.lower():
                        print("\nMatching record from inserted ID is,\n", "\n*************************\n",
                              line, "*************************")
                        break
        except Exception as e:
            print("\nData not found with inserted ID! Please add some data first !\n")
            print(e)


def menu():
    print("\n###########################\nEnter number according to your requirement.\n")
    print("1 ---- Add new student data to database")
    print("2 ---- Show student data by ID")
    print("3 ---- Exit !\n###########################\n")
    return input("\nEnter your selection now ==>> ")


def main():
    global default_dir
    default_dir = "data-folder"
    if not os.path.exists(default_dir):
        os.mkdir(default_dir)
    while True:
        selection = menu()
        if selection == "1":
            add_new_student()
        elif selection == "2":
            show_student_data()
        elif selection == "3":
            print("\nThank You. Visit Again !")
            break
        else:
            print("\nPlease Enter Appropriate Value to process your request !")
            continue


if __name__ == "__main__":
    main()
