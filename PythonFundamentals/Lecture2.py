#-----------Conditional Statement
age=20 #sensitive -> line by line --hard code
age=int(input("Enter the age:")) #age -1
# if (condition)-> basic , logical,etc
# error input -> str comparison int
# method 1:
#age=int(age)
if age >=18: # 20> 18
    print("You can vote")
elif age <=50:
    print("Yes, you can still vote.")
 #else if = elif
elif age <=17:#  elif we can add condition elif <condition>:
    print("You cannot vote.")
else :
    print("Incorrect Input!")
# elif  and else

# nested condition if ->if
age=22
has_cnic=True #bool -> True or False -> operators Logical and or not if ____
is_citizen=True
# if ____:
#         _____
# else declare, you must declare if
if age>=18: # 1st condition condition -->defined->rules 
    if has_cnic: # 2nd condition if has_cnic 
        # if has_cnic==True:
        print("You can Vote")
        if is_citizen:
            print("You can vote")
        else:
            print("Bring Citizenship papers")   
    else: # logic Handling->verification
        print("Please Bring Cnic")
else:
    print("You cannot vote")
#Case Statement-> multiple nested else if
day=2 # user -> day value we have to find -> what day it is? 1,2,3,4,5,6,7
#case statement
#user-> laymen 
#Error Handling -> edge cases solves
#edge case user input day=10
day=int(input("Enter the day number:"))
# python input -> str
match day: # keyword-> cant declare them as variable day==1
    case 1: #case <condition> # day==1-> true or fasle
        print("Monday")
    case 2: # day ==2 T or F
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4: #case <condition> # day==1-> true or fasle
        print("Thursday")
    case 5: # day ==2 T or F
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _: # Error Handling 
        print("Invalid Input")

# why conditional:
# user input validation, error handling, control flow/ logic flow control flow
