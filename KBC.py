# WE ARE MAKING THE LEGENDARY KBC !

print("NAMASKAR"+"\U0001F64F" +"WELCOME TO KAUN BANEGA CROREPATI(KBC) !")
print("Deviyon aur Sajjano , are u ready for the questions?"+"\u2764\uFE0F" )


questions_list = [
    ["He loves me or he loves me not ?" ,"loves me","loves me not","is obsessed","Dont know",4],
    ["how many legs does a spider have?","1","4","6","8",4],
    ["kya aam aadmi aam kha sakte hain?","bilkul kha sakte h","aam h toh kya hua aadmi toh hai","nahi kha sakte","apne apne dimaag ka prayog kare!",4],
    ["Dilli ka best street food kya hai?","chole bhature","aloo tikki","golgappe","chole kulche",4],
    ["Britishers ne humare desh se sabse zada kya churaya?","spices","Gold","our Culture","sab churake legye SAALE CHOR!",4],
]

levels= [1000,2000,4000,6000,10000]

# loop to access all the inner lists pf questions_list.
# money = 0
# sum = 0
# for i in range(0,len(questions_list)):
 

#     print(f"\n\n Aapka sawaal {levels[i]} Rs. keliye :")
#     print(questions_list[i][0])
#     print(f"a. {questions_list[i][1]}       b. {questions_list[i][2]} ")
#     print(f"c. {questions_list[i][3]}       d. {questions_list[i][4]} ")
#     sum = sum + levels[i]

    
     
         

#     user_input = int(input("enter your answer(1-4) : "))
#     if(user_input == questions_list[i][-1] ):
#         print(f"Badhai Ho !!! Aap jeet gaye rs. {levels[i]}")

  
             
#         x = input("kya aap aage khelna chahte hain? Dar toh nhi rahe na HAIYEN"+"\U0001F44D")
#         if(x == "quit"):
#                 print(f"aapki dhanraashi aapko puri milegi {sum} "+"\U0001F44D")
#                 break
#         if(i == 0):
#             money = levels[i]
#         elif(i == 2):
#             money = levels[i]    
#         elif(i == 4):
#             money = levels[i]
#     else:
#         print("WRONG ANSWER :( \n Better luck next time"+"\u2764\uFE0F")
#         print(f"{money} Dhanraashi aapki hui" +"\u2764\uFE0F")
#         break

money = 0
sum = 0
for i in range(0,len(questions_list)):
 
 if i ==0 :
    print(f"\n\n Aapka sawaal {levels[i]} Rs. keliye :")
    print(questions_list[i][0])
    print(f"a. {questions_list[i][1]}       b. {questions_list[i][2]} ")
    print(f"c. {questions_list[i][3]}       d. {questions_list[i][4]} ")
    # sum = sum + levels[i]

    user_input = int(input("enter your answer(1-4) : "))
    if(user_input == questions_list[i][-1] ):
        print(f"Badhai Ho !!! Aap jeet gaye rs. {levels[i]}")
        sum = sum + levels[i]
    else:
         print("WRONG ANSWER :( \n Better luck next time"+"\u2764\uFE0F")
         print(f"{money} Dhanraashi aapki hui" +"\u2764\uFE0F")
         break

 else:  
    print(f"\n\n Aapka sawaal {levels[i]} Rs. keliye :")
    print(questions_list[i][0])
    print(f"a. {questions_list[i][1]}       b. {questions_list[i][2]} ")
    print(f"c. {questions_list[i][3]}       d. {questions_list[i][4]} ")
    # sum = sum + levels[i]       
    x = input("kya aap aage khelna chahte hain? Dar toh nhi rahe na HAIYEN"+"\U0001F44D")
    if(x == "quit"):
         print(f"\n aapki dhanraashi aapko puri milegi {sum} "+"\U0001F44D")
         break
    user_input = int(input("enter your answer(1-4) : "))
    if(user_input == questions_list[i][-1] ):
     print(f"Badhai Ho !!! Aap jeet gaye rs. {levels[i]}")
     sum = sum + levels[i] 
     if(i == 0):
            money = levels[i]
     elif(i == 2):
            money = levels[i]    
     elif(i == 4):
            money = levels[i]
    else:
        print("WRONG ANSWER :( \n Better luck next time"+"\u2764\uFE0F")
        print(f"{money} Dhanraashi aapki hui" +"\u2764\uFE0F")
        break
    
     
         


  

        
   

