#[ Decorator is function it take a function as a argument and extend its functionality and
# returns the modified function with extended functionality ]

# def more_feature(func):
#     def inner(a,b):
#         op=input('Enter The Operation : ')
#         if op.lower()=="add":
#             return a+b
#         if op.lower()=="sub":
#             return a-b
#         if op.lower()=="mul":
#             return a*b
#     # print('hello')
#     return inner
# @more_feature
# def calcul(a,b):
#     return a+b
# value=calcul(4,5)
# print(value)

# To Execute outer and inner function.

# def outer():
#     def inner():
#         print('inner')
#     print('outer')
#     return inner
# x=outer
# x()
