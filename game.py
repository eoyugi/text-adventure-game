# Simple Python Text Adventure Game

def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark room with two doors. Which do you take?")
    print("1. The door on the left.")
    print("2. The door on the right.")

    choice = input("> ")

    if choice == "1":
        forest_path()
    elif choice == "2":
        dragon_room()
    else:
        print("That's not a valid choice. Try again!")
        start_game()

def forest_path():
    print("You've entered a dark forest. There's a path ahead.")
    print("Do you:")
    print("1. Follow the path.")
    print("2. Go back to the room with two doors.")

    choice = input("> ")

    if choice == "1":
        cave_entrance()
    elif choice == "2":
        start_game()
    else:
        print("Please enter a valid number.")
        forest_path()

def cave_entrance():
    print("You've come to a cave entrance. It's very dark inside.")
    print("Do you:")
    print("1. Enter the cave.")
    print("2. Go back to the forest.")

    choice = input("> ")

    if choice == "1":
        treasure_room()
    elif choice == "2":
        forest_path()
    else:
        print("Please enter a valid number.")
        cave_entrance()

def dragon_room():
    print("Oh no, you've walked into a room with a sleeping dragon!")
    print("What do you do?")
    print("1. Try to sneak past the dragon.")
    print("2. Attack the dragon.")
    print("3. Go back to the room with two doors.")

    choice = input("> ")

    if choice == "1":
        print("You successfully sneak past the dragon and live to adventure another day!")
        end_game()
    elif choice == "2":
        print("The dragon wakes up and you bravely face it in a fierce battle... but it's not enough. Game Over.")
        end_game()
    elif choice == "3":
        start_game()
    else:
        print("Please enter a valid number.")
        dragon_room()

def treasure_room():
    print("Congratulations! You've found the treasure room.")
    print("You see a chest full of gold and jewels.")
    print("Do you take the treasure and leave, or do you explore further?")
    print("1. Take the treasure.")
    print("2. Explore further.")

    choice = input("> ")

    if choice == "1":
        print("You take the treasure and leave the cave. You are now a rich adventurer!")
        end_game()
    elif choice == "2":
        print("As you explore further, you hear a loud rumbling sound. It's another dragon! Game Over.")
        end_game()
    else:
        print("Please enter a valid number.")
        treasure_room()

def end_game():
    print("Thank you for playing the game!")
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no) ")
    if choice.lower() == "yes":
        start_game()
    else:
        print("Goodbye!")

# Start the game
start_game()
