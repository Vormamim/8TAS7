
# imports
import sys
import os
import random
import time
from yachalk import chalk

# colors
dialogue_text = chalk.yellow_bright
output_text = chalk.green
error_text = chalk.red

# functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Print a newline

def display_inventory():
    print(output_text('Inventory: ' + ', '.join(player_inventory)))
def display_location():
    print(output_text('You are in ' + (player_location)))

def take_item(item):
    if item == locations[0][4]:
        player_inventory.append(item)
        locations[0][4] = ''
        print(output_text(f'You have taken the {item}.'))
    else:
        print(error_text(f'There is no {item} here.'))


# variables
player_inventory = ['Sword', 'Shield', 'Potion']
game_over = False
talkTuah = ('True')

# Define locations
locations = {
        "Forest": {
        "description": "You are standing in a dense forest. Trees tower above you, blocking out the sun.",
        "exits": ["north", "east"],
        "items": ["stick"],
        "next_locations": {"north": "Cave", "east": "Thornwood Village Main"}
    },
    "Cave": {
        "description": "You enter a dark cave. The air is damp and musty.",
        "exits": ["south"],
        #exit south is back to forest
        "items": ["torch"],
        "next_locations": ["Forest"]
    },
    "Thornwood Village Main": {
        "description": "You arrive in a bustling village. People are going about their daily lives.",
        #exit east is well, exit west is forest
        "exits": ["west","east"],
        "items": [],
        "next_locations": ["Forest", "Thornwood Well"] 
    },
    "Thornwood Well": {
        "description": "A deep well in the centre of the village, the elder said that there was a monster down there.",
        #exit east is Thornwood Village main, exit west is Mountain Path
        "exits": ["west","down","east"],
        "items": [],
        "monsters": [],
        "next_locations": ["Thornwood Village Main", "Thornwood Well Depths","Mountain Path"]
    },
    "Thornwood Well Depths": {
        "description": "A deep well in the centre of the village, the elder said that there was a monster down there.",
        #exit east is Thornwood Village main, exit west is Mountain Path
        "exits": ["up"],
        "items": [],
        "monsters": ["mutated rat"],
        "next_locations": ["Thornwood Well"]
    },
    "Mountain Path": {
        "description": "A desolate path winding up the mountains in distance.",
        #exit east is Thornwood Village Well, exit west is Mountain
        "exits": ["west","east"],
        "items": [],
        "monsters": ["goblin", "goblin", "goblin"],
        "next_locations": {"east": "Thornwood Well", "west": "Mountain"}
        
    },
"Mountain": {
    "description": "The summit of a tall mountain with a wyrmling living atop an empty dragon's nest.",
    #exit east is Thornwood Village Well, exit west is Mountain
    "exits": ["west","east"],
    "items": ["gold"],
    "monsters": ["wyrmling"],
    "next_locations": {"east":"Mountain Path"}
},
}

# Current location
current_location = "Mountain"

def move(direction):
    global current_location
    global locations
    if direction in locations[current_location]["exits"]:
        for location_data in locations:
        # Find the corresponding location based on the exit
            for location_name, location_data in locations.items():
                if direction in location_data["next_locations"]:
                    current_location = location_name
                    print(output_text(f"You move {direction} to the {location_name}."))
                return
    else:
        print(error_text(f"You cannot go {direction} from here."))

# Game loop
actions = ['take', 'use', 'go', 'look', 'inventory','talk']

# Game scenes
def scene_one():
    animate_text('Welcome to the game!')
    print('What is your name?')
    name = input('My name is: ')
    talkTuah = True
    print(dialogue_text('You have entered the bustling town of Thornwood, in front of you is an old, proud-looking man'))
    while True:
        action = input('What do you want to do? ').lower()

        if action.startswith('go e'):
            move('east')
            break # End this scene
        elif action == 'inventory':
            display_inventory()
        elif action == 'look':
            display_location('Thornwood Village')
        elif action.startswith('take'):
            print(error_text(f'There is no item here.'))
        elif action.startswith('talk'): 
                print(dialogue_text('Hello, you must be the monster-hunter we have called for! I am the village elder. I have been waiting for you to arrive. A monster sighting has just been reported, and we need your help to find it. We have been told that it is hiding in the well on the east of the village!'))
        elif action == 'quit':
            print(output_text('Thanks for playing!'))
            sys.exit()
        else:
            print(error_text("Invalid command."))

def scene_two():
    print('scene 2')

def scene_three():
    print('scene 3')

# main game loop
    clear_screen()
animate_text('Loading game...')
time.sleep(1)

# Game loop
current_scene = "scene_one"  # Initial scene

while True:  # Main game loop
    if current_scene == "scene_one":
        scene_one()
        current_scene = "scene_two"  # Transition to the next scene
    elif current_scene == "scene_two":
        scene_two()
        current_scene = "scene_three"
        # ... (Decide how to transition from scene_two)
    else:
        print(error_text("Invalid scene."))
        break  # Exit the game loop if an invalid scene is encountered
