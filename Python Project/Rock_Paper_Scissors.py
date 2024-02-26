import random
def get_user_choice():
    """
        Prompts the user to enter their choice of rock, paper, or scissors.

        Returns:
            The user's choice as a string.

        Raises:
            ValueError: If the user enters an invalid choice.
    """
    while True:
        user_choice = input("Enter Your Choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    """
        Returns a random choice from the set of possible computer choices.

        Returns:
            A random choice from the set of possible computer choices.
    """
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """
        Determines the winner of a rock, paper, scissors game based on the user's and computer's choices.

        Args:
            user_choice (str): The user's choice of rock, paper, or scissors.
            computer_choice (str): The computer's choice of rock, paper, or scissors.

        Returns:
            str: A message indicating the winner of the game.

        Raises:
            ValueError: If the user or computer enters an invalid choice.

    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Plays an interactive game of rock, paper, scissors."""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
# Run the game
play_game()