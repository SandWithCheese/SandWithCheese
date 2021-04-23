import random

i = 0
while i < 1:
    computer_hand = ["Rock", "Paper", "Scissors"]
    computer_index = random.randint(0, 2)
    computer_play = computer_hand[computer_index]
    computer_play = computer_play.upper()

    user_hand = input("Rock/Paper/Scissors! ")
    user_hand = user_hand.upper()

    if (user_hand == "ROCK" and computer_play == "ROCK") or (user_hand == "PAPER" and computer_play == "PAPER") or (user_hand == "SCISSORS" and computer_play == "SCISSORS"):
        print(f"It's {user_hand} against {computer_play}. Try Again! ")
    elif (user_hand == "PAPER" and computer_play == "ROCK") or (user_hand == "ROCK" and computer_play == "SCISSORS") or (user_hand == "SCISSORS" and computer_play == "PAPER") :
        print(f"It's {user_hand} against {computer_play}. You Win! ")
        i += 1
    elif (user_hand == "PAPER" and computer_play == "SCISSORS") or (user_hand == "SCISSORS" and computer_play == "ROCK") or (user_hand == "ROCK" and computer_play == "PAPER"):
        print(f"It's {user_hand} against {computer_play}. You Lose! ")
        i += 1
    else:
        print("Invalid input. Please try again! ")
