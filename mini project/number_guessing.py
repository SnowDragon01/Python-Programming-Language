# build a number guessing game where user inputs the number and computer tells too higjh or too low >>

import random

randomNumber=random.choice(range(1,100))



while True:
    userInput=int(input("Enter Your Guess :"))
    if userInput>randomNumber:
        print("Goo Lower!")
    elif userInput<randomNumber:
        print("Goo Higher!")
    else:
        print("Correct Guess!")
        break

    


