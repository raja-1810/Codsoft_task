import random

def get_computer_choice():
    """Randomly generate the computer's choice."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the game outcome."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_scores(user_score, computer_score):
    """Display the current scores."""
    print("\n=== Current Scores ===")
    print(f"User: {user_score} | Computer: {computer_score}")
    print("======================\n")

def play_round():
    """Play a single round of Rock-Paper-Scissors."""
    while True:
        user_choice = input("Enter your move: (rock, paper, scissors):").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            break
        print("Invalid input! Please choose rock, paper, or scissors.")
    
    computer_choice = get_computer_choice()
    print(f"\nYour pick is: {user_choice}")
    print(f"\nThe computer picked: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("Victory is yours this round!")
    else:
        print("The computer takes this round!")
    
    return winner

def main():
    """Main function to run the Rock-Paper-Scissors game."""
    print("Let's play Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0
    
    while True:
        winner = play_round()
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        display_scores(user_score, computer_score)
        
        play_again = input("Want to go another round? (yes/no):").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
