#Topic
#elif
#nested if..else
#function
#oop
#constructor
#import library example(calender)


# #1.elif
# #...if you have more than 2 options
#
# num=-9
# if(num>0):
#     print("Number is positive")
# elif(num<0):
#     print("Number is negative")
# else:
#     print("Number is zero")
#

#
# #nested else if:
# #..if ..else statement inside another if...else condition
#
# num=float(input("Enter a number:"))
# if num >= 0:
#     if num == 0:
#         print("ZERO")
#     else:
#         print("positive")
# else:
#     print("Negative")
#

#3.function:
#a block of code which runs after being called.
#def fun_name(parameter)
#def abc(username,password)

#
# def abc(name):
#     print("Hello",name)
# abc("Surakshya")
# abc("87654")
# abc("keshari")
# abc("saroj")
# abc("proush")
# abc("rupak")
#


# def add(num1, num2):
#     return (num1 + num2)
# print(add(2,6))
#
# print(add(2,7))




#build in function :
#print(), input(), range()

#variables: used to store the value
#
# x =10
# def fun():
#     x=5
#     print("value of x inside the function:",x)
# fun()
# print("Value of x outside the function:",x)


#6.oop

#oop-->object oriented programming language.
#class
#collection of data and function sets;
#object is the instance of a class.


# class myclass:
#     a=100
#     def fun1(self):
#         print("Hello")
# obj=myclass()
# print(obj.a)
# obj.fun1()
#
# class calculator:
#     def add(self,num1,num2):
#         return num1 +num2
#     def mul(self,nu1,num2):
#         return nu1 *num2
# cal1=calculator()
# print(cal1.add(2,5))
#
# print(cal1.mul(2,5))

#constructor:
#it is a class function with double underscore
#__init__(), functions is being called when object is created.

class Employee:

    def __init__(self, name, id):
        self.name =name
        self.id =id

    def print_emp_details(self):
        print("Employee Name:",self.name)
        print("Employee Id:",self.id)

emp1=Employee("SAROJ",5)
emp2=Employee("Nikita",8)
emp3=Employee("Sapana",1)
emp4=Employee("Surakshya",2)
emp1.print_emp_details()
emp2.print_emp_details()
emp3.print_emp_details()
emp4.print_emp_details()


#import calender

import  calendar
yy=2024
mm=7
dd=8
print(calendar.month(yy,mm,dd))