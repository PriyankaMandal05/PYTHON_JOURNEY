"""print("hey, world")
print("hey, world")
print("hey, world")"""
# print("Priyanka here\nand this is my \"friend\".") # (\") is an escape seq char.
# print("priyanka",  "girl",  21, sep="$",end="*") #sep separates everything with the symbol in it($) & end just ends the line with the char

# CALCULATOR***

# a = 1
# b = 2
# print("addition of",a ,"+",b , "=",a+b)
# print("substraction of",a ,"-",b , "=",a-b)
# print("multiplication of",a ,"*",b , "=",a*b)
# print("division of",a ,"/",b , "=",a/b)

# EXPLICIT CONVERSION*** (TYPE-CASTING)

# a = "5"
# b = 3
# print(int(a)+b)



#INPUT FROM USER***

# a = input("enter your name:")
# b = input("enter your roll_no. :")
# print(a)
# print(b)
# print(a+b)

# a = input("enter 1st no.:")
# b = input("enter 2nd no. :")
# print(a+b)
# print(float(a)+float(b))



# CONDITIONAL- STATEMENTS***

# a = input("Enter your skin type:")
# print("your skin type is : ",a)
# if(a == "dry"):
#     print("prep skin well before make-up.")
# elif(a == "oily"):
#     print("use oil free skin-care.")
# else:
#     print("maybe u have ",a,"skin bby!")  


# EXERCISE-2 SOLUTION***

# x = int(input("what time is it now ? :"))
# print("it's ", x,"am/pm")
# if(x <= 11 ):
#     print("good morning sir/mam !")
# elif(x>= 12 and x <= 15):
#     print("good afternoon sir/mam !")
# elif( x > 15 and x<=19):
#     print("good evening sir/mam !")   
# else:
#     print("good night sir/mam !") 
   



#FOR- LOOP***

# age = "twenty one"
# for k in age:
#     print(k)
# for i in range(0,5,2): # for using step* , we must provide all the 3 arguments.
#     print(i)



# WHILE- LOOP***

# num = int(input("enter a no. : ")) # this is executed only once. we never come back to here.
# print (num)

# while(num <= 10): # here whatever num we are entering, it first prints then the condition is checked and loop runs.
#     num = int(input("enter a no. : "))
#     print(num)

# # print("we have come outside the loop!")  
# else:    # like print after loop stops running.
#     print("i am inside else statement.") 



# DO-WHILE LOOP***

#  => every condition is true and loop runs,  till break statement is hit.
# i = 0
# while (True) :
#     i = int(input("enter no. "))
#     print(i)
#     if(i > 200):
#         break




# BREAK-CONTINUE STATEMENTS***

# for k in range(10):
#     print(k)
#     if(k== 8):
#         break
# print("outside for loop")    


# for k in range(10):
#     print(k)
#     if(k == 7):
#         continue

# FUNCTIONS***

# def average_of_num(x,y,z):
#     average = (x+y+z)/3
#     print(int(average))

# a = 1
# b= 2
# c= 3
# average_of_num(a,b,c) 




# LIST IN PYTHON***


# list = [1,2,3,4,"priya", "8"]

# list1 = [900,1000,1200]
# print(list.extend(list1))
# print(list)
# print(list[1:3])

# for i in list: # THIS PRINTS ALL ITEMS SEPARATELY AS ITERATIONS 
#     print(i)
# print(list[5])  
# print(list)

# if "pri" in list:   => THIS SAME IF - ELSE CHECK CAN BE DONE FOR STRINGS ALSO.** 
#     print("yes")  
# else:
#     print("not at all") 
# if "priy" in "priya":
#     print("yes")
# else:
#      print("no") 

# list = [i for i in range(10) if (i% 2) == 0 ]  # LIST COMPREHENSION        
# print(list)



# TUPLE IN PYTHON***

# tup = (2,4,6,8,10)
# # tup[0]= 8 // not possible in tuple as immutable
# print(tup)
# print(type(tup))

# print( tup[1:3])
# # print(tup1)
# print(tup[:3])
# if 8 in tup:
#     print("yes")
# else:
#     print("no")    

# tup1 = (1,2)
# tup2 = (3,4)
# print(tup1 + tup2)
# print(len(tup1))

# EXERCISE - 2 SOLUTION 2***
# import time
# t = time.strftime('%H : %M : %S')
# hour = int(time.strftime('%H'))
# print(t)
# print(hour)
# hour = int(input("enter hour : "))

# if(hour > 0 and hour < 12):
#     print("good morning!")
# elif(hour >= 12 and hour< 16 ):
#     print("good afternoon!")  
 # (OR) elif(hour >= 16 ):
 #     print("good evening!")
# else:
#     print("good evening!")     
 
  

# EXERCISE - 3***
# print("NAMASKAR ! WELCOME TO KAUN BANEGA CROREPATI(KBC)")
# print("Deviyon aur Sajjano , are u ready for the questions? " \
# "(in yes/no)")
# print(input())
# print("1Q - how many legs does a spider have?")
# print("1) 2")
# print("2) 4")
# print("3) 6")
# print("4) 8") 
# choice = int(input("enter your choice : "))
# match choice:
#     case 1:
#         print("2") 
#     case 2:
#         print("4") 
#     case 3:
#         print("6")    
#     case 4:
#          print("8") 
#     case _:
#          print("Sirf 4 hi options hai Deviyon aur Sajjano !!! ")


# if(choice == 4):
#     print("7 CRORE !!!")
# else:
#     print("try next time " \
#     "SHAAVA SHAAVA ")    



# import this (THE ZEN OF PYTHON)


# SETS IN PYTHON***

# FIBONACCI SERIES***
# def fibonacci(n):
#     if(n == 0 or n == 1):
#         return n
#     else:
#        return fibonacci(n-1) + fibonacci(n-2)
    
# # print(fibonacci(3))
# for i in range(5):
#     print(fibonacci(i), end =" ")


# SET METHODS***
# newset = set()
# print(type(newset))

# set1 = { 1,2,3}
# set2 = {3,4,5}
# newset = set1.union(set2)
# print(newset)
# set1.update(set2)
# print(set1 , set2)

# set1 = { 1,2,3}
# set2 = {3,4,5}
# newset = set1.intersection(set2)
# print(newset)
# set1.intersection_update(set2)
# print(set1 , set2)

# set1 = { 1,2,3}
# set2 = {3,4,5}
# newset = set1.symmetric_difference(set2)
# print(newset)
# set1.symmetric_difference_update(set2)
# print(set1 , set2)

# set1 = { 1,2,3}
# set2 = {3,4,5}
# newset = set1.difference(set2)
# print(newset)
# set1.difference_update(set2)
# print(set1 , set2)


# DICTIONARY IN PYTHON***

# student = {
#     "name" : "priyanka",
#     "class": "I-123",
#     "college": "MAIT",

# }

# for key in student.keys():
#     print(key)

# for key in student.keys():
#     print(student[key])

# print(student["name"])

# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())



# BY USING f-STRING***
# for key,value in student.items():
#     print(f"the value of {key} is {value}")
# OR
# for key in student.keys():
#     print(f"the value of {key} is {student[key]}")

# dict1 = {"num1":  1,
#          "num2": 2,
#          "num3": 3
#          }
# dict2 = {
#     # "num4":  4,
#     "num5": 5,
#     "num6": 6

# }
# print(dict1)
# print(dict2)
# dict1.update(dict2)
# print(dict1)
# dict2.update({"num9" : 5}) #if key is not present earlier, then it add new key value pair.(doesnot change the existing value of key for same value)
# print(dict2)

# dict1.clear()
# print(dict1)

# x = dict2.pop("num4","num5") 
# print(x)
# print(dict2)

# dict2.popitem()
# print(dict2)

# del dict1["num2"]
# print(dict1)



# ELSE- IN FOR LOOP***

# for n in range(5):
#     # if(n == 3):
#     #     break
#     print(n)
# else:
#     print("out of loop")



# EXCEPTION HANDLING***

# try:
#    a = int(input("enter number :"))
#    print(f"the multiplication  of {a} is :")
#    for i in range(1,5):
#      print(f"{int(a)} x {i} = {int(a)  *  i}")
# except Exception as x :
#   print(x)

# print("end of code")  

# FINALLY CLAUSE***
# try:
#     list = [1,2,3,4]
#     user = int(input("enter index:"))
#     print(list[user])
# except Exception as x:
#     print(x)    
# finally:
#     print("i am anyways executed.")    
        
# print("i am anyways executed.")    here, no difference is observed in using print / finally.*
# def new_function():
#     try:
#       list = [1,2,3,4]
#       user = int(input("enter index:"))
#       print(list[user])
#       return 1
#     except Exception as x:
#       print(x)   
#       return 0 
#     #finally:
#     #   print("i am anyways executed.")  

#     print("ALWAYS") # THIS IN IN LIGHT COLOR BCZ => VS CODE THINKS THIS CODE WILL NEVER BE EXECUTED.
# print("always") # this will be printed first*. AS FUNCTION IS CALLED AFTER THIS.
# y = new_function()
# print(y)


     

# RAISING CUSTOM ERRORS***

# x = input("enter any string :").strip().lower() # input always returns a string, so doesnt matter u input int /str.

# if(x == "quit"):
#     print("yay! successfull code.")
# else:
#     raise ValueError("error occured :( ") 




# ENUMERATE FUNCTION***
# string = "priyanka"
# for index,i in enumerate(string,start = 1):
#     # print(f"{index}:{i}" ,end =" ")
#     print(index,i)

# list = [1,2,3,4,5]
# for index,i in enumerate(list):
    
#     print(index,i)




# IMPORT WORKING  ***
# import new 
# new.func()

# import new as n
# n.func()

# from new import * # here nothing is printed bcz, there is no top level code that has print statement. & we dint call func().

# from new import *  # hereprint inside func is printed bcz, there is no top level code that has print statement. & we called func() first, then x which is just a variable.
# func()
# print(x)

# from new import * as s  # INVALID.
# s.func()

import new 
new.func()
















  










 
 





