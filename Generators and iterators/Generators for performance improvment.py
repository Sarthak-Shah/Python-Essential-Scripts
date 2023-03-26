#!/usr/bin/env python
# coding: utf-8
__author__ = "Sarthak Shah"
__version__ = "1.0.1"
__maintainer__ = "Sarthak Shah"
__email__ = "er.sarthak@outlook.com"
__status__ = "Production"

import time
import sys


def employee_default_info_saver(mylist:list):
    gathered_info = []
    for n, emp in enumerate(mylist):
        new_emp = {
            "id": "IU2022"+str(n),
            "name": emp,
            "sick_leave": 15,
            "casual_leave": 30,
            "base_salary": None
        }
        gathered_info.append(new_emp)
    return gathered_info


def employee_default_info_generator(mylist:list):
    for n, emp in enumerate(mylist):
        new_emp = {
            "id": "IU2022"+str(n),
            "name": emp,
            "sick_leave": 15,
            "casual_leave": 30,
            "base_salary": None
        }
        yield new_emp


testing_list = ["rohan", "darpan", "sarthak", "akshat", "akarshan", "ridha", "utsav", "heli"]*1000000

start = time.process_time()
result1 = employee_default_info_saver(testing_list)
end = time.process_time()
print("It took {} sec to complete this task !".format(end-start))
print("Total size occupied by result in bytes is ==>>, ", sys.getsizeof(result1))
print(type(result1))
print("\n##########################\n")

start = time.process_time()
result2 = employee_default_info_generator(testing_list)
end = time.process_time()
print("It took {} sec to complete this task !".format(end-start))
print("Total size occupied by result in bytes is ==>>, ", sys.getsizeof(result2))
print(type(result2))
print(next(result2))
print(next(result2))