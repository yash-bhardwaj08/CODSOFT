import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
round_number = 1

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

print(" Welcome to Rock, Paper, Scissors!")
print("Instructions: Type 'rock', 'paper', or 'scissors' to play.\n")

while True:
    print(f"\nRound {round_number}")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f" Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print(" It's a tie!")
    elif result == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1

    print(f" Score -> You: {user_score} | Computer: {computer_score}")

    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("\n Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        if user_score > computer_score:
            print(" Congratulations! You won the game.")
        elif user_score < computer_score:
            print(" The computer won the game. Better luck next time!")
        else:
            print(" It's a draw!")
        break

    round_number += 1
