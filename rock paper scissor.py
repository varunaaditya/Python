import random

def play_round():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (Rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return None

    print(f"Computer chose {computer_choice}.")
    
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def main():
    user_score = 0
    computer_score = 0

    while True:
        result = play_round()

        if result == 'user':
            user_score += 1
            print("You win this round!")
        elif result == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        elif result == 'draw':
            print("It's a draw!")

        print(f"Score: You {user_score} - {computer_score} Computer")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()