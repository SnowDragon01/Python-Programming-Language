import random
choice=["rock","paper","scissor"]
computer_choice=random.choice(choice)
user_choice=input("Enter your choice (rock,paper,scisor) :")
if computer_choice==user_choice:
    print("Match Tied!")
if computer_choice=="rock" and user_choice=="paper":
    print("You win!")
if computer_choice=="rock" and user_choice=="scossor":
    print("You lost!")
if computer_choice=="paper" and user_choice=="rock":
    print("You lost!")
if computer_choice=="paper" and user_choice=="scissor":
    print("You win!")
if computer_choice=="scissor" and user_choice=="paper":
    print("You lost!")
if computer_choice=="scissor" and user_choice=="rock":
    print("You win!")
print("computer choosed :",computer_choice)