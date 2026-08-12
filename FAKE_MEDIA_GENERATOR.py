
# we will import the random module first.
import random
print("WELCOME YOU'LL TO INDIA'S BEST FAKE MEDIA GENERATOR !")
# we will make the list of few objects
subjects = ["Virat Kohli" , "Priyanka Chopra" , "Narendra Modi Ji" ,"Bheegi billi" ,"Meloni Ji","Samay Raina" ,"Mukesh Ambani"]
actions = ["drinks water", "plays cricket" ,"celebrates" ,"eats Pizza" ,"dances","faints","cries terribly" ]
places = ["at Red Fort", "at airport","at Fateh Chand Book Store","at gandhi smriti","in Italy","at India gate","in Nala Sopara",
          "on my terrace"]

while(True):
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    print(f"BREAKING NEWS : {subject} {action} {place}")

    user_enters = input("do you want to see more headlines ? (yes/no)").strip().lower()
    if(user_enters == "no"):
        break
print("Thank You for your time on our platform" +"\u2764\uFE0F")
