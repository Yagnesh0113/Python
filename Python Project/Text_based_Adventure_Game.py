import time
def intro():
    print("Welcome to the text Advaenture Game!")
    print("You wake up in a mysterious room...")
    time.sleep(2)
    print("You see two doors in front of you")
    time.sleep(1)

def choose_door():
    if True:
        choice = input("Which door do you choose? (left/right): ").lower()
        if choice == "left" or choice == "l":
            print("You chose the left door.")
            time.sleep(1)
            return "left"
        elif choice == "right" or choice == "r":
            print("You chose the right door.")
            time.sleep(1)
            return "right"
        else:
            print("Invalid choice. Please enter 'left' or 'right'.")

def left_door():
    print("You open the left door and step into a dark hallway.")
    time.sleep(2)
    print("You hear footsteps approaching...")
    time.sleep(2)
    print("A monster appears!")
    time.sleep(1)
    print("You have been eaten by the monster. Game Over!")

def right_door():
    print("You open the right door and find a treasure chest!")
    time.sleep(2)
    print("Congratulations! You found the treasure. You win!")

def play_game():
    intro()
    door_choice = choose_door()
    if door_choice == "left":
        left_door()
    else:
        right_door()

play_game()