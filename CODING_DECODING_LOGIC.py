# CODING - DECODING *** 
import random 
list_ofvariables = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = int(input("do you want to code or decode? (1) coding , 2) de-coding ) :"  ))
str = input("enter the text here : ")
words = str.split(" ")
newwords = []
if(x == 1 ):
    for word in words:
        if (len(word) >= 3):
            prefix = random.choice(list_ofvariables) +  random.choice(list_ofvariables) +  random.choice(list_ofvariables)
            suffix = random.choice(list_ofvariables) +  random.choice(list_ofvariables) +  random.choice(list_ofvariables)
            newstr = prefix + word[1: ]+word[0]+suffix
            newwords.append(newstr)

        else:
          newwords.append(word[::-1])
    print(" ".join(newwords)) 
else:
    for word in words:
            if (len(word) >= 3):
               newstr = word[3:-3]
               newstr = newstr[-1]+ newstr[:-1]
               newwords.append(newstr)
    
            else:
              newwords.append(word[::-1])
    print(" ".join(newwords)) 