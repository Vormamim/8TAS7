# Author: Vanessa
# Date
# Purpose: A text-based adventure game where the player must escape a haunted hospital.
#import libraries
import sys
import os
import random
import time
from yachalk import chalk
#font colours
narrative = chalk.black
main_story = chalk.red
error_text = chalk.blue

player_location = 'hallway'
game_over = False
#lists
Inventory = ["compass"]
locations = ['hallway', "storage", "emergency room", "inpatient ward", "dungeon", "control room"]
action_verbs = ["collect", "use", "move", "exit", "inventory", "quit"]
items = ["bread", "energy bar", "canned fish", "water", "antiseptic", "bandages", "flashlight", "storageroomkey"]
entity =  ["ghost", "phantom", "vampire", "You hear strange noises behind you. Thankfully, when you look around, there's nobody there. You must have been spared."]
Health = 5
#defining functions 
def quit_game():
    print("You have quit the game. The game will now close.")
    time.sleep(1)
    cls()
    sys.exit()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
#show inventory function when printing inventory
def showInventory():
    print("Inventory:", ", ".join(Inventory))
#compass shows you where the objective items are in which room
def Compass():
    if "water" not in Inventory:
        print("You need water. Try the emergency room.")
    elif "bandages" not in Inventory:
        print("You need bandages. Try the inpatient ward.")
    elif "bread" not in Inventory:
        print("You need bread. Try the storage room.")
    else:
        print(error_text("I do not understand that command."))
    

def sceneOne():
    print(narrative("You limp through the discarded debris of the fragments of gravel and bones piercing into the sole of your feet. The filthy strip of cloth encircling around your wounded side begins to fall off, bloodied and painted a gruesome crimson, but it doesnt matter. You're almost there. With the last of your energy, you wipe the grime and sweat from your forehead and swipe at the curtain of underbrush ahead,  revealing a looming building in midst of human carcasses sprawled in a sea of red. If it wasnt for the massive cross peeking from the carpet of moss and vines snaking up the colourless concrete, you wouldn't have known it was a hospital."))

def sceneOneP2():
    print(narrative("\nYou walk to the porch, and twist the door handle. Surprisingly, the door creaks open with a creak, and you step inside. The building is dark, and the only light comes from the stained windows. The air inside is thick with the scent of decay and neglect, every creak and groan of the aged structure echoing like a ghostly whisper. Faded posters clung desperately to crumbling walls, and the dim light filtering through grime-encrusted windows were casting eerie shadows on the walls."))

def sceneTwo():
    print(narrative("\nEvery creak of the floorboards beneath you amplify the eerie silence. The walls, lined with peeling paint and faded wallpaper, close in as you tread deeper into the heart of the hospital."))

def StorageRoom():
    print(main_story("\nYou try the storage room door. It's locked. Perhaps you’ll need a key."))

def StorageRoomP2():
    print(main_story("You push open the heavy door to the storage room, the rusted hinges groaning in protest. Inside, it's a claustrophobic clutter of dusty shelves and scattered medical supplies. Boxes are piled haphazardly, some spilling their contents onto the grimy floor."))

def EmergencyRoom():
    print(main_story("\nYou push through the doors of the Emergency Room, a place once pulsing with life and urgency. Now, it lies in a heavy, suffocating silence. The monitors, once vital and beeping, are now cold and dark. Every corner of the room whispers stories of frantic, desperate efforts to save lives – now just echoes in the stillness."))

def ControlRoomPart1():
    print("\nIt's dark. Perhaps you'll need a flashlight.")

def ControlRoomPart2():
    print(main_story("\nThe control room is shrouded in darkness. Monitors flicker, casting ghastly shadows on the cracked, mold-covered walls. Operators, haunted by the chill of the forgotten, scan screens for anomalies whispering from the past. Security feeds show long-forgotten, pitch-black corridors, and  the communication lines crackle with ghostly echoes."))

def InpatientWard():
    print("The inpatient ward loomed in eerie silence, its once-vibrant walls now peeling and faded. Dust motes danced in the shafts of light that pierced the cracked windows, illuminating remnants of forgotten lives. Drawers remain ajar, and you wonder if you can find anything useful here.")

def entity_spawn():
  global Health #refers the same health whenever printed bc its global
    #random entity from list
  random_entity = random.choice(entity)
  if random_entity == "ghost" or random_entity == "vampire" or random_entity == "phantom":
    print(f'You encounter a {random_entity}')
    print("Possible actions:")
      #if energy bar in inventory u can fight the entity, but if not, there are no possible options, so you lose health
    if "energy bar" in Inventory:
        print("You have used energy bar to fight entity")
    elif "energy bar" not in Inventory:
      print("There are no possible options.")
      print("The entity strikes. You have lost a heart.")
        #different -health for the randomly generated entities
    #ghost and vampire does the same thing, so i can put it in the same line
      if random_entity == "ghost" or "vampire":
        Health -= 1
        print(f"Your health is now at {Health}")
          #phantom is -2 health, 
      elif random_entity == "phantom":
        Health -=2
        print(f"Your health is now at, {Health}")
          
  else:
    print(f'{random_entity}')

#def so that u can proceed to finish the game
def closingScene():
            print("You have collected all the items needed to escape. You can now proceed to the Dungeon.")
            input("To proceed, press Enter")
            print("You have finished the game. Congratulations! You have left the hospital, and can escape the country.")

def item_drop(Item):
    global Health 
    #global health again for items that heal
    Collected = input(main_story(f'You find a {Item}. Type "Collect" to store it, "Leave" to ignore it. '))
    #if your input is collect it will add to inv
    if Collected == "Collect":
        Inventory.append(Item)
        print(f'You have collected {Item}')
        #different printed text for different items u get to explain
        if Item == "flashlight":
            print(main_story("You will need this to see in the dark."))
            #two itmes at a time bc they have the same +1 health
        elif Item in ["antiseptic", "canned fish"]:
            action = input(main_story("Type 'Use' to consume or 'Leave' to store. "))
            if action == "Use":
                print(main_story(f"You have used {Item}. You feel better."))
                global Health
                Health += 1
                print(f"Your health is now {Health}")
            else:
                print(f"{Item} stored in your inventory.")
        elif Item == "storageroomkey":
            print(main_story("You will need this to open the storage room."))
        elif Item in ["bread", "water", "bandages"]:
            print("This is an objective item. Collect the rest to escape.")
    else:
        print(f'You leave the {Item} alone')

    
def hallwayActions():
    global player_location
    player_location = "hallway"
    print("You are in the hallway, the heart of the hospital...")
    #whenever in hallway if you have these items, and if you do, you can finish the game.
    if "bread" in Inventory and "water" in Inventory and "bandages" in Inventory:
        closingScene()
        quit()
    print("You can see a direction sign pointing to the emergency room, the inpatient ward, the control room, and the storage room.")
    player_choice = input(main_story("Where would you like to go? "))
#using my defs from before to make less lines to read
    if player_choice == "emergency room":
        player_location = "emergency room"
        EmergencyRoomActions()
    elif player_choice == "inpatient ward":
        player_location = "inpatient ward"
        inpatientWardActions()
    elif player_choice == "control room":
        ControlRoomActions()
    elif player_choice == "storage room":
        StorageRoomActions()
    elif player_choice == "quit":
        print('Exiting game from the hallway')
        time.sleep(3) #this is text where its delayed
        quit_game()
    else:
        print(error_text("I do not understand that command. Try again."))
        hallwayActions()

def inpatientWardActions():
    global player_location
    player_location = "inpatient ward"
    InpatientWard()
    #while in impatient ward, it will keep asking you what actions u want to do
    while player_location == "inpatient ward":
        actions = input(main_story("Actions: exit, search, quit, Inv, Compass. "))
        #when u exit ur back in the hallway so that it can ask u to go to different room
        if actions == "exit":
            player_location = 'hallway'
            hallwayActions()
        elif actions == "quit":
            quit_game()
        elif actions == "search":
            #u cant search things twice, and if you already have something in inventory, it skips and item drops another thing
            if "flashlight" not in Inventory:
                item_drop("flashlight")
            elif "bandages" not in Inventory:
                item_drop("bandages")
            elif "energy bar" not in Inventory:
                item_drop("energy bar")
            #if u have all items, it will print this text
            else:
                print("You have already searched this area.")
        #other actions
        elif actions == "Inv":
            showInventory()
        elif actions == "Compass":
            Compass()
        else:#if u didnt write anything in the list of actions u will get this text
            print(error_text("I do not understand that command."))

def ControlRoomActions():
    global player_location
    #if you have the flashlight, which is obtained in the impatient ward, then you can go to the control room
    if "flashlight" in Inventory:
        ControlRoomPart2()
        player_location = "control room"
        #spawned random entity from def
        entity_spawn()
        while player_location == "control room":
            actions = input(main_story("Actions: exit, search, quit, Inv, Compass. "))
            if actions == "exit":
                player_location = 'hallway'
                hallwayActions()
            elif actions == "search":
                #different items
                if "canned fish" not in Inventory:
                    item_drop("canned fish")
                elif "storageroomkey" not in Inventory:
                    item_drop("storageroomkey")
                elif "energy bar" not in Inventory:
                    item_drop("energy bar")
                else:
                    print("You have already searched this area.")
                
            elif actions == "quit":
                quit_game()
            elif actions == "Inv":
                showInventory()
            elif actions == "Compass":
                Compass()
    else:
        #if you dont have flashlight ur location is back at hallway, it will tell you that you dont have the light and need to get it first before u can go into the control room.
        ControlRoomPart1()
        player_location = "hallway"
        hallwayActions()

def EmergencyRoomActions():
    global player_location
    player_location = "emergency room"
    entity_spawn()
    while player_location == "emergency room":
        actions = input(main_story("Actions: exit, search, quit, Inv, Compass. "))
        if actions == "exit":
            player_location = 'hallway'
            hallwayActions()
        elif actions == "search":
            if "antiseptic" not in Inventory:
                item_drop("antiseptic")
            elif "water" not in Inventory:
                item_drop("water")
            else:
                print("You have already searched this area.")
        elif actions == "quit":
            quit_game()
        elif actions == "Inv":
            showInventory()
        elif actions == "Compass":
            Compass()
        
            

def StorageRoomActions():
    global player_location
    #again you need the key to go into the storage room
    if "storageroomkey" in Inventory:
        StorageRoomP2()
        
        player_location = "storage"
        while player_location == "storage":
            actions = input(main_story("Actions: exit, search, quit, Inv, Compass. "))
            if actions == "exit":
                player_location = 'hallway'
                hallwayActions()
            elif actions == "search":
                if"bread" not in Inventory:
                    item_drop("bread")
                else:
                    if "bread" in Inventory:
                        print("You have already searched this area.")
            
            elif actions == "quit":
                quit_game()
            elif actions == "Inv":
                showInventory()
            elif actions == "Compass":
                Compass()
            else:
                print(error_text("I do not understand that command."))
    else:
        #back at hallway if u dont have the key, prints the rooms again for you to find the key
        StorageRoom()
        player_location = "hallway"
        hallwayActions()
            
    
#the narrative
def welcomeScene():
    cls()
    print("Welcome to the game.")
    time.sleep(1)
    print('Prologue.')
    time.sleep(1)
    sceneOne()
    time.sleep(1)
    sceneOneP2()
    time.sleep(1)
    sceneTwo()
    time.sleep(4)
    input('Press Enter to start the game.')

#Start the game
print("Compass for clues, Default health is 5")
welcomeScene()
hallwayActions()

