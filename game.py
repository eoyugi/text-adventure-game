map = [
    ["start", None, None],
    [None, "treasure", None],
    ["enemy", None, "end"]
]

def print_location(current_location):
    """
    Generates a message describing the player's current location in a text-based adventure game.

    Parameters:
    current_location (list): A list representing the player's current location and the adjacent locations. 
    The first element is a string representing the current location. 
    The second, third, and fourth elements represent the locations to the north, east, and south, respectively.

    Returns:
    message (str): A string describing the player's current location and the types of the adjacent locations.
    """
    if current_location[0][0] == "S":
        message = "You are at the start of the path.\n\nAdjacent paths:\n  ↑ north\n  → east\n  ↓ south"
    elif current_location[0][0] == "T":
        message = "You have found the treasure!\n\nReturn to the start (← west) to win!"
    elif current_location[0][0] == "E":
        message = "Watch out - there's an enemy here!\n\nReturn to the start (← west) to escape."
    else:
        message = f"You are currently at {current_location[0][0]}."
        
    def print_location(current_location):
        """
        Generates a message describing the player's current location in a text-based adventure game.

        Parameters:
        current_location (list): A list representing the player's current location and the adjacent locations. 
        The first element is a string representing the current location. 
        The second, third, and fourth elements represent the locations to the north, east, and south, respectively.

        Returns:
        message (str): A string describing the player's current location and the types of the adjacent locations.
        """
        if current_location[0][0] == "S":
            message = "You are at the start of the path.\n\nAdjacent paths:\n  ↑ north\n  → east\n  ↓ south"
        elif current_location[0][0] == "T":
            message = "You have found the treasure!\n\nReturn to the start (← west) to win!"
        elif current_location[0][0] == "E":
            message = "Watch out - there's an enemy here!\n\nReturn to the start (← west) to escape."
        else:
            message = f"You are currently at {current_location[0][0]}."

        if current_location[1]:
            message += f"\n  ↑ north: {current_location[1][0][0]}"
        if current_location[2]:
            message += f"\n   → east: {current_location[2][0][0]}"
        if current_location[3]:
            message += f"\n  ↓ south: {current_location[3][0][0]}"
        
        return message
        map = [
            ["start", None, None],
            [None, "treasure", None],
            ["enemy", None, "end"]
        ]

        def print_location(current_location):
            """
            Generates a message describing the player's current location in a text-based adventure game.

            Parameters:
            current_location (list): A list representing the player's current location and the adjacent locations. 
            The first element is a string representing the current location. 
            The second, third, and fourth elements represent the locations to the north, east, and south, respectively.

            Returns:
            message (str): A string describing the player's current location and the types of the adjacent locations.
            """
    def print_location(current_location):
        if current_location[0][0] == "S":
            message = "You are at the start of the path.\n\nAdjacent paths:\n  ↑ north\n  → east\n  ↓ south"
        elif current_location[0][0] == "T":
            message = "You have found the treasure!\n\nReturn to the start (← west) to win!"
        elif current_location[0][0] == "E":
            message = "Watch out - there's an enemy here!\n\nReturn to the start (← west) to escape."
        else:
            message = f"You are currently at {current_location[0][0]}."

        if current_location[1]:
            message += f"\n  ↑ north: {current_location[1][0][0]}"
    current_location = map[0]
    if current_location[2]:
        message += f"\n   → east: {current_location[2][0][0]}"
    if current_location[3]:
        message += f"\n  ↓ south: {current_location[3][0][0]}"
    
    return message

def get_player_move():
    while True:
        move = input("Which way do you want to go? ")
        
        if len(move) != 1:
            print("Invalid command.")
            continue
        
        if move not in ("w", "a", "s", "d"):
            print("Invalid command.")
            continue
        
        break
    
    if move == "w": # move up
        return (-1, 0)
    elif move == "a": # move left
        return (0, -1)
    elif move == "s": # move down
        return (1, 0)
    else: # move right
        return (0, 1)
# Initialize starting location
current_location = map[0]

while True:
    print(print_location(current_location))
    
    dx, dy = get_player_move()
    
    new_x, new_y = current_location[0][0], current_location[0][1] + dy
    new_location = map[new_y][new_x]
    
    if new_location is None:
        print("There's nothing here!")
    elif new_location[0][0] == "E":
        print("Game over! You were killed by the enemy.")
        break
    elif new_location[0][0] == "T":
        print("Congratulations! You found the treasure and won the game!")
        break
    else:
        current_location = new_location
