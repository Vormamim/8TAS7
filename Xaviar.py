#import libraries
import os
import sys
import random
import emojis
import time
from yachalk import chalk
#variables

gameOver = False
actionWords = [
    'take', 'inventory', 'use', 'look', 'help', 'quit', 'move', 'talk', 'fight', 'hint'
]
playerInventory = []
locations = [
    [
        'Your house', 'A small wood-brick house of your very own.',
    ],
    [
        'Market District',
        'Normally a bustling area of commerce, however there are only 2 shops left...',

    ], ['Church'],
    [
        'Blacksmith',
        "The blacksmith makes weapons and armor for the soldiers"
    ], ['Stable', 'The stable has horses for hire'],
    ['Merchant', 'The merchant sells exotic goods with a high markup to the \ntownspeople...that dalcop'],
    [
        'Shipwright',
        'The shipwright builds and looks after the villages ships.',
    ],
    [
        'Barracks',
        'The barracks house the garrison of soldiers ordered to protect the village.'
    ]
]
horseItems = False
fightingGear = False
shipEscapeGear = False
gettingMary = False

#Npc conditions
wifeNpcTalkedTo = False

#colours
outputText = chalk.green_bright
errorText = chalk.red
celebrationText = chalk.cyan_bright
helpText = chalk.magenta
storyText = chalk.yellow_bright

#First time conditions for the story
houseFirstTime = True
marketFirstTime = True
shipwrightFirstTime = True
barracksFirstTime = True
stablesFirstTime = True
blacksmithFirstTime = True
merchantFirstTime = True
shipwrightFirstTime = True
gotMary = False
maryAtChurch = False

#define functions

#Help function is for getting all the controls while in the game
def help():
  print(helpText("Help: Get controls"))
  print(helpText("take: take an item"))
  print(helpText("inventory: check inventory"))
  print(helpText("look: look around"))
  print(helpText("quit: quit the game"))
  print(helpText("move (direction): move to another place"))
  print(helpText("talk: talk to someone"))
  print(helpText("fight: fight with someone"))
  print(helpText("hint: get a hint"))

#Clear screen can make the viewing experience better for the user
def clearScreen():
  os.system('cls' if os.name == 'nt' else 'clear')

#Animate text can make text look better
def animateText(text, delay=0.01):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()

#Display location prints the area you are in, where the exits are, and a brief description of the place.
def displayLocation(locationName):
  if locationName == locations[0][0]:
    print(outputText(f"You are at {locations[0][0]}: {locations[0][1]}"))
    print(outputText("Exits: West, Southwest, South"))
    return
  if locationName == locations[1][0]:
    print(outputText(f"You are at {locations[1][0]}: {locations[1][1]}"))
    print(
        outputText(
            "Exits: East, West, South, Southeast, To the blacksmith, To the merchant"
        ))
    return
  if locationName == locations[3][0]:
    print(outputText(f"You are at {locations[3][0]}: {locations[3][1]}"))
    print(outputText("Exits: Market district"))
  if locationName == locations[4][0]:
    print(outputText(f"You are at {locations[4][0]}: {locations[4][1]}"))
    print(outputText("Exits: East, Southeast"))
  if locationName == locations[5][0]:
    print(outputText(f"You are at {locations[5][0]}: {locations[5][1]}"))
    print(outputText("Exits: Market district"))
  if locationName == locations[6][0]:
    print(outputText(f"You are at {locations[6][0]}: {locations[6][1]}"))
    print(outputText("Exits: North, Northwest"))
  if locationName == locations[7][0]:
    print(outputText(f"You are at {locations[7][0]}: {locations[7][1]}"))
    print(outputText("Exits: Northeast, South, Northwest"))


def basicFunctions():
  if action == 'help':
      help()
      return True
  elif action == 'inventory':
      displayInventory()
      return True
  elif action == 'quit':
      sys.exit()
  elif action == 'look':
      displayLocation(currentLocation)  # Add currentLocation tracking
      return True
  return False


def displayInventory():
  print(outputText('Inventory: ' + ', '.join(playerInventory)))


#Npc functions


def wifeNpc():
  talkingToWife = True
  wifeNpcTalkedTo = True
  maryChoice = input("(should you let mary go pray at the church?)")
  if maryChoice == 'yes':
      animateText(storyText("""Sure, go and pray, it'll keep our minds off things for the \ntime being. Stay safe sweetheart.") 
      she notices your voice waver. \nHere, take my bracelet. "I'll be fine, trust me." Mary says, taking her cross and giving you a quick peck on the cheek before \nturning out the door.
      "Stay safe." you whisper. The bracelet smells faintly of sweet lavender and beautifully half-tuned perfumes."""))
      playerInventory.append('Bracelet')
      maryAtChurch = True
  elif maryChoice == 'no':
      animateText(storyText("""
"Mary. Stay here, I beg of you. It will be safer here. I need to go and find out what's happening." 
Mary opens her mouth to say something, but hesitates, closing it shut. She looks down and back up at you, her eyes glazed with \nsilent tears. 
"Very well. Stay safe sweetheart" 
"Yeah yeah don't worry about me. Shouldn't be anything much"

You leave the house. Outside you can clearly hear sounds of a \nclash and screams erupting from around the docks and shipyard.\nA warm orange glow radiates from the general direction, no doubt the sign of a raging inferno. You decide to go check it out.\nWalking down the street you are greeted with familiar faces, all of whom are plated with expressions of shock and fear.\nOne of the faces in an old pal, Baxter. 

"Bax! D'you have any idea what's goin' on?!", you ask, grabbing your mate. 

"Save your soul, Arthur! Northmen have landed by the shipyard \nand have set the whole \nplace on fire. They've already begun looting the other housing \nblock. Run, I implore you old friend!" He responds, quickly \nrunning off. 

You run home to Mary and explain the situation to her. She holds a hand to her mouth, a gasp escaping her lips. She listens intently and asks a few little questions here and there. 

"But what should we do now? How are we going to escape?" 

You rub your temples. 

"Not 'we' Mary, 'me'. It's too dangerous for you to be running around with me looking for a way to escape that might not even exist!

"But.." 

"I won't be hearing it. I'm sorry honey, it's for your safety. The cellar has some supplies and a spear you can use to defend yourself if needed. Pray you, stay at home for goodness sake." you beg. 

Mary hangs her head in silent acceptance. You move forward and give her a warm, intimate hug. 

"I'll come back for you, my love. I promise it"  

The embrace lasts an eternity, and you are eventually forced to tear yourself from her love. Before leaving out the door she gives you a small item. 

"It's that stupid bracelet you gave me on our first date" she says, smiling as she hands it over to you. 

You grin softly as she places it in the palm of your hand, drawing an imaginary love heart around it and then closing your fingers around the precious artefact. 

"Stay safe, love" she tearfully says, her voice wavering. 
"""))
      animateText(celebrationText())
      playerInventory.append('Bracelet')
      maryAtChurch = False
  else:
      animateText("That isn't a very clear answer.")
      wifeNpc()  # Recursively ask again for valid input

#Scene functions

#The house is the starting scene, it has the wife npc which can give you a bracelet, and if you enter the house again with the bracelet you can get the reigns.

# The backdash n (\n) prints it on a new line to prevent words being printed on separate lines
def house():
  clearScreen()
  global houseFirstTime
  if houseFirstTime:
  
        animateText(
            storyText(
                """Your eyes open drearily as you are shaken awake violently by the \nsweaty hands of your wife, through your drowsy eyes you see her \ncontorted face filled with fear and anguish. You sit \nup from your hard straw bed in your modest house made of cold \ngrey stone.
                
Her face looks unnatural, a strange flickering light appears \nfrom behind the wooden door which faces towards the shipyard. \nPerhaps another work accident, \nor it could’ve been the neighbour's horse knocking over another lantern in his pen again. 

\n“Arthur, wake up!” she stutters, sweat dripping from her golden hair. “Something’s happening- i'm not sure what but i've been \nhearing screams and shouts and..and-” 
“Calm down honey, sweet jesus. I'll go out and investigate. Stay here, I pray you.” 
“I want to go pray, love. At the church. Please, \nfor our safety.”
"""            ))
        wifeNpc()
  if not houseFirstTime:
    global gettingMary
    if gettingMary:
      global gotMary
      gotMary = True
      print("Mary at the house story")
  if not houseFirstTime and 'Bracelet' in playerInventory:
    animateText(storyText("Your neighbour is exiting his house, evidently \nanxious to escape. He says to you, 'I have a spare pair of reigns, \nbut i'm not parting with them for free..."))

    neighbourReigns = input("Do you want to give him the bracelet in return for the \nreigns?")
    if neighbourReigns == 'yes':
      playerInventory.remove('Bracelet')
      playerInventory.append('Reigns')
    if neighbourReigns == 'no': 
      animateText("Suit yourself") 
  houseFirstTime = False
  while True:
    displayLocation('Your house')
    global action
    action = input("What do you want to do or where do you want to go? (market, \nbarracks, shipwright)")
    basicFunctions()
    if action == 'market':
      marketDistrict()
    elif action == 'barracks':
      barracks()
    elif action == 'shipwright':
      shipwright()
    else:
      print("That command doesn't exist")

def church():
  pass

#The market district is the first place you can go to that you can do things in. You can choose either the blacksmith or the merchant, and they give you the items necessary for the 3 endings, you can only choose one though. The three endings are fighting the vikings, escaping by boat or escaping by horse.

def marketDistrict():
  clearScreen()
  global marketFirstTime
  if marketFirstTime:
      animateText(
          storyText(
                "You made it to the market district. You see many people screaming and \nrunning around. Many shops are on fire, but the blacksmith and the \nmerchant's stalls are still there, however the shopkeepers have fled. \nPerhaps you could 'borrow' something?"
            ))
      marketFirstTime = False
  while True:
    displayLocation('Market District')
    global action
    action = input("What do you want to do or where do you want to go? (house, \nshipwright, barracks, stables, merchant, blacksmith)")

    
    basicFunctions()
    if action == 'house':
      house()
    if action == 'shipwright':
      shipwright()
    if action == 'barracks':
      barracks()
    if action == 'stables':
      stables()
  
    if action == 'merchant' and 'Sword' not in playerInventory:
      merchant()
    if action == 'merchant' and 'Sword' in playerInventory:
      clearScreen()
      print("You shouldn't go to the merchant. You are already carrying a heavy items.")
    if action == 'blacksmith' and 'Oars' or 'Saddle' in playerInventory:
      clearScreen()
      print(outputText("You shouldn't go to the blacksmith. You are already carrying \nheavy items."))
    if action == 'blacksmith' and 'Oars' not in playerInventory:
      blacksmith()

#The blacksmith has a sword - you can combine it with the shield and go fight the vikings.

def blacksmith():
  clearScreen()
  global barracksFirstTime
  if barracksFirstTime:
    animateText(storyText('The blacksmith has left to fight the vikings with \nthe rest of the soldiers. On the table there is a simple \nunadorned sword.'))
    barracksFirstTime = False
  displayLocation('Blacksmith')
  global action
  action = input("What do you want to do? (barracks, house, take (sword)")
  basicFunctions()
  if action == 'house':
    house()
  elif action == 'barracks':
    barracks()
  if action == 'take':
    clearScreen()
    print("You took the sword. A nice basic infantryman's blade.its pretty heavy so dont think about taking anything else from the market, you greedy fool. Maybe you can find a use for it!")
    playerInventory.append('Sword')

#The merchant has the saddle for escaping by horse, and the oars for escaping by boat.

def merchant():
  clearScreen()
  global merchantFirstTime
  if merchantFirstTime:
      animateText(storyText("The merchant has escaped the town with his high value \ngoods. On the table he left behind some oars, and a saddle. They \nare very heavy, so you can only take one."))
  else:
      displayLocation('Merchant')
  global action
  action = input("What do you want to do?")
  basicFunctions()
  if action == 'take':
      whatToTake = input("Would you like to take the oars or the saddle?")
      if whatToTake == 'saddle':
          playerInventory.append('Saddle')
          clearScreen()
          print(outputText("You took the saddle. You notice its only able to carry a single person. \nMaybe you can find a way to escape with \nit?"))
      if whatToTake == 'oars':
          clearScreen()
          playerInventory.append('Oars')
          print("You took the oars. Maybe you can find a use for them!")
          global shipEscapeGear
          shipEscapeGear = True

#The stables have a horse that you need the reigns and the saddle to escape.

def stables():
  global stablesFirstTime  # Add at start of function
  clearScreen()  
  if stablesFirstTime:
    animateText(storyText("As you get to the stable, most of the horses have \nalready departed. A man is sitting on his horse, about to leave. \nHe says to you, 'I have a spare horse for you if you intend to \nleave. But you need both some reigns and a saddle.'"))
  while True:
    displayLocation('Stables')
    global horseItems
    global action
    if 'Reigns' and 'Saddle' in playerInventory:
      horseItems = True
    action = input("What do you want to do or where do you want to go? (market, escape)")
    basicFunctions()
    if action == 'move east':
      marketDistrict()
    if action == 'escape' and not horseItems:
      print("You need a horse to go west. If you don't the vikings will run you down.")
    if action == 'escape' and horseItems:
      escape = input("Are you sure you want to escape? The saddle is only big enough \nfor one, you will have to leave your wife behind.")
      if escape == 'yes':
        print(celebrationText("You mount a chestnut throughbred, a strong and tall mount. Through a breach in the wall, presumably made by other citizens, you ride out into the sunset. Looking over your shoulder the city of Earlington ignites in a spectacular ember, turning the sky an eerie bright orange. You remember Mary, feeling like a complete coward for not going back for her. You have escaped, though you will never live this moment down, let along forgive yourself for the rest of your life. This is one of four endings"))
        sys.exit()

#The shipwright has the fight with the vikings if you have the fighting gear, and the escape by boat if you have the oars.

def shipwright():
    clearScreen()
    global gettingMary
    gettingMary = False
    
    displayLocation('Shipwright')
    global action
    action = input("What do you want to do or where do you want to go? (house, barracks)")
    basicFunctions()
    if action.startswith('move') and not gettingMary:
      clearScreen()
      animateText(outputText("On the way back, you encountered a roving band of vikings. \nThey charge towards you and cut you down."))
      sys.exit()
    if action == 'house':
      house()
    if action == 'barracks':
      barracks()
    if action == 'use':
      useFightingGear = input(
          'Do you want to use the fighting gear to fight the vikings?')
      if useFightingGear == 'yes' and fightingGear:
        clearScreen()
        print(
            animateText(
                storyText(
                    'You are outnumbered, but you take down viking after viking as you \nslowly push your way towards the boats. You break through the chaos \nand bloodlust of the invaders and make it through to the \nboats.'
                )))
        escape = input("Do you want to escape? You can also choose to go back for your \nwife")
        gettingMary = True
        if escape == 'yes' and not gotMary:
          print(celebrationText(animateText("You escaped Earlington, albiet without your \nwife. You look back at the burning city, what was once a bustling \ntrade centre has been reduced to nothing but rubble and flame. \nYou call out for your sweetheart but recieve no answer among the \ncackling of fire and grand collapse of buildings. You bury your \nface into your hands and weep amonst other terrified refugees, \nthough no one pays you any attention. \nThis is one of four endings.")))
          sys.exit()
        if escape == 'yes' and gotMary:
          animateText(celebrationText("You barely make it to the boat, arrows whistle past you and your \nwife as you clamber into it. Other terrified citizens help \nyou aboard as soldiers fire back with their bows, striking deadly \ninto the hearts of the invaders. the boat pushes off and you and your \nwife embrace eachother in an intimate hug that lasts for a \nlifetime. \nThe other refugees huddled in the boat dont pay you any attention, \nas if that is the least of your concerns. \nThis is one of four endings."))
          sys.exit()

#The barracks have a shield to complete the fighting gear set, then you can go south to fight vikings and escape.

def barracks():
  clearScreen()
  while True:
    global barracksFirstTime
    if barracksFirstTime:
      if 'Sword' not in playerInventory:
        print(
            animateText(
                storyText(
                    "You make your way to the barracks. From the outside you can hear a mass clamouring of men. \nYou take a peek inside the barracks and see the garrison soldiers \ngearing up to go fight. Men gather around each other offering solemn prayers as others sit in silence. Perhaps you could get a sword to protect yourself with? "
                )))
      if 'Sword' in playerInventory:
        print(
            animateText(
                storyText(
                    "As you get near the barracks, a flood of armed people rush out, \none of them says: 'Hey lad, we have invaders to repel. Take this \nshield, it looks like you have a sword, come and help us down \nat the shipwright!' "
                )))
      barracksFirstTime = False
      global fightingGear
      fightingGear = True
    displayLocation('Barracks')
    playerInventory.append('Shield')
    global action
    action = input("What do you want to do? (shipwright, house, or market)")
    basicFunctions()
    if action == 'shipwright':
      shipwright()
    if action == 'house':
      animateText(outputText("On the way back, you encountered a roving band of vikings. \nThey charge towards you and cut you down."))
      sys.exit()
    if action == 'market':
      marketDistrict()
      


#Main game loop:
if not gameOver:
  house()

#Add after existing variables section
gotMary = False 
stablesFirstTime = True
maryAtChurch = False

# Add at top with other variables
currentLocation = locations[0][0]  # Start at house

# Update in movement functions
def house():
    global currentLocation
    currentLocation = locations[0][0]
