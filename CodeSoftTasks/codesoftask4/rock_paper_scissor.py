import random

print("=== ROCK PAPER SCISSORS GAME ===")
print("Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:

    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print("\nYour Choice:", user_choice)
    print("Computer Choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\nScore Board")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        print("Thanks for playing!")
        break