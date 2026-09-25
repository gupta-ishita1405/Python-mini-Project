import random 

target=random.randint(1,100)

while True :
    n= (input("enter a number to see if its target numbeer or Quit[Q]  :-"))
    if(n=="Q"):
        break

    n=int(n)
    if(n==target):
        print("correct Target Number")
        break
    elif(n<target):
        print("Your number is smaller than targated value try again---")
    else:
        print("Your number is larger than targated value try again---")



print("---GAME OVER---")