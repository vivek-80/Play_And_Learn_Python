# we are here to learn python in deapth and make a command on each and every single topic.
# then anybody ask a questions regarding to python you can answer it.

# what is python ?

# { Python is a general purpose, High level programming language which is being used in web
# -development, machine learning, along with new technologies like AI.python allows 
# programming in object and procedural oriented, python indentation concept make python 
# more readable all the time.}

# print('Hello There !')

# Identifiers :

# a=10

# total=45
# TOTAL=89
# print(total,TOTAL)

# import keyword
# print(keyword.kwlist)

# a='Hello There !'
# print(type(a))

# a='Hey you can talk !'
# print(id(a))

# a=oct(6)
# print(a)

# { The process of converting the value of one data type(integer, string, float etc) to
# another type is called type conversion or type casting.}

# { Into Which You Have To Convert that Function you have to use !}

# a= float(2)
# print(a)

# print(str(45))

# Remember Points:

# { if you want to convert str type to int type then compulsory string should specified in

# integral form or in other words base 10 form.}

# int():

# 1) int(10+5j) -> Type Error can't convert complex to int.

# 2) int('10') -> OK 

# 3) int('10.5') -> Value Error.

# 4) int('ten') -> Value Error.

# float():

# 1) same as int() except int('10.5')

# 2) float('10.5') -> OK

# bool():

# bool(0) -> False

# bool(1) -> True

# bool(2) -> True

# bool(0.0) -> False

# bool(0.12) -> True

# bool('') -> False

# bool('True') -> True

# bool('False') -> False

# bool(None) -> False

# bool({}) -> False

# bool(()) -> False

# bool([]) -> False

# bool([4]) -> True

# Escape Characters:

# print(str(10))

# @ Operator Concept:

# Arithmetic Data type:
# ---------------------

# + Addition

# - Substraction

# * Multiplication

# / Division

# % Modulo

# // Floor Division 

# ** Exponent Operator.

# print(3+5)
# print(5-2)
# print(5*2)
# print(3/2)
# print(135%2)
# print(3**2)

# Operator Precedence:

# () -> parenthesis
# ** -> Exponent Operator
# ~,- -> Bitwise Complement and Unary Minus Operator.
# *,/,%,// -> 
# +,- ->

# Floor Division:

# print(10/3)
# print(10.0//3)

# (+) Operator With string:

 
# { if you are using + Operator with string then both the argument should be string.}

# print('100'+'200') // OK
# print('100'+200) // Type Error

# {if you are using * Operator with string then one argument should be int and other one
#  should be string.}

# List Comprehension:

# x=[ x for x in range(1,5) if x%2==0]
# print(x)

# x=[print(x,end='') for x in 'vivek' if x not in ['a','e','i','o','u']]

# Ternary Operator and Conditional Operator:

# a,b=10,55
#    or
# a=10;b=5
# x= 30 if a>b else 40
# print(x) 

# x= 'hello' if a>b 'Welcome' if a<b else 'good-bye !'

# a,b,c=10,20,30
# max= a if a>b and a>c else b if b>c else c

# is and is not operator we are using for address comparsion.

# a=30
# b=20
# print(a is b)// False
# print(a is not b)// True

# a = 2
# b = 11
# if b % a == 0 : 
# 	print("b is divisible by a")
# elif b + 1 == 10: 
# 	print("Increment in b produces 10")
# else: 
# 	print("You are in else statement")

# a,b,c,d= 10,20,30,40
# if a+1>c and c-1<d:
# 	print('hello')
# else:
# 	print(a)

# we can use break and continue inside loop only.

# def Remove(duplicate): 
#     final_list = [] 
#     for num in duplicate: 
#         if num not in final_list: 
#             final_list.append(num) 
#     return final_list

# def unique_names(names1, names2):
#     z=names1+names2
#     return Remove(z)

# if __name__ == "__main__":
#     names1 = ["Ava", "Emma", "Olivia"]
#     names2 = ["Olivia", "Sophia", "Emma"]
#     print(unique_names(names1, names2))

# lst= [12,14,15,14,16,15]
# print(list(dict.fromkeys(lst)))

# print(True+True+True) // 3 (valid)

# Range Data-type:

# 1) Form: range(10)

# 2) Form: range(2,9)

# 3) Form: range(1,10,1)

# Eval('it Evaluate Expressions')

# ex:
# x= eval('hello')
# print(x)

# NOTE: eval() Function always take string as an argument.

# if you are using string with % then nothing is required
# if you are using string with format function then . is required.

# print('this is %d'%(2))
# print('{} is divisible by 2'.format(10))

# To Check Birth of date:

# x=int(input('Enter Your Birth Year: '))
# y=int(input('Enter Your current Year: '))
# print('Currently Your Age is: %i'%(y-x))

# String Deapth:

# Any Sequence of Characters Enclose within Double quotes and Single quotes.

# for Eg:
	 
	 # s='vivek' (valid)
	 # s="vivek" (valid)

# multi-line doc-string:

# def sum(a,b):
# 	''' This function we use for 
# 	     addition.'''
# 	return a+b
# print(sum(5,5),sum.__doc__)

# How to Access characters of a string?

# s='vivek'
# print(s[1])

# Slicing Concept In Python.

# if you are not specfying any value in beginning and ending as well then by defualt 
# it consider whole string.

# s='vivek'
# print(s[:])// vivek

# s= 'viveknagar'
# print(s[1:])// iveknagar

# s[begin:end-1]

# s= 'viveknagar'
# print(s[2:7]) // vekna

# Negative indexing in string 

# s= 'abcdefghij'
# print(s[::-1]) // jihgfedcba



# Note: when we move backward dir both +ve and -ve indexing should be considered.

# Best ex:

# s= 'abcdefghij'
# print(s[-1:3:-1])

# s= 'abcdefghij'
# print(s[-4:1:-1]) // gfedc

# (==) operator use for content comparison.

# s= 'vivek'
# s1= 'vivekn'
# print(s==s1)

# rstrip():

# Best ex:

# s= 'vivek     '
# s1=s.rstrip()
# s2= 'vivek'
# print(s1==s2)

# lstrip()  

# s= '   vivek'
# print(s)
# print(s.lstrip())

# strip() used to removes spaces from both the side.

# updating string:

# s='viveknagar'
# s[0]='k'
# print(s)

# s='{:.5d}'.format(123)
# print(s)



# NOTE THAT: WHY WE SAY STRING IS DYNAMIC because we can change the size of list as per 
#            Our requirement.

# how many ways are there to create list.

# So there are two ways through which we can create list.

# first is: lst= []
# second is: lst= list() by using list method.

# List:

# lst=[1,2,'vivek',0.45,'True']
# print(lst)

# s='vivek'
# lst=list()
# print(lst)

# lst1=[1,2,3]
# lst2=[4,5,6]
# lst1.extend(lst2)
# del lst1[1]
# print(lst1)

# 2D list:

# lst=[[1,2,3,4],[5,6,7,8]]
# print(lst[1][2])

# To remove duplicate from the list:

# def duplicate_removal(lst):
# 	new_lst= []
# 	for x in lst:
# 		if x not in new_lst:
# 			new_lst.append(x)
# 	print(new_lst)
# lst=[4,2,3,4,1,5,2,5]
# duplicate_removal(lst)

# List Comprehension.

# lst=[int(x) for x in range(1,50) if x%2==0]
# print(lst)

# if you want to take input in single line then.

# lst=[int(x) for x in input('Enter few numbers: ').split()]
# print(lst)

# Nested if in list Comprehension:

# num_list = [y for y in range(50) if y % 2 == 0 if y % 5 == 0]
# print(num_list)

# if and else in List Comprehension:

# obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
# print(obj)

# Tuple:

# tp= (7,5,6,7)
# tp[0]=10
# print(tp)// Type error

# Tuple with list:

# lst= [4,5,6,7]
# lst[0]=11
# print(lst) // executable.

# NOTE: list is Mutable and Tuple is Immutable.

# has_good_credit= True
# has_criminal_record= False

# if has_good_credit and not has_criminal_record:
# 	print('Eligible for loan')

# while loop:

# as long as the condition is true the inner content will get execute when condition become False it
# never execute.

# i=1
# print('\n')
# while i<=5:
# 	print('*'*i)
# 	i+=1

# Guessing number:

# secret_number= 7
# guess_count=0
# guess_limit=3

# while guess_count<guess_limit:
# 	x=int(input('Guess the value: '))
# 	if x==secret_number:
# 		print('You Won')
# 		break
# 	guess_count+=1
# else:
# 	print('Try some-other time')

# dic:

# dic={100:'vivek',122:'rohit'}
# print(dic.pop(100))
# print(dic)

# d={100:'vivek',101:'alex',102:'alice',103:'greece'}
# for k,v in d.items():
# 	print(k,'--',v)

# message = input('>').split(' ')
# dic = {
# 	':)': '😆',
# 	':(': '😣'  
# }
# out= ''
# for ch in message:
# 	out+=dic.get(ch,ch) + ' '
# print(out)
# print(dic[':)'])

# Module Concept:

# A file contain group of functions, classes, variables that file is nothing but module.  
# Every Python file with .py extention act as a module.

# import math as m
# print(m.sqrt(25)) 

# USE of Sleep Functions.
# import time
# print('Am i late ?')
# time.sleep(5)
# print('Yes you are !')

# The special variable:

# Object Serialization:

# Object Serialization can be do by using JSON.
# Object Serialization can be do by using Pickle.
# Object Serialization can be do by using Yaml.

# import json
# emp= {
#     'name':'vivek',
#     'roll_no':121,
#     'salary':'1000',
#     'designation':'leader',
#     'age': None
# }
# json_string= json.dumps(emp,indent=2,sort_keys=True)
# print(json_string)

# with open('employee.json','w') as f:
#     json.dump(emp,f,indent=2)

# x= float(2.5)
# print(x)

# x='hello'[0]
# print(x)

# s='viveknagar'
# print(s[:-7])

# pickling:

# import pickle 
# class Employee:
# 	def __init__(self,eno,ename,esal,eaddr):
# 		self.eno= eno
# 		self.ename= ename
# 		self.esal= esal
# 		self.eaddr= eaddr
# 	def display(self):
# 		print(self.eno,self.ename,self.esal,self.eaddr)
# e=Employee(123,'vivek',2000,'123 bhopal')
# with open('emp.dat','wb') as f:
# 	pickle.dump(e,f)
# with open('emp.dat','rb') as f:
# 	obj= pickle.load(f)
# 	obj.display()

# class user:
# 	def func(self):
# 		pass
# class chil_user():
# 	def func(self):
# 		print()


import sys 
print(sys.argv[1])