import random

while True:

    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None
    
    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!!!")
        
    elif player == "rock":
         if computer == "scissors":
             print("computer: ", computer)
             print("player: ", player)
             print("You win!!!")
         if computer == "paper":
             print("computer: ", computer)
             print("player: ", player)
             print("You are a loser ~ hahaha!")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("I win ~ hahaha")
    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print(" You win! Congratsss !")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Game over ~ hahaha")
            
    play_again = input("Play again? (yes/no): ").lower()
    
    if play_again !="yes":
        break
print("See you later, dude !")
