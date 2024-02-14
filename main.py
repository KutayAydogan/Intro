import random
choices = ["rock","paper","scissors"]
while True:
    pc_choice = random.choice(choices)
    your_choice = input("Please select rock, paper or scissors:")
    your_choice = your_choice.lower()
    print(f"\nYou chose {your_choice}, computer chose {pc_choice}.\n")
    if pc_choice == your_choice:
         print("It's a tie")
    elif your_choice == "rock":
        if pc_choice == "paper":
             print("Rock loses to Paper, You lose.")
        else:
            print("Rock beats Scissors, You win.")
    elif your_choice == "paper":
        if pc_choice == "rock":
             print("Paper beats Rock, You win.")
        else:
            print("Paper loses to Scissors, You lose.")
    elif your_choice == "scissors":
        if pc_choice == "rock":
            print("Scissors loses to Rock, You lose.")
        else:
            print("Scissors beats Paper, You win.")
    play_again = input("Play again? (y for yes , n for no): ")
    if play_again.lower() != "y":
        break
