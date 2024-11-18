import random
import time
import sys
import os

# Map system
Grid_width = 5
Grid_height = 5
Grid = [["in the Town", "in the Town", "in the Mansion", "in the Town", "Ocean"],
        ["in the Town", "in the Town", "in the Town Square", "in the Town", "Ocean"],
        ["at the Shops", "in the Town", "in the Town", "in the Town", "Ocean"],
        ["at the Archaeologist", "at the Beach", "at the Beach","at the Port", "Ocean"],
        ["Ocean", "Ocean", "Ocean", "Ocean", "Ocean"]]

# Player starting position
Player_x, Player_y = 3, 0

# Minigame variables
done_minigame_1 = 0

# to see if you have seen the shopkeeper when going back to the beach for money
asked_shopkeeper = False

# Minigame list
words = ["sand", "shovel", "river", "digging", "bones"]
words2 = ["money", "sand", "ground", "bones", "beach"]

# Permanent items
perm_inv = ["map"]

# Player Map position

# Inventory
inv = []

# incase of loss
fail = True

# Grabbable items for scenes
grabbable_items = []

# Interactable npcs in area
interactable_npcs = []

# Variable for shopkeeper dialogue
asked_Scientist = False


# Function for clearing the screen
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# Movement Function
def Player_Move(Direction):
  global Player_x, Player_y
  
  if Direction == "north" and Player_x > 0:
    Player_x -= 1

  elif Direction == "south" and Player_x < Grid_height - 2:
    Player_x += 1

  elif Direction == "east" and Player_y > 0:
    Player_y -= 1

  elif Direction == "west" and Player_y < Grid_width - 2:
    Player_y += 1
  else:
    print("That's invalid")

# Function for checking if there are valid interactions
def Interact():
  # Interactable npcs in area
  interactable_npcs = []
  if Player_x == 3 and Player_y == 0:
    interactable_npcs.append("Archaeologist")
  elif Player_x == 0 and Player_y == 2:
    interactable_npcs.append("Scientist")
  elif Player_x == 2 and Player_y == 0:
    interactable_npcs.append("Shopkeeper")
  elif Player_x == 3 and Player_y == 3:
    interactable_npcs.append("Fisherman")
  else:
    interactable_npcs.clear()
  print(interactable_npcs)
  NPC = input("Who would you like to interact with?\n")
  if NPC in interactable_npcs:
    if NPC == "Archaeologist":
      Scene_1_Beach()
    elif NPC == "Scientist":
      Scene_2_Manor()
    elif NPC == "Shopkeeper":
      Scene_2_and_a_half_Shop()
    elif NPC == "Fisherman":
      Scene_3_Docks()
    else:
      pass #work on these later
  else:
    print("There is nobody like that here.")


# Function for using items
def Inventory_Use(Item):
    if Item in inv or perm_inv:
      if Item == "map":
        print(f"You are at {Player_x , Player_y} [y and x axis swapped and inverted btw]")
        print("Key: B = Beach, T = Town, M = Mansion, S = Shop, P = Port, O = Ocean, TS = Town Square, Archaeologist = A\n[T][T][M][T][O]\n[T][T][TS][T][O]\n[S][T][T][T][O]\n[A][B][B][P][O]\n[O][O][O][O][O]")
      elif Item in inv:
        print(f"You used the {Item}")
        inv.remove(Item)
      elif Item in perm_inv:
        print(f"You use the {Item}")
      else:
        print(f"You do not have that")

# Function for adding items to your inventory
def Inventory_Grab():
  Item = input("What would you like to grab?\n")
  if Item in grabbable_items:
    inv.append(Item)
    print(f"You added the {Item} to your inventory")
  else:
    print("There's nothing here to grab.")
# Function for opening inventory
def Inventory_Open():
    print("Inventory:")
    for item in inv or perm_inv:
      print(item)
# scene 1 minigame
def Scene_1_Beach(): # Scene one, at the beach
  num = 1 # for the minigame
  global done_minigame_1
  global asked_shopkeeper
  if done_minigame_1 == 1:
    if asked_shopkeeper == True:
       print('Why are you back here? Scram!')
       time.sleep(1)
       print("I need money, can I get some here?")
       time.sleep(1)
       print("I mean... I guess I'd give you some if you dig up something nice...")
       time.sleep(3)
       clear_screen()
       while num in range(0, 11): #typing game part 2
         randomt = random.choice(words2)
         clear_screen()
         print(f'{str(num)}/10 finished.')
         print(randomt)
         sand_challengetext = input('Re-type this word in!: ')
         if sand_challengetext.lower() == randomt:
           print("Correct!")
           print()
           num+=1
           time.sleep(1)
         elif sand_challengetext.lower() == "skippit": #skipping for testing
           done_minigame_1 = 1
           break
         else:
           print('Incorrect!')
           print()
           time.sleep(1)
       print("You've won. Here's my pocket change. I hope it's enough for you.")  
       inv.append("coin")
    else:
      print("Why are you back here? Scram!")
  else:
    print("Hello young one, what purpose do you have on this fine day? You see him holding bones, oddly similar to yours... It is yours! He has your rib cage!")
    time.sleep(5)
    print()
    print("Hey! Give my bo-costume back! \n\nNow that's not very polite. Be nice and maybe I'll help you.")
    time.sleep(3)
    while True:
      user_input = input("What do you do? \n1. Ask him nicely. Say 'please'. \n2. He's stolen your ribs! Say 'give that back'.\n ") #input action
      if user_input == "please":
        print("Alright then. Play my game and I'll give it to you! I'm gonna bury the bone and you'll have to dig it up! \n\nWhile it's nothing to be excited about, finding your ribcage is rather important. You'll play the game.")
        time.sleep(5) 
        clear_screen()
        while num in range(0, 11): #typing game
          randomt = random.choice(words)
          clear_screen()
          print(f'{str(num)}/10 finished.')
          print(randomt)
          sand_challengetext = input('Re-type this word in!: ')
          if sand_challengetext.lower() == randomt:
            print("Correct!")
            print()
            num+=1
            time.sleep(1)
          elif sand_challengetext.lower() == "skippit": #skipping for testing
            done_minigame_1 = 1
            break
          else:
            print('Incorrect!')
            print()
            time.sleep(1)
        print("Alright... you beat me! You get your ribs. And I'll give you some information; there's a manor up the path from here, it's great and white marble, you can't miss it. My scientist buddy is in there, he might know where one of your legs are.")
        time.sleep(5)
        perm_inv.append("Ribcage") # Success
        done_minigame_1 = 1
        fail = False
        time.sleep(1)
        print()
        break
      elif user_input == "give that back": # Wrong choice
        print('The mysterious archaeologist picks you up angrily before kicking you far away into the water. Great job. You lost.')
        fail = True
        break
      else:
        print("What? Input 'please' or 'give that back'") # Uncomputable choice

def Scene_2_Manor(): # scene 2, at a manor
  user_input = '' #to get user input
  global has_sandpaper
  global asked_Scientist
  if "Sandpaper" in inv:
    print("Thanks a lot! You can come in now.")
    time.sleep(2)
    print("As you walk through the grand door, you are met with an ever more marvellous room. Walls are lined with displays of bones, ranging from everyday animals to those you've never heard of. I guess he really is a collector.")
    time.sleep(4)
    print("Oh, and here's your left leg. It might be a bit cleaner than others, but you'll dirty it with time.")
    perm_inv.append("Left Leg")
    time.sleep(4)
    print("Suddenly, you fall through the floor. The old floorboards you were standing on must've given out.")
    time.sleep(3)
    print("'Are you okay?' cries a voice from the manor above.")
    
    Hub_3_Cave()
  else:
    print("Reason for entry? Why are you here?")
    print("I was told by an archaeologist that my stolen bone... costume was here. He said a scientist had it.")
    time.sleep(2)
    print("No. No way. I told that stupid man to never contact me again. Go away. Go.")
    time.sleep(2)
    print("Please let me in! I'll do something for you! Whatever you want.")
    time.sleep(2)
    print("Well... I did need some sand paper to smooth down my bone collection. If you get me some, I'll let you in.")
    user_input = input("Well... you really need that bone. Will you do it? \nSay 'yes' \nSay 'no'")
    while True:
      if user_input == 'yes':
        asked_Scientist = True
        print("Splendid, I'll be waiting.")
        break
      elif user_input == 'no':
        print("You're not going to do it? I'm not going to let you in. Go away.")
        break
      else:
        print("Input a correct choice. 'yes' or 'no'.")
  

def Hub_1_TownSquare(): # hub for scenes
  print("You enter the town square; it's not the biggest town, but it's humble and open. People are hanging laundry, bartering with merchants, but they don't notice you're a skeleton. Somehow.")
  time.sleep(5)
  print()
  print("You see a large manor north of you, a smaller dirt path heading to a corner bend you can't see past on the west, and a pathway with a shop to the east that emits a smell of dust and wood. You could also go south to the beach where you already were. \nWhere do you do?")
  time.sleep(5)

def Hub_2_Left_Path():
  print("You walk to the left and see a wooden dock coming off of the path to the south. There's a man fishing at the end of it. Nothing else comes to note, except the path back to the east.")
  time.sleep(2)
  Action()

def Scene_3_Docks():
  if asked_shopkeeper == True: 
    print("Hello.")
    Hub_2_Left_Path()
  else:
      print("Can I have some money? \nI don't have any, but I bet that rich Archaeologist over there's got some. Go ask 'im.")
      Hub_2_Left_Path()

def Hub_3_Cave():
  user_input = ''
  print("Water drips from the ceiling in such a damp, dark cave. There's two paths from here, forward and to the west. Where should you go?")
  while True:
    user_input = input("You can go 'forward' or 'left'. ")
    if user_input == 'left':
      Cave_Path_Left()
      break
    elif user_input == 'forward':
      Scene_4_Cave()
      break
    else:
      print("Do 'forward' or 'left'. ")

def Cave_Path_Left():
  user_input = '' #user input
  print("You walk into the corridor and end up in a tight squeeze. You can't see past it; it's hard to see already, so you might have to go back.")
  user_input = input("What do you do? Say 'go back' or say 'go forward. ")
  if user_input == 'go forward':
    print("It was a tight squeeze, but you made it through. The haze of the dirt you kicked up while crawling shrouds your vision, but you eventually realise you're at a dead end. Then something grabs your eye; a bone. You pick up the leg bone, and being able to walk again is a relief.")
    time.sleep(5)
    perm_inv.append("Right Leg")
    Hub_3_Cave()
  elif user_input == 'go back':
    print("You turn back. That path could've been dangerous, after all. But the mystery still allures you.")
    Hub_3_Cave()
  else:
    print("You can't make up your mind, so you end up going back. Better safe then sorry.")
    Hub_3_Cave()

def fight():  # the awesome robot fight scene
  player_health = 100
  robot_health = 100
  num = 1
  player_attack = ''
  block = False
  while player_health > 0 and robot_health > 0:
    while num in range(1, 3):
      while True:
        num = random.randint(1, 3)
        if num == 1 and block == False:
          player_health -= 5
          print("The robot hit you, but you blocked most of the force.")
        elif num == 2 and block == False:
          print("The robot hit you, but you parried the attack.")
        elif block == False:
          player_health -= 10
          print("The robot hit you and you failed to counter it.")
        elif block == True and num == 1 or num == 2:
          print("The robot hit you but you blocked it.")
          block = False
        else:
          print("You blocked the robot's attack and countered.")
          block = False
          robot_health -= 10
        player_attack = input("Do you attack or block? Say 'a' or 'b'.")
        if player_attack == 'a':
          num = random.randint(1, 3)
          if num == 1 or num == 2:
            print("You hit the robot.")
            robot_health -= 10
          else:
            print("The robot evaded your attack.")
        elif player_attack == 'b':
          print("You'll block your next move.")
          block = True
        else:
          print("Say 'a' for attack or 'b' for block.")
        if player_health <= 0:
          print("You died.")
          break
        elif robot_health <= 0:
          with open("fight.txt") as f:
            text = f.read()
          print(text)
          break


def Scene_4_Cave():  #mainly just story
  if "Right Leg" in perm_inv:
    print("You continue down into the cave where you meet a large, open chasm. Stalactites hang from the ceiling and drip water to a place too dark to see. You continue walking.")
    time.sleep(3)
    print("As you walk you hear mechanical noises... and as you turn the corner, a large robot comes into your vision. It's metallic grey, with a top-heavy build. And how typical; it has your right arm.")
    time.sleep(3)
    print("You walk closer as it looks at you directly, raising its fist. Definitely not friendly.")
    time.sleep(2)
    clear_screen()
    fight()
  else:
    print("You feel as if you should turn back.")
    time.sleep(1)
    Hub_3_Cave()

def Scene_2_and_a_half_Shop(): # the dreadful shop
  global asked_Scientist
  global asked_shopkeeper
  print("'Well? What do you want?'")
  time.sleep(1)
  if "coin" in inv and asked_Scientist == True:
    #pays
    print("Here's your sandpaper.")
    inv.append("Sandpaper")
    inv.remove("coin")
    Hub_1_TownSquare()
  elif asked_Scientist == True:
    #asks for sand paper, has no money for it, does minigame.
# Function for actions
    print("You can't buy anything without money. Maybe if you worked more than once like that Archaeologist over there, maybe you could've brought in a pretty penny")
    asked_shopkeeper = True
  else: 
    print("You don't even know what you're getting. Get out of my shop.")


    

# Intro text
with open("intro.txt") as f:
  Intro = f.read()
while True:
  print(Intro)
  time.sleep(10)
  clear_screen()
  print("Getting out of the sand was hard, just being a head and all.")
  time.sleep(2)
  print()
  break



while True:
  if Player_x == 0 and Player_y == 2:
    print("You walk towards the giant door, about twice your height. The building looks like a Roman palace mixed with a modern house. And as you approach, a man suddenly appears. He's wearing a lab coat, possibly a scientist of some sort?")
    time.sleep(3)
    print()
    print()
    # Had to completely get rid of our Action function and exchange it for the stuff below in order for the quit to work
    Action = input("Here is a list of commands:\ninv, grab, move, interact, quit. \nWhat would you like to do? \n")
    if Action == "inv":
      Inventory_Open()
      Item = input("What would you like to use? \n")
      if Item in inv or perm_inv:
        Inventory_Use(Item)

    elif Action == "grab":
      Inventory_Grab() #me thinks this is right - Caelan

    elif Action == "move":
      Direction = input("Move 'north', 'east', 'south', or 'west'?\n ")
      Player_Move(Direction)

    elif Action == "interact":
      Interact()

    elif Action == "quit":
      print("Ok, thanks for Playing!")
      break

    else:
      print('That is not a valid command.')
  elif Player_x == 2 and Player_y == 0:
    print("You enter the shop. It's humble and small, despite being stocked to the walls with books, food, devices, and other items. The shop keeper seems friendly.")
    time.sleep(2)
    print()
    Action = input("Here is a list of commands:\ninv, grab, move, interact, quit. \nWhat would you like to do? \n")
    if Action == "inv":
      Inventory_Open()
      Item = input("What would you like to use? \n")
      if Item in inv or perm_inv:
        Inventory_Use(Item)

    elif Action == "grab":
      Inventory_Grab() #me thinks this is right - Caelan

    elif Action == "move":
      Direction = input("Move 'north', 'east', 'south', or 'west'?\n ")
      Player_Move(Direction)

    elif Action == "interact":
      Interact()

    elif Action == "quit":
      print("Ok, thanks for Playing!")
      break

    else:
      print('That is not a valid command.')
  elif Player_x == 3 and Player_y == 3:
    print("You walk up to the port. You see the old man that the shop keeper told you about. He is busy fishing.")
    print()
    Action = input("Here is a list of commands:\ninv, grab, move, interact, quit. \nWhat would you like to do? \n")
    if Action == "inv":
      Inventory_Open()
      Item = input("What would you like to use? \n")
      if Item in inv or perm_inv:
        Inventory_Use(Item)

    elif Action == "grab":
      Inventory_Grab() #me thinks this is right - Caelan

    elif Action == "move":
      Direction = input("Move 'north', 'east', 'south', or 'west'?\n ")
      Player_Move(Direction)

    elif Action == "interact":
      Interact()

    elif Action == "quit":
      print("Ok, thanks for Playing!")
      break

    else:
      print('That is not a valid command.')
  elif Player_x == 1 and Player_y == 2:
    Hub_1_TownSquare()
    print()
    Action = input("Here is a list of commands:\ninv, grab, move, interact, quit. \nWhat would you like to do? \n")
    if Action == "inv":
      Inventory_Open()
      Item = input("What would you like to use? \n")
      if Item in inv or perm_inv:
        Inventory_Use(Item)

    elif Action == "grab":
      Inventory_Grab() #me thinks this is right - Caelan

    elif Action == "move":
      Direction = input("Move 'north', 'east', 'south', or 'west'?\n ")
      Player_Move(Direction)

    elif Action == "interact":
      Interact()

    elif Action == "quit":
      print("Ok, thanks for Playing!")
      break

    else:
      print('That is not a valid command.')
  elif Player_x == 3 and Player_y == 0:
    print("As you climb out onto the beach you see a weird looking archaeologist, in a stereotypical outfit, brimmed hat with a chin strap and all. His face is shrouded in shadow. You see your house boat at the docks, but there's no reason to go back.")
    print()
    Action = input("Here is a list of commands:\ninv, grab, move, interact, quit. \nWhat would you like to do? \n")
    if Action == "inv":
      Inventory_Open()
      Item = input("What would you like to use? \n")
      if Item in inv or perm_inv:
        Inventory_Use(Item)

    elif Action == "grab":
      Inventory_Grab() #me thinks this is right - Caelan

    elif Action == "move":
      Direction = input("Move 'north', 'east', 'south', or 'west'?\n ")
      Player_Move(Direction)

    elif Action == "interact":
      Interact()

    elif Action == "quit":
      print("Ok, thanks for Playing!")
      break

    else:
      print('That is not a valid command.')
  else:
    print()
    Action = input("Here is a list of commands:\ninv, grab, move, interact, quit. \nWhat would you like to do? \n")
    if Action == "inv":
      Inventory_Open()
      Item = input("What would you like to use? \n")
      if Item in inv or perm_inv:
        Inventory_Use(Item)

    elif Action == "grab":
      Inventory_Grab() #me thinks this is right - Caelan

    elif Action == "move":
      Direction = input("Move 'north', 'east', 'south', or 'west'?\n ")
      Player_Move(Direction)

    elif Action == "interact":
      Interact()

    elif Action == "quit":
      print("Ok, thanks for Playing!")
      break

    else:
      print('That is not a valid command.')


