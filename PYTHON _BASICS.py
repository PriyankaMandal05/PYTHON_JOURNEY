"""print("hey, world")
print("hey, world")
print("hey, world")"""
# print("Priyanka here\nand this is my \"friend\".") #\" is an escape seq char.
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


list = [1,2,3,4,"priya", "8"]

list1 = [900,1000,1200]
print(list.extend(list1))
# print(list)
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




  










 
 





