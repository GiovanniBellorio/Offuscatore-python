#!/usr/bin/python
# -*- coding: utf-8 -*-
name = "Kevin"
somma = 0

for i in range(0,10):
    somma += i

i = 111
if(i < 30):
    c = 3
    #i += c

print(name, somma)


if name == "Kevin":
    name = "ok"
    b = ["c","i","","","a","o"]
else:
    name = 10

print(name)
print(b)

b = [11,2,3,4,56,1,2,3,4]
print(b)

b = ["c","i","","","a","o"]
print(b)

b = [{"key":"value"},{"key1":"value1"}]
print(b)


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp1.displayEmployee()
