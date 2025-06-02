import random as r
print("let's play rock paper scissors")

#https://www.asciiart.eu/people/body-parts/hand-gestures

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
out = {0:rock,1:paper,2:scissors}
inp = {0:'rock',1:'paper',2:'scissors'}


user_count=0
comp_count=0
game = 'Y'
while(game == 'Y'):
    user = int(input("Type 0 for rock, 1 for paper, 2 for scissors : "))
    print("User chose "+inp[user]+"\n"+out[user])
    comp = int(r.choice([0,1,2]))
    print("Computer chose "+inp[comp]+"\n"+out[comp])
    if(user == comp):
        print("That's a tie")
    elif(user ==0 and comp == 1): #rock and paper
        print("You Lost! Computer Won")
        comp_count = comp_count+1
    elif(user ==0 and comp == 2): #rock and scissors
        print("You Won!")
        user_count = user_count+1
    elif(user ==1 and comp == 2): #paper and scissors
        print("You Lost! Computer Won")
        comp_count = comp_count+1
    elif(user ==1 and comp == 0): #paper and rock
        print("You Won!")
        user_count = user_count+1
    elif( user ==2 and comp == 0): #scissors and rock
        print("You Lost! Computer Won")
        comp_count = comp_count+1
    elif(user ==2 and comp == 1): #scissors and paper
        print("You Won!")
        user_count = user_count+1
    game = input("Ready for another round? Y / N : ").upper()
print("Your Score : "+str(user_count)+"\n"+"Computer Score : "+str(comp_count))
