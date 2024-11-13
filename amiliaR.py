import os
import random
import time
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
import time
import sys

def helpHint(someText):
    print('\nwelcome to the semi useful hint system')
    print('\nAll I can tell you is {someText}')

def QUIT(someText):
    print('\nWelcome to the QUIT system for losers who cant play the game')
    print('\nWell well well...you loser. Exit the console yourself dumbie..')

                                                  
def typewriter_print(text, delay=0.05):
      for char in text:
          sys.stdout.write(char)
          sys.stdout.flush()  
          time.sleep(delay) 
      print()


listforpack = ['corn', 'spaghetti', 'glasses', 'book']

# intro to the game
typewriter_print('Welcome to Barbie and the Mystery of the Lighthouse')
time.sleep(2)
clear_screen() 
time.sleep(2)
typewriter_print("You live in a quaint, seaside town, as a herboliogist tasked to transform the native flora of Malibura, (also known as Malibu, for short) into a sustainable ecosystem.")

time.sleep(4)
typewriter_print("You are lounging at your sunny home - listening to a healthy amount of One Direction and Taylor Swift when you hear a melodic knocking against your ornate oak door")
while True:
  door1game = input("Do you want to open the door?").strip().lower()
  if door1game == 'yes':
      break
  elif door1game == 'no':
      print("In order for you to play Barbie and the mystery of the lighthouse, you must say yes to this question.")
  elif door1game =='help':
      helpHint("This is the hint for this. Answer yes dumbie")
  elif door1game == 'quit':
      QUIT("You have quit the game. Please close the program")
      break
  else:
          print("Please answer 'yes' or 'no'.")
clear_screen()
time.sleep(1)
typewriter_print("- you open the door hesitantly... and with delight see the famously multi-talented celebrity Barbie.")
time.sleep(3)   
clear_screen()
typewriter_print("Barbie smiles, 'Hey! I've heard you are a really talented herbologist and I need your help...")
time.sleep(2)
clear_screen()
userName = input("Barbie chuckles awkwardly. 'And I'm sorry to ask - this is TOTALLY not girlypop of me, given that I need you to help me resore the nature of island Moord, but I forgot your name. What is it again?'").strip().lower()


clear_screen()
print("'Ahh of course your name is", userName , "It really suits you!'")
typewriter_print(""'NOW.. ahem... as I mentioned earlier, I need you to accompany me to the island Moord - where we will relieve the current lighthouse keepers. As a benefit of this arrangement you can study and rebalance the flora of Moord.')
time.sleep(1)
clear_screen()
while True:
  islandyesorno = input("Do you wish to accompany Barbie to the island Moord? ").strip().lower()
  if islandyesorno == 'yes':
      print("Barbie smiles sharply... 'Yay', she says flatly, 'Now to the island'...")
      break
  if islandyesorno == 'no':
          print("In order for you to play Barbie and the mystery of the lighthouse, you must say yes to this question.")
  if islandyesorno =='help':
        helpHint("This is the hint for this. you must go to the light house to play Barbie and the mystery of the lighthouse")
  if islandyesorno == 'quit':
      QUIT("You have quit the game. Please close the program")
      break
  else:
          print("Please answer 'yes' or 'no'.")


# scene 2 - lighthouse entry / open scen
time.sleep(4)
typewriter_print("You arrive at the island Moord via boat. The ocean is calm - the turquoise waters reflecting the fading sunlight.")
clear_screen()
typewriter_print("The sky is stained a rosy hue and few clouds can be seen. You get off the boat and take in the scenic island")

typewriter_print("As you step onto the moist sand, a mossy stone staircase unfolds before you. Attatched is a small engraved sign saying: 'watch your step, things can get slippery sometimes'. You acknowledge the sign and carefully tread up the stairs, Barbie following closely behind. After what feels like a kilometre of climbing, grassy plains stretch out before you and you see the white lighthouse infront of you that will be your new temporary home. 'There it is, Barbie!' you say excitedly, and she responds with a cheery remark. you walk your way up the brick paved path to the lighthouse and knock on the door, expecting the other keepers to be awaiting you but nobody answers...")
clear_screen()

# ask to enter lighthouse - else if or while loop ur choice
while True:
  lighthouseentry = input("Do you want to enter the lighthouse? ").strip().lower()
  if lighthouseentry == 'yes':
        typewriter_print("You swing open the door and step inside. The lighthouse is clean,perfectly dusted and empty besides the table set up before you with a candle, its wick cut and a suspiciously fat cat scratching at it. You and Barbie both call out for the lighthouse keepers but there is no response. 'That's strange', Barbie says and you nod in agreement.")
        break
  if lighthouseentry == 'no':
            typewriter_print("In order for you to play Barbie and the mystery of the lighthouse, you must say yes")
  if lighthouseentry =='help':
      helpHint("This is the hint for this. You need to want to play")
  if lighthouseentry == 'quit':
      QUIT("You have quit the game. Please close the program")
      break
  else:
          print("please answer yes or no")

typewriter_print("After filtering through the foyer, you notice a rumbling in your stomach... A glance out the window reveals that darkness has afflicted the sky. Hm. You haven't eaten since leaving for the island Moore.")
time.sleep(2)
clear_screen()
typewriter_print("Your gaze is drawn to the kitchen, where cabinets made from pine wood and an antique refridgerator are located.")
snack1kitchen = input("Do you want to eat a something? ").strip().lower()
if snack1kitchen == 'yes':
    print("Great. You move towards the kitchen before contemplating what to make.")
    snack1food = input("Do you want to make a sandwich or a salad?")
    if snack1food == 'sandwich':
        print("You gather the ingrediants for your sandwich. Surprisingly, the bread is fresh despite the lighthouse not having a shipment delivered.")
        print("You find a sharp knife in the draw... some crimson tomato juice remains tarnishing the blade. Such silly lighthouse keepers... not cleaning properly.")
        knife1 = input("Would you like to add the knife to your inventory")
        while True:
            if knife1 == 'yes':
                typewriter_print("added to inventory")
                break
            if knife1 == 'no':
                typewriter_print("You may need the knife for... future sandwich preperation. Try again.")
            if knife1 =='help':
                  helpHint("This is the hint for this. You never know when you may want to make a sandwich")
            if knife1 == 'quit':
                  QUIT("You have quit the game. Please close the program")
            else:
                print("please answer yes or no")
    
    elif snack1food == 'salad':
        while True: 
            print("You find a sharp knife in the draw... some crimson tomato juice remains tarnishing the blade. Such silly lighthouse keepers... not cleaning properly.")
            knife1 = input("Would you like to add the knife to your inventory")
            if knife1 == 'yes':
                typewriter_print("added to inventory")
                break
            elif knife1 == 'no':
                typewriter_print("You may need the knife for... future sandwich preperation. Try again.")
            elif knife1 =='help':
                  helpHint("This is the hint for this. You never know when you may want to make a sandwich")
            elif knife1 == 'quit':
                  QUIT("You have quit the game. Please close the program")
    else:
        typewriter_print('please answer salad or sandwich')
            
if snack1kitchen == 'no':
    
    while True: 
        print("Barbie comes towards you sheepishly. 'Can you make me a sandwich please? I'm ravished...'")
        sandwichforbarb = input("Would you like to make a sandwich for Barbie?")
        if sandwichforbarb == 'yes':
            typewriter_print("You make Barbie a sandwich and she smiles brightly and thanks you")
            break
        elif sandwichforbarb == 'no':
            typewriter_print("Barbie chuckles menacingly. 'I really want a sandwich - perhaps you can reconsider...'")
        elif sandwichforbarb =='help':
            helpHint("This is the hint for this. You shouldn't dissapoint Barbie")
        elif sandwichforbarb == 'quit':
            QUIT("You have quit the game. Please close the program")
        else:
            typewriter_print('please answer yes or no')
            
    typewriter_print("You  return to the kitchen to do the washing up, and see the knife you used to slice the sandwich. While washing it up, you notice that the blade looks incredibly worn...")
    while True:
        knife2 = input("Would you like to add the knife to your inventory")
        if knife2 == 'yes':
            typewriter_print("added to inventory")
            break
        elif knife2 == 'no':
            typewriter_print("You may need the knife for... future sandwich preperation. Try again.")
        elif knife2 =='help':
            helpHint("This is the hint for this. You never know when you may want to make a sandwich")
        elif knife2 == 'quit':
            QUIT("You have quit the game. Please close the program")
        else:
            typewriter_print('please answer yes or no')

    print()
    # candle with wick cut - prepared for night - on mantle - everything dusted etc
      # view fat cat 
clear_screen()
      # room else if statements 
typewriter_print("Barbie grabs your arm. 'lets go!' she smiles. She guides you to your bedroom, where you say goodnight to her and go to sleep... ")
clear_screen()
            

      #5 barbie doscovery

      # based on selected room
typewriter_print("You wake up feeling refreshed and curious since the lighthoue keepers cannot be found.")
yesornoexplore = input('Do you want to explore the lighthouse?')
if yesornoexplore == 'yes':
    lighthouseexplore = input('Barbie is yet to be awakened, and her bedroom is locked. The only areas available fpr you to explore are the light itself, or the library in your room. Where do you want to go?')

    if lighthouseexplore == 'light':
        typewriter_print("You walk up the stairs, round and round, for what feels like the average life span of the Australian woman. Upon reaching the top, you see a large red door and you swing it open. Infront of you is the light bulb that shines each night, a table with a logbook and that same obese cat from earlier. Strange it could climb all those stairs....but anyways...")
        clear_screen()
        typewriter_print("Grabbing the log book, you flick it to the last page which has the most recent entry which is weird as it's logged by barbie the day before you arrived on the island. You brush it off and assume it was just a mistake. You flick through the pages like a deck of cards, just fidgeting but a reddish brown spot on one of the pages catches your eye. You open up to that page to reveal a smear of a message reading 'BEWARE BARBARA PG. 23.' Curious, you turn to page 23 - the supply page - and underlined in that same red brown colour is the word 'Knife'. Highly suspicious, you shut the book quickly and begin trekking back down the stairs while wondering how and why that warning was there.")
        clear_screen()
#log book
    if lighthouseexplore == 'library':
        print("The library books look well loved and weathered, the scent of old books wafting through the air. You notice in the corner of your eye a book labelled 'secrets.'")
        print("You open the book and see the following words scrawled hurriedly on the page 'Do not trust Barbie' in blood")
        
    else:     
         typewriter_print("Answer 'light' or 'library'")
if yesornoexplore == 'no':
    typewriter_print('Your rumbling tummy summons you into the kitchen')
typewriter_print("You're peacefully sitting on the kitchen countertop with a grilled cheese sandwich and a womans weekly magazine in your hands. What is better than this, hey? You look up and see Barbie walking past eating a.... wait.... 'What is that?!', you asked Barbie, concerned. 'Haha. A finger' she responds dryly. Your jaw drops in horror and you lose grip on your magazine. 'Oh don't be silly I'm only kidding!', she says as you run to your room and lock the door. You're almost certain that she isn't kidding.")

if yesornoexplore =='help':
    helpHint("This is the hint for this. You must explore the lighthouse")
elif yesornoexplore == 'quit':
    QUIT("You have quit the game. Please close the program")
else:
    typewriter_print("Please answer yes or no")
    
typewriter_print("You return to your bed with an uneasy pit in your stomach... Barbie will wake soon")
knifetokill = input('Do you wish to keep the knife from the kitchen?')
while True:
    if knifetokill == 'yes':
        print("Good choice... you slip it into your pocket as you hear Barbie knocking on your door")
        break
    if knifetokill == 'no':
        print("Perhaps thou should reconsider")
        clear_screen()
    elif knifetokill == 'quit':
      QUIT("You have quit the game. Please close the program")
      break
    else:
        print('please answer yes or no')
      #confrontation
typewriter_print("Barbie opens the door, her face plastered with an eerie smile. 'So, darling I'm suspicious of your behaviour. Please answer me truthfully...'")
clear_screen()
barbieinterrogation = input("Do you know anything?")
while True:
    if barbieinterrogation == 'yes':
        typewriter_print('I see...')
        break 
    if barbieinterrogation == 'no':
        typewriter_print("I hate few things, but lying is one of them.")
        break
    if barbieinterrogation =='help':
      helpHint("This is the hint for this. You must tell Barbie yes or no")
    elif barbieinterrogation == 'quit':
        QUIT("You have quit the game. Please close the program")
        break 
        
    else:
        typewriter_print("please answer yes or no")
typewriter_print("Barbie strolls towards you, her hands crossed behind her back. 'I know what happened to the lighthouse keepers...' she mutters")

while True:
    lighthouseanswerlost = input("Do you want to ask Barbie what happened to the lighthouse keepers?")
    if lighthouseanswerlost == 'yes':
        typewriter_print("You hesitantly make eye contact with Barbie, and ask, 'what?'")
        break
    if lighthouseanswerlost == 'no' :
        typewriter_print("Would you like to try and answer again...? It would be a shame for you to end up like those lighthouse keepers before you...")
    if lighthouseanswerlost =='help':
      helpHint("This is the hint for this. you must answer yes or no")
    elif lighthouseanswerlost == 'quit':
      QUIT("You have quit the game. Please close the program")
      break 
    else:
        print("Please answer yes or no.")
typewriter_print("Her grin slips open... 'I'm assuming you have seen the cat?' she asks. You nod. 'Well the cat and I have unusual tastes... human tastes if you will...'")
clear_screen()
typewriter_print("'Yes, that's right,' she smirks, 'Salem and I enjoy eating humans... That is why the lighthouse keepers have gone missing, and why I chose you - a nobody herbologist with no friends or family to accompany me.")
typewriter_print("'Because you, my deary, will make an excellent meal. Salem and I will eat until the only leftovers are your bones.'")
clear_screen()
typewriter_print('She pulls out a bloodied axe from behind her.')
fightbarbiecore = input("Do you want to use your knife to fight Barbie?")
if fightbarbiecore == 'yes':
    typewriter_print("You summon your knife and swing it towards her threateningly. A girlie gasp flees her throat.")
    typewriter_print("She swings her arm towards you, puncturing your skin with the rusty weapon. You scream and step away from her slowly.")
    stablocation == input("You notice that she isn't standing defensively. Where would you like to stab her now that you have the oppurtunity? The chest, head, or thigh")
    while True:
        if stablocation == 'chest':
            print("You jam the blade into her heart, feeling the cool metal slip through her ribcage. Blood coats the knife and trickles down your arm. She gurgles obnoxuiously when you feel it puncture her lungs.")
        finalchestwords = input("What do you want to say to her - the final words she will ever hear?")
        typewriter_print("'Well,' you breath", finalchestwords, "Then she crumples onto the floorboards, dead...")
        break
    while True:
        if stablocation == 'head':
            typewriter_print("You jam the blade into her head, feeling the cool metal slip against her hard skull. Blood coats the knife and trickles down your arm. She winces in pain as you thrust it against her skull, until you can feel the bone crack.")
        finalheadwords = input("What do you want to say to her - the final words she will ever hear?")
        typewriter_print("'Well,' you breath", finalheadwords, "Then she crumples onto the floorboards, dead...")
        break
    while True: 
        if stablocation == 'thigh':
            typewriter_print("You jam the blade into her thigh, feeling the cool metal slip under her skin and grate it against the muscle. She crys pathetically as you flay the skin away from her body, detatching it from her flesh." )
        finalthighwords = input("What do you want to say to her - the final words she will ever hear?")
        ("'Well,' you breath", finalthighwords, "Then she crumples onto the floorboards, dead...")
        break 
    while True:
        
        if stablocation =='help':
            helpHint("This is the hint for this. You must defend yourself against Barbie")
        elif door1game == 'quit':
          QUIT("You have quit the game. Please close the program")
          break 
        else:
            typewriter_print("Please answer 'thigh' 'head' or 'chest'")
if fightbarbiecore == 'no':
    print('she stabs you and you die. exit the console now......')
    time.sleep(60)
else:
    print('your inaccurate typing skills just cost you your life... exit the console now...... game over')
    time.sleep(60)
#write confrontation
clear_screen()
      #ending scene
#go home, stare at lighthouse see light turn on and realise u let the cat live
print('You swim from the lighthouse to your home... nobody will notice the missing Barbie .. you think.')
typewriter_print("You get up from your book and spot on the lounge - that hagaan das icecream was a bad bad idea for your lactose introlerance self. You then move to sit on your balcony, happy to be safe back at home despite your crippling tummy ache. You look over to the lighthouse, it's standing strong against the setting sun. Suddenly the light switchs on, that's strange. Ohno. You forgot about the cat.")