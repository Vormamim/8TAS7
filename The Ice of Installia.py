import os
import random
import sys
import time
from yachalk import chalk

# variables
player_inventory = []
player_location = 'Mystical Forest'
location_history = []
# locations found in the game that the player will visit, along with all the exits and items in each location
locations = {
    'Mystical Forest': {
        'description': ' Surrounding you is a vast land of trees. The forest looks like a winter wonderland but instead of wonder it was hell. The trees were dead, no leaf in sight with icicles hanging and wicked branches clinging to the trees for dear life. The ground was white no ground in sight and it was covered in thick layers of snow, so thick that when you walk through the forest your knees are buried deep into the layers of snow. You see some frost-covered houses down below.',
        'exits': {'north': 'Village of Installia'}, 
        'item': 'dagger'
    },
    'Village of Installia': {
        'description': 'Your crew arrives at the village, barely, and scan the area; villagers were frozen as well as their tears, it was a sorrowful sight. Your crew tries all the doors and all reveal useful items except two locked doors. They are locked for your fellow crew but are they for you?',
        'exits': {'south': 'Mystical Forest', 'east': 'Lake Kirkrey'}, 
        'item': 'pickaxe'
    },
    'Lake Kirkrey': {
        'description': 'Your crew walks to the infamous Lake Kirkrey. The lake is frozen and has thick layers of ice. You can see the cracks of the people who attempted to bust the myth, you could see the people themselves through the ice; they were screaming for help. There seems to be some rocky opening to the east of the lake. There is a submerged boat under the frozen surface of the lake. Maybe try breaking the ice?',
        'exits': {'west': 'Village of Installia', 'by boat': 'Cave Grotto Entrance'}, 
        'item': 'torch'
    },
    'Cave Grotto Entrance': {
        'description': 'Your crew musters up the courage to walk to the cave you had seen in the distance earlier. As you advance towards it, you see a snowman next to the entrance. The snowman has a freakishly human build about it and next to it there is a sign that says to not enter unless you want to end up like the snowman next to you. Willing to test your luck?',
        'exits': {'by boat': 'Lake Kirkrey', 'north': 'Cave Grotto'},
        'item': 'air'
    },
    'Cave Grotto': {
        'description': 'The inside of the cave is pitch black and nothing can be seen. You ask your crew if they’re okay and your voice echoes. It was colossal and was a void of darkness. You were staring at what you thought was your friend but, in reality, it was actually you staring into the abyss.',
        'exits': {'south': 'Cave Grotto Entrance', 'east': 'Nest of the (not-so-Mythical) Dragon'},
        'item': 'air'
    },
    'Nest of the (not-so-Mythical) Dragon': {
        'description': "Your crew finds to entrance to the (not-so) mythical dragon's nest. There is no sunlight reaching here, and it is weirdly chilly.",
        'exits': {'west': 'Cave Grotto'},
        'item': 'air'
    }
}
# actions and more items
action_verbs = ['move', 'search', 'inventory', 'quit', 'use']
random_scene_items = ['brain', 'cake', 'cryoconite']

# text colours
game_text = chalk.white.italic.bold
player_text = chalk.green
location_text = chalk.blue
exit_text = chalk.magenta
inventory_text = chalk.yellow_bright
item_text = chalk.cyan_bright
error_text = chalk.red.bold

# functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_inventory():
    print(inventory_text('Inventory: ' + ', '.join(player_inventory)))

def display_location(location_name):
    if location_name in locations:
        location = locations[location_name]
        print(location_text(f"You are at {location_name}: {location['description']}"))
        print(exit_text(f"Exits: {', '.join(location['exits'].keys())}"))
        print(item_text('There may be something around you that could be useful.'))
        return
    if location_name == 'Nest of the (not-so-Mystical) Dragon':
        print(item_text('There is nothing here.. or is there?'))
        return
    print(game_text("You have already been here."))
    print(error_text("Location not found."))

def move(direction):
    global player_location
    global location_history
    while True:
        if direction in locations[player_location]['exits']:
            location_history.append(player_location) 
            new_location = locations[player_location]['exits'][direction]
            print(location_text(f'You move {direction} to {new_location}.'))
            player_location = new_location
            break
        else:
            direction = input(error_text('Invalid direction. Which way do you want to move? ')).lower()    

def use(item):
    if item in player_inventory:
        if item == 'torch' and player_location == 'Cave Grotto':
            if 'battery' in player_inventory:
                print(item_text('You put the battery into the torch and turn it on and light up the cave.'))
                locations['Cave Grotto']['description'] = 'You can now see into the cave. There are words on the far wall.'
                player_inventory.remove('battery')
                print(location_text('Your crew spots an opening inside the cave. You advance toward it.'))
                move('north')
            else:
               print(item_text('You try to turn on your torch but there is no battery. You need to find one. Try using something to open one of the locked doors in the village maybe?'))
        elif item == 'dagger' and player_location == 'Village of Installia':
            print(item_text('You use the dagger on one of the locked doors. You kick it open. There is a key inside. You take it into your inventory.'))
            player_inventory.remove('dagger')
            player_inventory.append('key')
        elif item == 'key' and player_location == 'Village of Installia':
            print(item_text('You use the key on the second locked door. It opens. Inside is a box. You use your dagger to open it. Inside is a battery, which you take. What are you gonna need a battery for??'))
            player_inventory.append('battery')
            player_inventory.remove('key')
        elif item == 'pickaxe' and player_location == 'Lake Kirkrey':
            print(item_text('You use the frostbitten pickaxe to break the thick layer of ice on the lake. A boat floats to the surface. Maybe you can get to the cave by boat?'))
            player_inventory.remove('pickaxe')
        elif item == random.choice(random_scene_items) and player_location == 'Nest of the (not-so-Mythical) Dragon':
            print(item_text('You use your food item to feed the dragon and he is satisfied. He lets lifts the mist.'))
        else:
            print(error_text("You can't use that here."))
    else:
        print(error_text("You don't have that item."))

def grab(item):
    if item == locations['Mystical Forest']['item']:
        player_inventory.append(item)
        locations['Mystical Forest']['item'] = ''
        print(item_text(f'You have grabbed the {item}.'))
        return
    elif item == locations['Village of Installia']['item']:
        player_inventory.append(item)
        locations['Village of Installia']['item'] = ''
        print(item_text(f'You have grabbed the {item}.'))
    elif item == locations['Lake Kirkrey']['item']:
        player_inventory.append(item)
        locations['Lake Kirkrey']['item'] = ''
        print(item_text(f'You have grabbed the {item}.'))
    elif item == locations['Cave Grotto']['item']:
        player_inventory.append(item)
        locations['Cave Grotto']['item'] = ''
        print(item_text(f'You have grabbed the {item}.'))
    else:
        print(error_text(f'There is nothing around here. Try elsewhere.'))

# scene 1 - the forest
def scene_one():
    animate_text(game_text('Spooky much?'))
    display_location('Mystical Forest')

    while True:
        action = input(player_text('What do you want to do? ')).lower()

        if action == 'move':
            move(input(player_text('Which way?')))
            break
        elif action == 'use':
            item = input(player_text('What do you want to use? '))
            use(item)
        elif action == 'inventory':
            display_inventory()
        elif action == 'search':
            grab('dagger')
        elif action == 'help':
            print(game_text('Actions: move, use, inventory, search, quit'))
            print(game_text('Use "help" to see this message again.'))
        elif action == 'quit':
            print(game_text('Thanks for playing!'))
            sys.exit()
        else:
            print(error_text("I don't understand that command."))
# scene 2 - village
def scene_two():
    animate_text(game_text('You made it to the village!'))
    display_location('Village of Installia')

    while True:
        action = input(player_text('What do you want to do? ')).lower()

        if action == 'move':
            move(input(player_text('Which way?')))
            break
        elif action == 'use':
            item = input(player_text('What do you want to use? '))
            use(item)
        elif action == 'inventory':
            display_inventory()
        elif action == 'search':
            grab('pickaxe')
        elif action == 'help':
            print(game_text('Actions: move, use, inventory, search, quit'))
            print(game_text('Use "help" to see this message again.'))
        elif action == 'quit':
            print(game_text('Thanks for playing!'))
            sys.exit()
        else:
            print(error_text("I don't understand that command."))
# scene 3 - lake
def scene_three():
    animate_text(game_text('Looks cold!'))
    display_location('Lake Kirkrey')

    while True:
        action = input(player_text('What do you want to do? ')).lower()

        if action == 'move':
            move(input(player_text('Which way?')))
            break
        elif action == 'use':
            item = input(player_text('What do you want to use? '))
            use(item)
        elif action == 'inventory':
            display_inventory()
        elif action == 'search':
            grab('torch')
        elif action == 'help':
            print(game_text('Actions: move, use, inventory, search, quit'))
            print(game_text('Use "help" to see this message again.'))
        elif action == 'quit':
            print(game_text('Thanks for playing!'))
            sys.exit()
        else:
            print(error_text("I don't understand that command."))
# scene 4 - cave entrance
def scene_four():
    animate_text(game_text("You made it to the cave entrance but it doesn't look inviting..."))
    display_location('Cave Grotto Entrance')

    while True:
        action = input(player_text('What do you want to do? ')).lower()
        
        if action == 'move':
            move(input(player_text('Which way?')))
            break
        elif action == 'use':
            item = input(player_text('What do you want to use? '))
            use(item)
        elif action == 'inventory':
            display_inventory()
        elif action == 'search':
            grab('torch')
        elif action == 'help':
            print(game_text('Actions: move, use, inventory, search, quit'))
            print(game_text('Use "help" to see this message again.'))
        elif action == 'quit':
            print(game_text('Thanks for playing!'))
            sys.exit()
        else:
            print(error_text("I don't understand that command."))
# scene 5 - cave
def scene_five():
    animate_text(game_text("Your crew steps into the cave but it's too dark to see anything. Maybe try and use something to light it up?"))
    display_location('Cave Grotto')

    while True:
        action = input(player_text('What do you want to do? ')).lower()

        if action == 'move':
            move(input(player_text('Which way?')))
            break
        elif action == 'use':
            item = input(player_text('What do you want to use? '))
            use(item)
        elif action == 'inventory':
            display_inventory()
        elif action == 'search':
            grab('air')
        elif action == 'help':
            print(game_text('Actions: move, use, inventory, search, quit'))
            print(game_text('Use "help" to see this message again.'))
        elif action == 'quit':
            print(game_text('Thanks for playing!'))
            sys.exit()
        else:
            print(error_text("I don't understand that command."))
# scene 6 - dragon nest
def scene_six():
    animate_text(game_text("Is this a... nest?"))
    display_location('Nest of the (not-so-Mythical) Dragon')
    while True:
        nest_choice = input(player_text('Do you dare search the area?')).lower()
        if nest_choice == 'yes':
            print(game_text('You will regret that.'))
            animate_text(game_text('Your breath hitches as you can faintly make out some letters on the rough walls.'))
            read = input(player_text('Do you want to read what it says?'))
            if read == 'yes':
                print(game_text('You read the letters.'))
                animate_text(game_text("They read: You should have gone back when you had the chance...Your neck hairs rise as you feel a rush of chilly air run down your back. You turn to see the not-so-mythical ice dragon standing behind you. In one swift motion, it grabs you by your throat and your last memory is the betrayal in it's deep piercing blue eyes.") + chalk.red.bold(' GAME OVER'))
                break
            elif read == 'no':
                print(game_text('You decide not to read the letters.'))
                animate_text(game_text("You cannot help but peek at them however. They seem to call to you and you trust them. They read: You should have gone back when you had the chance... Your neck hairs rise as you feel a rush of chilly air run down your back. You turn to see the not-so-mythical ice dragon standing behind you. In one swift motion, it grabs you by your throat and your last memory is the betrayal in it's deep piercing blue eyes.") + chalk.red.bold(' GAME OVER'))
                break
            break
        elif nest_choice == 'no':
            decision1 = input(player_text('Are you sure?')).lower()
            if decision1 == 'yes':
                print(game_text('You decide to not search area.'))
                decision2 = input(player_text('Do you want to go back instead?'))
                if decision2 == 'yes':
                    scene_five()
                    direction = (input(player_text('Which way again?')))
                    if direction == 'west':
                        scene_four()
                        direction = (input(player_text('Which way again?')))
                        if direction == 'west':
                            scene_three()
                            direction = (input(player_text('Which way again?')))
                            if direction == 'south':
                                scene_two()
                                scene_three()
                                scene_four()
                                scene_four()
                                scene_five()
                                scene_six()
                                break
                            elif direction == 'east':
                                scene_four()
                                scene_five()
                                scene_six()
                                break
                        elif direction == 'east':
                            scene_five()
                            scene_six()
                            break
                    elif direction == 'north':
                        scene_six()
                        break
                elif decision2 == 'no':
                    print(game_text('You decide to search the area because you will look like a coward if you go back. You may regret that.'))
                    animate_text(game_text('Your breath hitches as you can faintly make out some letters on the rough walls.'))
                    read = input(player_text('Do you want to read what it says?'))
                    if read == 'yes':
                        print(game_text('You read the letters.'))
                        animate_text(game_text("They read: You should have gone back when you had the chance...Your neck hairs rise as you feel a rush of chilly air run down your back. You turn to see the not-so-mythical ice dragon standing behind you. In one swift motion, it grabs you by your throat and your last memory is the betrayal in it's deep piercing blue eyes.") + chalk.red.bold(' GAME OVER'))
                    elif read == 'no':
                        print(game_text('You decide not to read the letters.'))
                        animate_text(game_text("You cannot help but peek at them however. They seem to call to you and you trust them. They read: You should have gone back when you had the chance...Your neck hairs rise as you feel a rush of chilly air run down your back. You turn to see the not-so-mythical ice dragon standing behind you. In one swift motion, it grabs you by your throat and your last memory is the betrayal in it's deep piercing blue eyes.") + chalk.red.bold(' GAME OVER'))
                        break    
            elif decision1 == 'no':
                decision3 = input(player_text('So do you want to search the area?'))
                if decision3 == 'yes':
                    print(game_text('You will regret that.'))
                    animate_text(game_text('Your breath hitches as you can faintly make out some letters on the rough walls.'))
                    read = input(player_text('Do you want to read what it says?'))
                    if read == 'yes':
                        print(game_text('You read the letters.'))
                        animate_text(game_text("They read: You should have gone back when you had the chance...Your neck hairs rise as you feel a rush of chilly air run down your back. You turn to see the not-so-mythical ice dragon standing behind you. In one swift motion, it grabs you by your throat and your last memory is the betrayal in it's deep piercing blue eyes.") + chalk.red.bold(' GAME OVER'))
                        break
                    elif read == 'no':
                        print(game_text('You decide not to read the letters.'))
                        animate_text(game_text("You cannot help but peek at them however. They seem to call to you and you trust them. They read: You should have gone back when you had the chance...Your neck hairs rise as you feel a rush of chilly air run down your back. You turn to see the not-so-mythical ice dragon standing behind you. In one swift motion, it grabs you by your throat and your last memory is the betrayal in it's deep piercing blue eyes.") + chalk.red.bold(' GAME OVER'))
                        break
                elif decision3 == 'no':
                    print(game_text('You decide not to search the area.'))
                    print(game_text("Your curiosity got the better of you and you ordered your crew to search...Your neck hairs rise as you feel a rush of chilly air run down your back. You turn to see the not-so-mythical ice dragon standing behind you. In one swift motion, it grabs you by your throat and your last memory is the betrayal in it's deep piercing blue eyes." + chalk.red.bold(' GAME OVER')))
                    break
        else:
            print(error_text("I don't understand that command."))

def random_item_scene():
    random_item = random.choice(random_scene_items)
    print(item_text(f'You find a {random_item} outside the cave and take it. You might need it.'))
    player_inventory.append(random_item)




# main game loop
clear_screen()
animate_text('Loading game...')
time.sleep(1)
animate_text('Welcome to the Ice of Installia!')
time.sleep(1)
print(inventory_text('Actions: move; to move, use; to use an item in your inventory, inventory; list of your collected items, search; search for nearby items, quit; exit the game   Use "help" to see this message again'))
time.sleep(3)
scene_one()
time.sleep(2)
scene_two()
time.sleep(2)
while True:
    direction = (input(player_text('Can you repeat which way again?')))
    if direction == 'south':
        scene_one()
        time.sleep(2)
        scene_two()
        time.sleep(2)
        direction = (input(player_text('Can you repeat which way again?')))
        if direction == 'south':
            scene_one()
            time.sleep(2)
            scene_two()
            time.sleep(2)
        elif direction == 'east':
            scene_three()
            time.sleep(2)
            break
    elif direction == 'east':
        scene_three()
        time.sleep(2)
        break
        
while True:
    direction = (input(player_text('Can you repeat which way again?')))
    if direction == 'west':
        scene_two()
        time.sleep(2)
        direction = (input(player_text('Can you repeat which way again?')))
        if direction == 'south':
            scene_one()
            time.sleep(2)
            scene_two()
            time.sleep(2)
            scene_three()
            time.sleep(2)
            direction = (input(player_text('Can you repeat which way again?')))
            if direction == 'west':
                scene_two()
                time.sleep(2)
                scene_three()
                time.sleep(2)
            elif direction == 'by boat':
                scene_four()
                time.sleep(2)
                break
        elif direction == 'east':
            scene_three()
            time.sleep(2)
            scene_four()
            time.sleep(2)
            break
    elif direction == 'by boat':
        scene_four()
        time.sleep(2)
        break

while True:
    direction = (input(player_text('Can you repeat which way again?')))
    if direction == 'by boat':
        scene_three()
        time.sleep(2)
        direction = (input(player_text('Can you repeat which way again?')))
        if direction == 'west':
            scene_two()
            time.sleep(2)
            scene_three()
            time.sleep(2)
            scene_four()
            time.sleep(2)
            scene_five()
            time.sleep(2)
        elif direction == 'by boat':
            scene_four()
            time.sleep(2)
            random_item_scene()
            time.sleep(2)
            scene_five()
            time.sleep(2)
            break
    elif direction == 'north':
        random_item_scene()
        time.sleep(2)
        scene_five()
        time.sleep(2)
        break

scene_six()
time.sleep(2)
print("THANKS FOR PLAYING 'THE ICE OF INSTALLIA'")
sys.exit()

