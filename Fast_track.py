# Python Fundamentals:

# Q.1) What is Python ?

# [ python is general purpose high level programming language,
# which is used in web-development, artificial intelligence and
# machine learning and for Data Analysis etc.python allows
# programming in object oriented as well as procedural oriented.
# python indentation concept make python more readable all the
# time.]

# Q.2) Who was the developer of python ?

#[ Python was developed by Guido Van Rossum in 1991]

# Q.3) How python code get execute ?

# [ Python Source Code written in .py file is first compiled
# to generate byte-code. This byte-code stored with extension
# .pyc in pycache folder, then this byte code executed by
# interpreter(p.v.m) to convert it into machine understandable
# code.]

# Q.4) Why we say Python is interpreted language ?

# [ Because compilation part is hidden from the programmer thus,
#  many programmers believe that it is an interpreted language.]

# Q.5)  What is PEP-8 in Python ?

# [ PEP-8 stands for python Enhancement proposal. The purpose
#  of PEP-8 is to improve readability & consistency of python
#  code.]

# Q.6) What is P.V.M ?

# [ So PVM is nothing but an interpreter that converts the byte
# code to machine code for given operating system. pvm is also
# called python interpreter.]

# Q.7) Where we can use python or what are the Application of
#      python ?

# * Artificial intelligence and machine learning.
# * web-development.
# * Data Analysis and data visualization.
# * Image processing.(open cv)
# * Game development.
# * Scientific Computing.

# Q.8) What are the imp Features of Python ?

# Simple and Easy to code:

# [ Python is very easy to code as compared to other programming
#  languages like Java and C++.Python code is quite like English.
#  Statements, you can easily tell what the code is supposed
#  to do.]

# Freeware and OpenSource:

# [ we are using python software without any licence, so it's
#   freeware.]
# [ python source code is open, so we can customize it based
#   on our requirement. ]

# Dynamically typed language:

# [ we are not required to declare type explicitly for variable
#   when-ever we are assigning any value, based on value,The type
#   will be considered automatically. and also dynamically type
#   nature provide more flexibility to the programmer. ]

# a=10
# a='vivek'

# Python both Object Oriented as well as Procedure Oriented.

# Python supports Extensive libraries and huge community.

# platform Independent:

# [ once we write a python program, it can run on any platform
#   without rewriting once again. ]

# python is interpreted language.

# Extensible:

# Identifiers:

# [ Identifiers are nothing but just a name in python for example
#   class name, variable name, function name, Module name. ]

# There are some rules that you have to know before declaring any
# identifiers.

# 1. Alphabetic symbol are allowed(either in upper or lower).
# 2. Digits allowed 0 to 9.
# 3. In special characters only underscore is allowed.
# 4. Must remember identifier should not be begin with digits.
# 5. You can assign any value to _ (underscore).
# 6. Identifier can be start or begin with underscore(_).
# 7. Identifiers are case-sensitive.
# 8. We cannot use reserve key words as an identifiers.
# 9. There is no length limit for python identifier.but not
#    recommended to use too lengthy identifier.
# 10. ($) symbol is not allow in python.

# Note:
# 1.[ if identifier start with double underscore (_) then
#     it indicates that is private.]
# 2.[ if identifier start with single underscore (_) then
#     it indicates that is protected.]
# 3.[ if identifier start and end with double underscore (_) then
#     it indicates that is a magic variable.]

# Q.8) what is reserve keyword ?

# usually, Reserve keyword represent some special meaning and
# functionality.

# To know how many reserve keywords are there:

# import keyword
# for x in keyword.kwlist:
#     print(x)

# all valid:

# int=20
# float=1.2
# str=45
# string=56
# print(int,float,str,string)

# Note: There is no need of switch statement in python,basically
#       you can go with dictionary concept and full fill your
#       demand.

# There is no do-while loop in python but we can create a program
# like this.

# i = 1
# while True:
#     print(i)
#     i = i + 1
#     if (i > 5):
#         break

# Data-Type:
# import random
# for x in range(1000):
#     print(random.randint(1,9),random.randint(1,9),random.randint(0,9),random.randint(0,9),sep=' ')

# Integer can be represent in four forms:

# Decimal
# Binary
# Octal
# Hexadecimal

# The Default form of this number 2e2 is Float only !
# ex:
# a=2e2
# print(a)

# set={10,20,30}
# print(type(set))


# x=0x22
# a=hex()
# print(a)

# Note: True means '1' and False means '0'.

# lst=[1,2,4,5]
# x=bytes(lst)
# x[0]=45
# print(x)// 'bytes' object does not support item assignment.

# lst=[0,256]
# x=bytearray(lst)
# for i in range(len(x)):
#     print(x[i])// error

# print(3**2)
# a=b=c=45
# print(a,b,c)

# print(not True)

# print(~9)

# print(5<<3)

# a=(12,)
# z=a
# print(a is z)

# x=12
# if type(x) is int:
#     print('true')
# x=1+2**3/4*5
# print(x)

# p[

# import math
# print(math.exp(2))

# x=input('Enter a value:')

# z,g=[int(x) for x in input('Enter some values: ').split()]
# print(z,g)
# ls=[4,5]
# b=bytes(ls)
# x= eval('10+2')
# print(x)

# import sys
# print(sys.argv[3])

# String Formatting !

# print('this is %i'%(10))

# Flow Control

# if,else,elif : Conditional Statements
# for,while : Iterative Statements.
# break,continue,pass : Transfer Statements.

# lst=[1,2,4,5]
# if lst[0]==2:
#     break
# i=0
# while i<=5:
#     # if i==3:
#     #     break
#     print(i)
#     i+=1
# else:
#     print('else sorry')

# def number():
#     pass

# string:
# [begin:end-1,steps]

# s='viveknagar'
# print(s[-2:3:-1])

s=':'.join(['1','2','3','4','5'])


# print('{:5d}'.format(23))
# print('{:05d}'.format(23))
# print('{:.2f}'.format(45.2350))
# print('{:8.3f}'.format(123.4567))
# print('{:f}'.format(123.4567))
# print('{:<5d}'.format(12))
# print('{:>5d}'.format(12))
# print('{:=5d}'.format(-12))
# print('{:^5d}'.format(45))

# unpacking concept:

# a,b,*c,g=[4,5,6,15,9,3,4]
# print(a,b,c,g)

# tp=tuple([1,2,3,4,5])
# print(sum(tp))

# dic={1:'vivek',2:'rohit',3:'sahil',400:'john'}
# print(dic.popitem())

# s={10,20,40}
# s.update([10,60,30])
# s.remove(60)
# print(s)

# tu=(10,20,30)
# tu.update()
# print(tu)

# x={10,20,30,40}
# y={30,40,50,60}
# print(x-y)

# x={10,10}
# print(x[0])

# s={15.4}
# print(type(s))
# tu=()
# print(type(tu))

# Functions:

# doc string always define function definition or purpose

# def sum(a=45,**b):
#     '''This function made for addition purpose !'''
#     print(b)
# val=sum(x='vivek',c='alice',b='john')
# print(id(sum))
# print(val)
# print(sum.__doc__)

# Python Support this kind of argument:

# Ordered argument (normal one):
# Keyword argument:
# Default value argument:
# Variable length argument: *args
# Variable length keyword argument: **args

# Parameter:

# global()

# def myfunc(n):
#     print(type(n))
#     return lambda a:a*n
# myvar=myfunc('vivek')
# print(myvar(2))

# from functools import *
# l=[5,10,15,20]
# result=(reduce(lambda x,y:x-y,l)
# print(result)

# l=[5,10,15,20]
# result=set(map(lambda x:x*2,l))
# print(result)

# s=lambda x,y:x*y
# print(s(5,2))

# def outer():
#     print('outer execution !')
#     def inner():
#         print('inner execution !')
#     return inner
# o1=outer()
# o1()
# o1()

# Class and Objects:

# How to define class in Python

# class add:
#     def __init__(self):
#         self.a='vivek'
#         self.b='Nagar'
# ref=add()
# print(ref.a,ref.b)

# if you want to inherit parent properties into child then:

# class parent:
#     def info(self):
#         print('This is parent properties !')
# class child(parent):
#     pass
# c=child()
# c.info()

# class Test:
#     def __init__(self,x):
#         self.a=x
#     def display(self):
#         print(self.a)
# n=Test(452)
# n.display()

# class Test:
#     x=800
#     def __init__(self):
#         self.a=100
#     def display(self):
#         self.b = 500
#         print(self.a,self.b,self.c,Test.x)
# t=Test()
# t.c=2000
# t.display()

# class Test:
#     a=12
#     def magic(self):
#         b=89
#         self.a=45
# t=Test()
# t.magic()
# print(Test.a)
# print(t.a)

# class math:
#     def sum(x,y):
#         print(x+y)
# math.sum(5,5)

# Inner Class

# class outer:
#     def display(self):
#         print('Outer !')
#     class inner:
#         def display(self):
#             print('Inner !')
# o=outer()
# o.display()
# i=o.inner()
# i.display()

# class math:
#     b=300
#     @classmethod
#     def dec(cls):
#         cls.c=400
#     @staticmethod
#     def sum():
#         a=200
#         print(a+math.b+math.c)
# m=math()
# m.dec()
# m.sum()

# Garbage collection:

# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())
# print(gc.get_threshold())

# import sys
# class Test:
#     @staticmethod
#     def sum(t):
#         t.a=200
#         t.b=300
#     def display(self):
#         print(self.a)
# t=Test()
# Test.sum(t)
# t.display()
# print(sys.g)

# Iheritance concept:

# class engine:
#     def m1(self):
#         print('engine')
# class car:
#     def __init__(self):
#         self.engine=engine()
#     def m2(self):
#         print('car',self.engine.m1())
# c=car()
# c.m2()

# class p:
#     def m1(self):
#         print('parent method !')
# class c:
#     def m1(self,x):
#         super(p,x).m1()
#         print('child method !')
# c=c()
# p=p()
# c.m1(p)

# class parent:
#     def __init__(self):
#         print('parent !')
# class child(parent):
#     def __init__(self):
#         super(parent,self).__init__()
#         print('child')

# c=child()
# c.__init__()

# class adder:
#     def sum(self,x,y):
#         print(x+y)
# class adding(adder):
#     def sum(self,x,y,z):
#         print(x+y+z)
# a=adder()
# c=adding()
# c.sum(100,100)
# c.super().sum(12,12)
# a.sum(12,12)

# Operator Overloading:

# class Book:
#     def __init__(self,x):
#         self.page=x
    # def __add__(self,other):
        # total=self.page+other.page
        # return total
    # def __add__(self, other):
    #     return Book(self.page+other.page)
    # def __str__(self):
    #     return 'total page: {}'.format(self.page)
# b1=Book(200)
# b2=Book(300)
# b3=Book(500)
# print(b1+b2)
# print(b1+b2+b3)
# print(b1)
# print(b2)

# class Account:
#     def __init__(self,amount):
#         self.__balance=amount
#     def get_balance(self):
#         return self.__balance
# a=Account(10000)
# print(a._Account__balance)
# print(a.get_balance())

# def special_wishes(fnc):
#     def inner(special_greet):
#         if special_greet=='Happy New Year 2021':
#             print(special_greet)
#         else:
#             fnc(special_greet)
#         return inner
# def wish(greet):
#     print(greet)
# wish('Good-morning')
# wish('Happy New Year 2021')

# def decor1(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner
# def decor(func):
#     def inner():
#         x=func()
#         return 2*x
#     return inner
# @decor1
# @decor
# def num():
#     return 10
# print(num())

# xsssssssssssss

# Generators

# def mygen():
#     yield 'vivek'
#     yield 'kumar'
#     yield 'nagar'
#     yield 'programmar'
# g=mygen()
# print(next(g))
# print(next(g))
# print(next(g))

# g=(x*x for x in range(100000000000))
# while True:
#     print(next(g))

# name=['Vivek','Shiv','Rahul']
# surname=['Nagar','Kumar','Sharma']
# for name,surname in zip(name,surname):
#     print(name,surname)

# What is Database:

# import django
# print(django.get_version())

# from tkinter import *
# from tkinter.ttk import *
#
# root=Tk()
# root.title('My_first Tkinter project')
# root.geometry('320x200')
# label= Label(root, text='hello world').pack()
# button= Button()
# root.mainloop()
