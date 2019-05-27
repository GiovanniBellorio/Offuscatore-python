#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
from random import SystemRandom

g = [36,58,1,46,23,5,16,65,2,41,2,7,1,37,0,11,16,2,21,16]

'''
name = "Kevin"
somma = 0



for i in range(0,10):
	somma += i

if(i < 20):
	c = 3
	#i += c

print(name, somma)'''

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, a_name, a_salary):
        self.name = a_name
        self.salary = a_salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp1.displayEmployee()

