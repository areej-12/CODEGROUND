#variables-container data store
lecture="Lecture 1"
print(type(lecture))
# data types string , int , float , bool
a=5
b=3.44
flag=True # bool True(1) or False(0)
print(type(a),type(b),type(flag))
# input
name=input("Enter name:")
print("hello",name)
#type conversion->to change data type
num=2
num1=2.2 # float
print(num)
print(f"num1: {int(num1)}") #2
# f -> to dynmaically write variables in the print statement
num1=int(num1) # assign to num1
print(f"num1:{num1}",num1)#2.2
# Comment-> give context about programmer logic
# num1 -> number 1 variable that stores a value
"""
multi- line comment 
"""
# basic operations + - * / **-> expo //->floor div
a=3
b=9
#\n-> newline 
print(f"Add:{a+b}\n Sub:{a-b}\n Mult:{a*b}")
#comparison operators > < =< =>
print(f"Add:{a>b}\n Sub:{a<b}\n Mult:{a>=b}")
#Logical operators  and,or,not
print(a>10 and b<10) # True if both are True
print(a>10 or b<10) # True if both are True
print(not(a>10)) # True if both are True


