# We are making a finance tracker app in which we can keep a track of our expenses.
# making a list to keep our topics.
print("WELCOME TO 'THE FINANCE TRACKER' !!! \n # Sahi jagah kharcho :)")
allExpenses = []

while(True):
    print("Choose the type of service :")
    print("1) Add an expense")
    print("2) View all expenses till date")
    print("3) Get total amount spent")
    print("4) Exit App")

    choice = int(input("enter service number: "))

    if(choice == 1):
        date = input("Enter the date of purchase :")
        category = input("Enter the category of your purchase(clothes,makeup,books,etc.):")
        particular_detail = input("describe your purchase in particular:")
        amount = int(input("enter its amount :"))

        expenses = {
            "date" : date,
            "category": category,
            "particular_detail":particular_detail,
            "amount": amount
        }

        allExpenses.append(expenses)
        print("CONGRATS! EXPENSE ADDED SUCCESSFULLY !")

    elif(choice == 2):
        if(len(allExpenses)== 0):
            print("NO purchase.")

        else:

           count = 1
           for i in allExpenses:
            print(f"your expense no.{count} is on {i["date"]} of {i["category"]}, in which u purchased {i["particular_detail"]} and its price was {i["amount"]}")    
            count = count + 1

    elif(choice == 3):
        for i in allExpenses:
           total = 0
           total = int(total + i["amount"])
           print("Total amount spent = "+total)    

    elif(choice == 4):
       print("THANK YOU FOR VISITING OUR APP " +"\U0001F64F")

    else:
       print("INVALID CHOICE . TRY AGAIN")   
