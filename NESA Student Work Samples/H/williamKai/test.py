# # Define grid dimensions
# GRID_WIDTH = 3
# GRID_HEIGHT = 3

# # Starting position
# player_x, player_y = 1, 1  # Start in the middle of a 3x3 grid

# def move_player(direction):
#     global player_x, player_y

#     if direction == "north":
#         if player_y > 0:
#             if player_y < GRID_HEIGHT:
#                 print('north')
#                 player_y += 1
#             else:    
#                 print("You can't move in that direction.")
#                 return
#         else:
#             print("You can't move in that direction.")
#             return
#     elif direction == "south":
#         if player_y > 0:
#             if player_y < GRID_HEIGHT:
#                 print('south')
#                 player_y -= 1
#             else:
#                 print("You can't move in that direction.")
#                 return
#         else:
#             print("You can't move in that direction.")
#             return
#     elif direction == "west":
#         if player_x > 0:
#             if player_x < GRID_WIDTH:
#                 player_x -= 1
#             else:
#                 print("You can't move in that direction.")
#                 return
#         else:
#             print("You can't move in that direction.")
#             return
#     elif direction == "east":
#         if player_x > 0:
#             if player_x < GRID_WIDTH:
#                 player_x += 1
#             else:
#                 print("You can't move in that direction.")
#                 return
#         else:
#             print("You can't move in that direction.")
#             return
#     else:
#         print("You can't move in that direction.")
#         return

#     print(f"You moved {direction}. You are now at position ({player_x}, {player_y}).")

# # Game loop
# def play_game():
#     print("Welcome! Move with 'north', 'south', 'east', or 'west'. Type 'quit' to exit.")
#     print(f"Starting position: ({player_x}, {player_y})")

#     while True:
#         command = input("Enter direction: ").strip().lower()
#         if command == "quit":
#             print("Thanks for playing!")
#             break
#         elif command in ["north", "south", "east", "west"]:
#             move_player(command)
#         else:
#             print("Invalid command. Try again.")

# play_game()

# # Define grid dimensions
# GRID_WIDTH = 3
# GRID_HEIGHT = 3

# # Starting position
# player_x, player_y = 1, 1  # Start in the middle of a 3x3 grid

# def move_player(direction):
#     global player_x, player_y

#     if direction == "north" and player_x > 0:
#         player_y += 1
#     elif direction == "south" and player_x < GRID_HEIGHT - 1:
#         player_y -= 1
#     elif direction == "west" and player_y > 0:
#         player_x -= 1
#     elif direction == "east" and player_y < GRID_WIDTH - 1:
#         player_x += 1
#     else:
#         print("You can't move in that direction.")
#         return

#     print(f"You moved {direction}. You are now at position ({player_x}, {player_y}).")

# # Game loop
# def play_game():
#     print("Welcome! Move with 'north', 'south', 'east', or 'west'. Type 'quit' to exit.")
#     print(f"Starting position: ({player_x}, {player_y})")

#     while True:
#         command = input("Enter direction: ").strip().lower()
#         if command == "quit":
#             print("Thanks for playing!")
#             break
#         elif command in ["north", "south", "east", "west"]:
#             move_player(command)
#         else:
#             print("Invalid command. Try again.")

# play_game()




# Game constants
GRID_WIDTH = 10
GRID_HEIGHT = 10
VALID_MOVES = ["n", "s", "w", "e"]

# Starting position
player_x = 1
player_y = 1

def move_player(direction):
    global player_x, player_y
   
    if direction == "n" and player_y < GRID_HEIGHT - 1:
        player_y += 1
        return True
    elif direction == "s" and player_y > 0:
        player_y -= 1
        return True
    elif direction == "w" and player_x > 0:
        player_x -= 1
        return True
    elif direction == "e" and player_x < GRID_WIDTH - 1:
        player_x += 1
        return True
    return False

def Move():
    print("Welcome! Move with 'n (north)', 's (south)', 'e (east)', or 'w (west)'. Type 'quit' to exit.")
    print(f"Starting position: ({player_x}, {player_y})")

    while True:
        command = input("Enter direction: ").strip().lower()
       
        if command == "quit":
            print("Thanks for playing!")
            break
           
        if command not in VALID_MOVES:
            print("Invalid command. Try again.")
            continue
           
        if move_player(command):
            print(f"You moved {command}. You are now at position ({player_x}, {player_y})")
        else:
            print("You can't move in that direction.")

