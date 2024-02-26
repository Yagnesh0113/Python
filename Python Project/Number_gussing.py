import random
def number_guessing():
    secret_number = random.randint(1,100)
    attempts = 0
    max_attempts = 10
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it within 10 attempts?")
    while attempts < max_attempts:
        guess_input = input("Enter your guess: ")
        # Check if the input is empty
        if not guess_input:
            print("Please enter a number.")
            continue
        try:
            guess = int(guess_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            break
        print()
    else:
        print(f"Sorry, you've used up all {max_attempts} attempts. The correct number was {secret_number}.")
number_guessing()