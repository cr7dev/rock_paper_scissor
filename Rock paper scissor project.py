import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
player_choice_num= int(input())
print(player_choice_num)
comp_choice = random.randint(1, 3)
print(comp_choice)
if player_choice_num==1 and comp_choice ==2:
    print("YOU LOST")
if player_choice_num==2 and comp_choice ==1:
    print("YOU WIN")
if player_choice_num==1 and comp_choice ==3:
    print("YOU WIN")
if player_choice_num==3 and comp_choice ==1:
    print("YOU LOST")
if player_choice_num==2 and comp_choice ==3:
    print("YOU LOST")
if player_choice_num==3 and comp_choice ==2:
    print("YOU WIN")
if player_choice_num==comp_choice:
    print("DRAW")
