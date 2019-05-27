#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
name = "Kevin"
somma = 0

for i in range(0,10):
    somma += i

if(i < 20):
    c = 3
    #i += c

print(name, somma)'''

i = 10
print(i)

class Employee:
    'Common base class for all employees'

    def __init__(self, a_name, a_salary):
        self.name = a_name
        self.salary = a_salary

    def displayCount(self):
        empCount = 0
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp1.displayEmployee()

