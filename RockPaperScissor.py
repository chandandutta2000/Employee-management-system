import random
import time
Moves = ['rock', 'paper','scissors']

while(True):
    player = input("Enter your move : ").lower()
    if player == 'exit':
        exit()
    print("Computer Move : ")
    computer = random.choice(Moves)
    time.sleep(1)
    print(computer)

    if player == computer:
        print("Tie")
    elif (player == 'rock' and computer == 'scissors') or \
        (player == 'paper' and computer == 'rock') \
        or (player == 'scissors' and computer == 'paper'):
            print("You won...")
    elif (player == 'rock' and computer == 'paper') or \
        (player == 'paper' and computer == 'scissors') \
        or (player == 'scissors' and computer == 'rock'):
            print("Computer won...")

    else:
        print("invalid input")