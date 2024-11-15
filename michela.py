# Library
import sys # Imports the sys module for system-specific parameters and functions
import os # Imports the os module for interacting with the operating system
import random # Imports the random module for generating random numbers
import time # Imports the time module to add delays
from typing_extensions import deprecated  # Imports the deprecated decorator from typing_extensions
from yachalk import chalk # Imports the chalk module from yachalk for colored terminal output
from IPython.display import clear_output # Imports the clear_output function from IPython.display
clear_output(wait=True)

# Variables
player_name = ''
game_intro_text = ["Welcome to Save the Princess!", "Princess Chantilly has gone missing! Rumours have been spread about how she has been captured, but no one knows by who or what!! You must navigate your way through the castle and its many dangers to rescue the princess. ", "", "Good Luck!", "And remember, choose wisely...", "Loading game..."]

start_game_text = ["What is your name, brave knight? ", "You, ", " are our only chance!", "You have awoken in the castle garden. You see the bright sky and a variety of different flowers, trees and plants. As you look around, you notice the gardener, who is hard at work cutting the grass. "]

scene_one_text = ["\nWould you like talk to him? ", "Location: Royal Garden ", "\nHello, I'm the gardener. I'm busy cutting the grass. What is it that you need? ", "\nWell I'm sorry, I can't help you right now because it seems that I have lost my shovel! Can you find my shovel for me? ", "\nTask: Find the Gardners Shovel ", "\nOptions: Greenhouse, Royal Garden Shed, Courtyard, Rose Bush", "Where would you like to look? ", "\nYou step away from the castle garden, walking towards the greenhouse. During your journey, you admire the orderly rows of hedges and the intricate patterns of the flowerbeds, each bloom demonstrating the gardener’s meticulous care. The air was rich with the scent of freshly cut grass and the distant hum of bees. As you walk into the Greenhouse, you see a small box. Curious, you open it, but find nothing.", "\nYou search through the royal garden shed. It is small room covered in white tiles and a warm glow coming through the large window. The room is full of expensive gardening tools, a rose gold lawnmower and a small figure gleaming in the sunlight. ",'Would you like to investigate? ', "\nYou search the object and find that it is a sword with small engravings of a dragon on it. You put the sword in your inventory",  "\nYou look among the large coutyard full of perfectly cut, green hedgesall forming a perfect circle trapping the large, delicate waterfeature in the middle. The sparkling water trinkled down the stone foutain. You looked through the courtyard and notice something at the foot of the mountain. Its the gardners shovel!! You pick it up and put it in your inventory.", "\nYou look among the circular bush admiring the glamourous placement of the roses with there many blossoming, elegant petals. You start pushing aside the prickly leaves and get cut by a rose thorn.", "\nWould you like to return to the Gardener or keep searching? ", "\nReturning to the ", "Hey there! Thank you so much for finding my shovel! I'm so glad you... wait what is that you  have there?... oh no... that is the sword of the dragon! The princess must have been captured by him! You must go search the castle and rescue the princess! Goodluck brave Prince!" ]

scene_two_text =  ['As you open the door into the castle living room, a man frowns, searching around a room with an empty bell tray in his hands. Behind him is a television area, completely suffocating beneath piles of clothes and clutter. The mess travels across the room into an open library and office space, creating an uninviting disheveled atmosphere. The man catches your attention as he paces before the fireplace, sweat trickling down his worried face', '\nWould you like to talk to him? ', "Location: Castle Front Room", " Well hello there young one! I would really love to help you, but I am in need of my bell! I need it to call the maid as this room is a mess, though I do not know where she is! ", "Can you help me find it? ", '\nAs you are about to start searching, you walk across the soft rug and notice a bump beneath your feet. You decide to stop, so you pull back the rug and find... a key? You turn back around to face the butler and hand him the key. He looks even more confused and worried all of a sudden.', 'I thought it was just a rumour, but maybe its the truth.. As you may know, a dragon has captured the princess and has been reeking havoc around the castle. I overheard just a few hours ago that the maid had been locked in the bedroom! I assumed it was just a rumour, but this key was described! Once you find me my bell, I will tell you how to get to the maid!', '\nKey has been added to your inventory', '\nTask: Find the Butlers Bell', '\nWhere in this room would you like to inspect? ', '\nOn the far side of the living room lays a pile of unfolded clothes, scattered around a plush green couch, clothes strewn amongst the pillows. It is unclear what may be beneath the clothes, possibly the butlers bell. ', 'Would you like to take a look?', 'You look among the mess of the living room and find absolutely nothing!', '\nTo the left of the doorway is an office nook, lit by warm candlelight. The desk, tucked comfortably between two bookshelves,  is littered with old newspapers and paperwork, as well as unwashed mugs staining the wood with rings of coffee. Most of the wood remains hidden under the mounds of clutter, making it impossible to find anything. ', 'Do you think the bell might be under here? ', '\nAs you’re hauling down the stacks of paper from the desk, you realise there is no bell on the desk. You turn towards one of the bookshelves and grab onto a large book. You yank as hard as you can, but suddenly a shower of books land on you, sending you flying backwards against the paper littered floor. A creaking noise appears from above you, and before you can get a good look at the incoming bookshelf, a book hits you on the head, creating a penetrating stabbing pain. After a few seconds, the pain vanishes', '\nFar in the corner of the room, a reading area made up of brightly coloured bean bags catches your eye. The exquisite chandelier illuminates a metallic object stuffed beneath piles of thick volumes. It looks almost like….a bell! You decide to investigate…', '\nYou run over to the beanbags and begin lifting off the leather covered books. This reveals a shiny silver bell, sitting atop a purple bean bag. You quickly grab it and turn towards the butler, excited to see the joy on the old mans face at the sight of his bell.', 'Ah! Thank you so much for finding my bell! Now to get to the maid you need to go through the dark corridor and then down the spiralling stone steps and there, you should find the old bedroom where she is rumoured to be locked. Good luck!']

scene_three_text = ["As you leave the butler's quarters, the urgency of his message weighs heavily on your shoulders. The echoes of the butler’s hurried words still ringing in your ears: “I heard a rumour that the maid is locked in the old bedroom!” You quicken your pace through the dimly lit corridors of the castle, each footstep a resounding promise of finding the maid. The ancient tapestries lining the walls whisper forgotten secrets as you pass by. Your hand brushes the hilt of your engraved sword, ready for whatever might lie ahead. The air grew cooler and mustier as you descended the spiralling stone steps toward the bedroom and at last, you reach the room, and hear faint, muffled cries, spurring you into action. With a determined twist of the key, you open the bedroom to find the maid, eyes wide with fear, sitting still like a statue.", "You stare in confusion as the maid starts moving. It’s all quite strange, as if she’s under a spell.", " Enchanted now, within these walls, I, a maid who once would serve the halls. A dragon’s curse, a binding spell, I guard the secret I cannot tell. A knight may come with sword so bright, Seeking princess in the night. Yet in my riddle, lies the key, To free her from this misery. If wits are sharp and courage true, The knight might break the curse in two. But fail, and shadows keep their hold, The dragon wins—his heart stays cold.", "Can you, brave knight, unveil the clue, To save us from this fate so cruel? ", "Trapped in silence by the dragon's spell, A maid whose secrets I cannot tell. Locked within this ancient room, The key to knowledge lies in my broom. Find this token, dear brave knight, Or remain in shadows, lost in night. The dragon guards the princess fair, But words of truth, I cannot share. Without my broom, my lips are sealed, The secrets of the curse concealed. Seek the broom and break the chain, Only then will wisdom reign.", "Bound by the spell and dragon’s might, I whisper clues to aid your night. The broom you seek, essential key, Is hidden where I cannot see. In the billiard room, shadows play, Three spots where it might lay: ", "\nThe cupboard, silent and cold, The pool table, mysteries hold, Or in the minibar, concealed and still.",  "\nFind it, and break the binding will. Search these places, brave and true, Reveal the broom, uncover the clue. Only then my voice shall sing, And to the princess, freedom bring. May your search be swift and keen, Unlock the secret, make us free.", "\nWhere will you search brave knight? ", "\nYou step out of the bedroom, determined to find the broom and save the princess. As you keep walking  you hear the gentle creak of the wooden floorboards beneath your boots barely masking the resolve in your stride. You move quickly down the dimly lit corridor, your shadow flickering against the ancient stone walls adorned with faded tapestries of past glories. As you reach the billiard room, you pause briefly, surveying the room's opulence — the green felt table, ornate chandelier, and the gleaming minibar. Your eyes lock onto the cupboard at the far end of the room. With a deliberate, cautious approach, you cross the room, your every step echoing the weight of this mission. The cupboard loomed ahead, its polished wood glinting in the soft light, a silent keeper of secrets. Holding your breath, you reached out, the handle cool and firm, ready to uncover the hidden broom and the key to your quest. As you peek inside, you find nothing but a sign saying 'I know of your quest to find the princess. Your courage is commendable, but it will be your undoing. My flames have scorched the bravest of souls, and my claws have torn through the strongest of armor. Turn back now, or face a fate worse than death. The princess is mine, and so shall be your doom if you dare to challenge me. - Falkinor, the dragon ", "The scent of aged wood and ancient drapery fills your senses. As you enter the billiard room, the familiar sight of the pool table commanded your attention. The table's green felt surface, once pristine, now bore marks of neglect and use. With careful steps, you approach, your eyes scanning for any sign of the hidden broom. The search grew frantic as you lift the corners of the tablecloth and check beneath the table, but find nothing. Then, as you straighten up, your eyes caught the deep, jagged gouges marring the table's surface. Dragon claw marks. The realization hit you like a blow, the sheer power and presence of the beast etched into the very fabric of the room. Your grip tightens around the sword. The dragon was near, you could feel it. ", "You move with purpose from the bedroom, the urgency of your quest driving each step. As you enter the billiard room, the dim light catches the polished surfaces of the minibar. Your eyes scanning the collection of bottles and glasses. You approach the minibar, your heart pounding in your chest. With careful, deliberate movements, you begin to search, pushing aside the crystal decanters and intricately carved wooden boxes. Then, hidden behind a row of vintage wine bottles, you find it, the broom. Its handle was worn but sturdy, the bristles slightly frayed. Relief washes over you as you grasp the broom, the key to breaking the spell and rescuing the princess is now in your hands. ",  ]

scene_four_text = ['\nWould you like to talk to the donkey? ', 'Well met stranger of peculiar form! Word has reached my ear that thou art known by the calling of ',  'Sent, so it is told, by the fair maid herself, thou comest seeking whispers of thine heart’s desire. Yet, ere such secrets I do impart, thou must make a choice most curious and rare!', '\nYour sight is blinded by a glow as almost from the heavens, as your eyes adjust you notice that next to the donkey two objext have appeared, one is a shiny, red apple surrounded by a rim of gold, and the other the golden cresent of a banana surronded by a rim of silver glow.', 'So what does thou desire the juicy crunch of thy apple or the sweet desires of thy banana? ', 'So an apple thou hast chosen—most splendid of choices!' , ' Oho... a banana thou hast chosen, have ye? An interesting choice... most curious indeed.', 'Now heed this, for to learn the place where the fair princess is held, thou must seek counsel with the master of the kitchen—the chef himself holds the answer to her hiding. Remember, always choose wisely, for each choice weaves the tapestry of fate.', "After leaving the maid you wander again amongst the dark, mysterious hallways of the castle. You search among rooms until you finally stumble upon a brown wooden door with a golden sign reading 'Laundry'. Before stepping in, you brace yourself for the unknown creature which may lurch inside. You slowly creek open the door to reveal... a donkey.. with a dark, long curly moustache... and a black top hat?"]

scene_five_text = ['After leaving the laundry you start exploring the vintage corridors of the castle in search for the kitchen, all of sudden you smell a variety of scents, some of sweets and some savoury, all delighting your senses. You follow the smell and find a large metal door, its the kitchen!', '\nYou enter the kitchen and the first thing you see is the chef. He is cupping his head with his hand, and sitting next to him is a fresh bowl full of a cream coloured mixture. He glances up and sees you, immediately his eyes lit up as if you were some miracle, he starts to approach you, ', 'Bonjour! Finally someone has come to help me with my cooking. Je suis furieux! I have been stuck on this crepe recipe for so long! Can you please help me finish my recipe? ', 'Merci beacoup! Now I have some ingredients to choose from to finish off the recipe please choose one! Hopefully your magic touch will put an end to my misery!', 'What extra special ingredient do you want to add to the recipe? ', '\nYou pick up the sugar from a jar and add a handful, you want it to be extra sweet. You mix it in and try some of the mixture. Ew! Its disgusting, you immediately spit it out, it almost tasted... salty? You check the jar you got the sugar from and see that the jar is marked salt not sugar!', '\nThe chef gives you a new mixture, maybe try again!', 'You grab two eggs, crack them and add them to the mixture. You mix the eggs into the golden brown mixture, its starting to smell wonderul! You decide to try some of it andd... Oh my gosh its delicious! You notify the chef immediately.', 'Wow this really is delicieux! Thank you so much! Now I heard you need help finding the princess, I heard that apparently she is being kept in the castle abandonded tower, I suggest you get there quickily! Also, as a reward please take this token of a chocolate bar! Merci!', 'You realise that you are feeling a bit hungry, but the princess is also gonna be hungry when you save her! ', 'Do you want to eat the chocolate or save it for the princess?', 'You pour a large amount of bleach into the mixture, making sure it has an extra tang to the flavour. Mixing it around your nostrils start to fill with the toxic smell, burning your nose and eyes. You decide to try the golden brown mixture incase you added something wrong. You try it... after a few second your stomach starts burning as if set on fire, your vision starts to blur as you look around to notify the chef you notice the oxygen from your lungs is gone. Your vision slowly fades to black as you feel your heart stop and your body going limp...']

scene_six_text = ["\nAfter you wander out of the kitchen, you walk outside again. Faintly, yet surely in the distance, there is the castle's abandoned tower. Thick clumps of overgrown ivy nearly cover the entirety of the tower. You make your way across the intricately mowed lawn until you realise the only way to cross the lake is a crickety small wooden bridge. You lift your foot to step across then you look down. Snapping underneath are hungry crocodiles which haven't eaten in ages. ", "\nLocation: Abandoned Bridge", "\n\nWould you like to test the bridge or would you like to cross it? ", "\nYou throw a sturdy rock against the bridge and watch as the bridge crumples under the light weight, crashing down onto the scrawny hungry crocodiles below who leap up and demolish the worn out timber.", 'A note blows in the wind and falls at your feet. ', 'Would you like to read it? ', '\nNote Added to Inventory', '\nScrawled across the paper in cursive says “Near is help and help is near, to find me you will find some gear, in the haystack down the slope, lies and lays a worn out rope!', "\nYou start making your way back down the slope, you look up at the sky and realise it's getting dark, you are running out of time. The trimmed grass brushes against your ankles as you speed down to where you noticed a haystack earlier. You frantically pull the haystack apart searching for rope, prickly piles of hay begin to form beside you, you are about to give up then your hand touches a rough thick rope. You wrap it around your hand then sprint back up the luscious lawn. You come back to the bridge, this time with a rope.", '\nRope added to inventory', '\nWould like to risk it all and swing across?', '\nYou lasso the rope and hurl it onto one of the spikes on the top of the tower, you take a few steps back and then you start running. You jump and magnificently swing across the lake, as the tower nears you shorten the rope and pull yourself up onto the old balcony. The air is thick with a sense of mystery and eeriness.', 'You take a step further onto the planks, the bridge trembles under your weight and eventually gives way, as you slowly plummet to your death you manage to grab a handful of leaves. You hang a few centimetres from the hungry mouths of the crocodiles who are now angry that their snack has escaped. One of them jumps up and snaps at your feet, you wrench your foot out of its mouth, your fingers slip from the ledge as another crocodile crunches through your bones. Blood oozes from your legs as you watch what once had been your foot, bobbing against the current. The creature spins you around in the swampy muddy water as you feel blood draining from your dismembered body, the world starts to blur and turns to darkness']

scene_seven_text = ['\nLocation: Abandoned Castle Tower', '\nYou look around the mysterious balcony, the land around you has been covered with a blanket of fog. You turn around, ready to set foot into the golden door in front of you. As you walk forward towards the door your heart racing, palms sweaty you stumble on a mysterious object on the floor...', '\nMaybe that will be useful in fighting the dragon? You think to yourself, as you slowly creak the door open. The room is a large stone room with a large cage in the middle, inside stands a beautiful girl with white luscious locks, emerald eyes and a stunning velvet dress, wait... ITS THE PRINCESS!! As you realise about to release her you hear a growl to your right, you turn around and there towering over you is a giant dragon, you have no time to react, you must fight!', '\nFinal Task: Defeat the Dragon', '\nWhat from your inventory would you like to use? ', '\nYou grab the carefully crafted sword from your pocket and slash the dragon, a green ooze starts running from its skin!', '\nYou grab the apple and quickly eat it... all of sudden you feel extremely energized!', "\nYou grab the banana and quickly eat it... woah it doesn't taste very good...", '\nYou grab the rope from over your shoulder and whip the dragon on the back!', '\nYou grab the pencil out of your pocket and decide to strike the dragon! It completely misses and land next to the dragon... uh oh he looks mad!', '\nYou quickly gulp down the Golden Slice of Pizza, wow its delicious!', '\nYou decide to point the ring straight at the dragon it hope of it being able to do something... all of a sudden the a blinding beam of light shoot out of the ring and strikes the dragons eye!', '\nYou received a blunt pencil!', '\nYou received a beautiful ring with a bright red ruby in the middle!', '\nYou received a Golden Slice of Pizza!']

scene_eight_text = ["You stand there breathing deeply, staring at the beauty of the caged princess. You feel a sense of relief, this long jurney has finally paid off, and you will get to live your happily ever after, with the girl of your dreams. You walk to the rusty cage and kick it open, the princess is there, staring at you with a smile on her face.", "Hello fine knight, thank you for saving me! I have been stuck in this castle for so long! and now I can finally have my happily ever after! Do you have any food? Oooh what about chocolates? I'm starving!!! ", "What!! You came all this way without something to give to your fair maiden? You are not a real gentleman!", "\nYou have been slapped on the cheek by the princess.", "\nGAME OVER", "\nYou have not saved the princess successully, please try again.", "\nYou hand the princess the chocolate and she thanks you for saving her and rewards you with a passionate kiss. Soon after, you get married and start a beaufiul family. You also live in a huge mansion with all your friends and family and live happily ever after.", "\nYou have saved the princess!", "\nYOU WIN! CONGRATULATIONS!"]

chef_recipe = ['Flour', 'Milk', 'Butter', 'Vanilla Essence', 'Sugar']
ingredients_add = ['Extra Sugar', 'Eggs', 'Bleach']

player_inventory = [] 
gardener_inventory = []
maid_inventory = []
player_health = 100 # Initial health of the user
dragon_health = 200 # Initial health of the dragon
dragon_damage_options = [100, 75, 50, 25, 10, 0] # Damage values that the dragon can inflict against user
dragon_damage_text = ['\nThe dragon is mad and in a flash, it breathes a gush of fire towards you. A burning sensation aches your skin as the world starts to fade from the black of ash, to a black of death... \n -100 Health','\nIn protection of the princess, the dragon bites of your arm! \n -75 Health', '\nThe dragon is infuriated! It rapidly spins around and knocks you out with its tail! \n -50 Health', '\nThe dragon, in a mad rush scraps it claws against your body, you try to dodge it but get struck! \n-25 health', '\nThe dragon wacks you on the head with its paw. Ow! \n -10 health',  '\nThe dragon is getting mad, in fury it roars at you to try and scare you away but you are stronger than this so you stand strong before it ready to murder it and save your true love! \n -0 health']
player_item_options = ['Pencil', 'Ruby Ring', 'Golden Pizza'] #Items that the player can use to attack the dragon
scene_one_loop = True

#Text animations
def print_slow(text, delay=2):
    print(text, end='', flush=True)
    time.sleep(delay)
    print()

def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.07)

#Game intro
def game_intro():
    print_slow (chalk.italic(str(game_intro_text[5])))
    animate_text(str(game_intro_text[0]))
    print_slow(str(game_intro_text[2]))
    animate_text(str(game_intro_text[1]))
    print_slow(str(game_intro_text[2]))
    print(str(game_intro_text[3]))
    print_slow(str(game_intro_text[2]))
    animate_text(str(game_intro_text[4]))
    print_slow(str(game_intro_text[2]))

#Quit Game function
def quit_game(): 
    print("You have now ended the game.") 
    time.sleep(2) # Adds a delay of 2 seconds
    clear_screen() # Clears screen after output
    sys.exit()

#Clear Screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Start of game
def start_game():
    player_name = input(str(start_game_text[0]))
    animate_text(str(start_game_text[1]) + player_name + "," + str(start_game_text[2]))
    print(str(game_intro_text[2]))
    animate_text(str(start_game_text[3]))

#Scene one ending function
def scene_one_ending():
    global scene_one_loop # Access the global scene_one_loop variable
    return_gardener = input(str(scene_one_text[13]))
    if 'return' in return_gardener.lower(): #Checks if the user input contains the word 'return'
            if ('Shovel'in player_inventory) and ('Sword' in player_inventory):
                clear_screen() # Clears screen
                animate_text(chalk.grey(scene_one_text[14]) + chalk.green(' Gardener'))
                time.sleep(2) # delays text by 2 seconds
                animate_text (chalk.green('\nGardener: ') + scene_one_text[15])
                player_inventory.remove('Shovel') # Removes shovel from inventory
                gardener_inventory.append('Shovel') # Adds shovel to gardener inventory
                scene_one_loop = False 
            else: 
                print('Sorry you have not found everything to complete the scene. Keep Searching!') # Informs player that they have not found all necessary items to complete the scene
    elif 'keep searching' in return_gardener.lower(): 
            print(" ")
    else:
            print(chalk.red('Invalid. Please try again.')) #Promps the player to try again


#Scene 1
def scene_one(): # Function for scene 1
    global scene_one_loop # Set flag for scene 1 loop
    while (scene_one_loop == True): # Loops until the scene is completed
        global player_health # Access the global player_health variable
        gardener_interaction = input(str(scene_one_text[0])) #Prompts the player for interaction with the gardener
        if "yes" in gardener_interaction.lower(): # If player responds with 'yes'
            animate_text(chalk.gray(scene_one_text[1])) # Displays text in grey colour
            gardener_one =  input(chalk.green("\nGardener: ") + (str(scene_one_text[2]))) # Displays Gardener's dialogue in green
            if "help" in gardener_one.lower(): # If player responds with 'help'
                    shovel = input(chalk.green("Gardner: ") + (str(scene_one_text[3])))
                    if "yes" in shovel.lower(): # Loop until player finds sword and shovel
                            while ('Shovel' not in player_inventory) and ('Shovel' not in gardener_inventory) or ('Sword' not in player_inventory) :
                                time.sleep(2) # Pause for 2 seconds
                                clear_screen() # Clears the screen
                                animate_text (chalk.grey(scene_one_text[4])) # Displays text in grey
                                print(chalk.cyan(chalk.underline (scene_one_text[5]))) #Displays text in cyan and underlined
                                gardener_look = input(str(scene_one_text[6]))
                                if "greenhouse" in gardener_look.lower(): # Various location options for user
                                    animate_text(scene_one_text[7])
                                elif "royal garden shed" in gardener_look.lower():
                                    animate_text(scene_one_text[8])
                                    sword = input(str(scene_one_text[9]))
                                    if "yes" in sword.lower():
                                        animate_text(scene_one_text[10])
                                        player_inventory.append('Sword') # Sword added to player inventory
                                        animate_text(chalk.gray('\nSword Added to Inventory.')) # Displays that the sword is added to player inventory
                                        scene_one_ending() # Calls the ending function for scene one
                                    elif "help" in sword.lower():
                                        print(chalk.green_bright("Froggy the Guide:"), "Psssst! I think you should take the sword, it might come in handy later!") # Gives a hint
                                    elif "quit" in sword.lower():
                                        quit_game() # Quits the game
                                    else:
                                        animate_text('Continue searching the garden...')

                                elif "courtyard" in gardener_look.lower():
                                    animate_text(scene_one_text[11])
                                    player_inventory.append('Shovel') # Adds the shovel to player inventory
                                    animate_text(chalk.gray('\nShovel added to Inventory.'))
                                    scene_one_ending()
                                elif "rose bush" in gardener_look.lower():
                                    animate_text(scene_one_text[12])
                                    player_health = (player_health - 10) # Decrease player health
                                    animate_text(chalk.red('\n-10 Health')) # Display health loss
                                    print("\nHealth = " + str(player_health)) # Show current health
                                elif "quit" in gardener_look.lower():
                                    quit_game() # Quits the game

                                elif "help" in gardener_look.lower():
                                 print(chalk.green_bright("Froggy the Guide:"), "Maybe you should look in the Royal Garden Shed. You never know what you'll end up finding!") 
# Gives hint

                                elif "quit" in gardener_look.lower():
                                    quit_game() # Quits the game
                                
                                else:
                                    print(chalk.red("I'm sorry, but that does not exist in this castle. Try again please. "))  # Invald input message
                    elif "no" in shovel.lower():
                        print("I really think you should find his shovel! He might help you save the princess!")
                    elif "help"in shovel.lower(): # If user asks for a hint/help
                        print(chalk.green_bright("Froggy the Guide:"), "Go find his shovel, it will give you a chance to explore the castle! ") # Hint for this scene
                    elif "quit" in shovel.lower():
                        quit_game() # Quits the game
                    else:
                        print("This is not an option. Please try again") # Invalid input message
                        
        elif 'no' in gardener_interaction.lower(): # If player replies with 'no' to the gardener interaction
            print("Hmmm, I really think you should talk to the gardener")
        elif "help" in gardener_interaction.lower():
            print(chalk.green_bright("Froggy the Guide:"), "I really think you should talk to the gardener, he might help you save the princess!")
        elif "quit" in gardener_interaction.lower():
            quit_game() # Quits the game

        else:
            print(chalk.red("I'm sorry, but that is not an option. Please try again."))   # Invalid input message

# Scene 2
def scene_two(): # Function for scene 2
    global player_health # Access the global player_health variable
    scene_two_loop = True # Set flag for scene 2 loop
    while (scene_two_loop == True): # Loops until the scene is completed
        time.sleep(3) # Delays output by 3 seconds
        clear_screen() # Clears screen
        animate_text(scene_two_text[0]) # Displays initial text for scene 2
        butler_interaction = input(scene_two_text[1]) # Prompts the player for interaction with the butler
        if 'yes' in butler_interaction.lower(): # If player responds with 'yes'
            animate_text(chalk.grey(scene_two_text[2])) # Displays text in grey
            animate_text(chalk.blue('\nButler: ') + str(scene_two_text[3])) # Displays butlers dialogue in blue
            butler_bell = input(scene_two_text[4])
            if 'yes' in butler_bell.lower(): # If player responds with 'yes'
                animate_text(scene_two_text[5])
                animate_text(chalk.blue('\nButler: ') + scene_two_text[6])
                animate_text(chalk.grey(scene_two_text[7])) # Displays text in grey
                player_inventory.append('Key') # Adds key to player inventory
                while ('Bell' not in player_inventory): # Loop until player finds the bell
                    time.sleep(3) # Delays output by 3 seconds
                    clear_screen() # Clears screen
                    animate_text(chalk.gray(scene_two_text[8]))
                    animate_text(chalk.cyan(chalk.underline('\nOptions: Chaotic living room, Messy office, Bean bags')))
                    butler_look = input(scene_two_text[9]) # Asks where player wants to look
                    if 'living room' in butler_look.lower(): # Various locations for player to look
                        animate_text(scene_two_text[10])
                        living_room_search = input(str(scene_two_text[11]) + ' ')        # Prompts player to search the living room
                        if 'yes' in living_room_search.lower(): 
                            animate_text(scene_two_text[12])
                        else:
                            print('')
                    elif 'office' in butler_look.lower(): # Prompts player to search the office
                        animate_text(scene_two_text[13])
                        office_search = input(scene_two_text[14])
                        if 'yes' in office_search.lower():
                            animate_text(scene_two_text[15])
                            print(chalk.red('\n-100 Health')) # Displays health loss in red
                            print(player_health) 
                            print(chalk.red('\nYou were killed by a falling bookshelf. \n GAME OVER'))
                            time.sleep(3) # Delays output by 3 seconds
                            player_health = 0 # Set players health to zero
                            scene_two_loop = False # End scene loop
                            clear_screen() # Clears screen
                            break # Exit loop
                        else:
                            print('')
                    elif 'bean bags' in butler_look.lower(): 
                        animate_text(scene_two_text[16])
                        time.sleep(1) # Delays output by 1 second
                        animate_text(scene_two_text[17])
                        player_inventory.append('Bell') # Add bell to players inventory
                        time.sleep(3) # Delay for 3 seconds
                        animate_text(chalk.blue('\nButler: ') + scene_two_text[18])
                        time.sleep(3) # Delay for 3 seconds
                        scene_two_loop = False # End scene loop
                        break # Exit loop
                    else:
                        print(chalk.red('This is not an option. Please try again.'))     # Invalid input message
            elif "help" in butler_bell.lower():
                print(chalk.green_bright("Froggy the Guide:"), "I think you should find his bell, it might help you save the princess!") # Give a hint

            elif "quit" in butler_bell.lower():
                quit_game() # Quits the game
                
            elif 'no' in butler_bell.lower():
                animate_text('I really think you should find his bell, try again!') # Prompts player to try again
            else:
                animate_text(chalk.red("I'm sorry, but that is not an option. Please try again.")) # Invalid input message
                

        elif 'no' in butler_interaction.lower():
            animate_text('The princess is still lost, and the butler may be able to assist in your adventure! He really needs your help!') # Prompt to help the butler

        elif "help" in butler_interaction.lower():
            print(chalk.green_bright("Froggy the Guide:"), "You should try talking to the butler, he may be able to help you save the princess!") # Give a hint

        elif "quit" in butler_interaction.lower():
            quit_game() # Quits the game
    
        else:
            animate_text(chalk.red("I'm sorry, but that is not an option. Please try again.")) # Invalid input message
            
#Scene 3
def scene_three(): # Function for scene 3
    scene_three_loop = True # Set flag for scene 3 loop
    while (scene_three_loop == True): # Loop until scene is completed
        time.sleep(3) # Delays for 3 seconds
        clear_screen() # Clears screen
        animate_text(scene_three_text[0]) # Display initial text for scene 3
        animate_text(scene_three_text[1]) # Display additional text for scene 3
        time.sleep(1) # Pause for 1 second
        animate_text(chalk.gray('\nLocation: Palace Bedroom')) # Display Location
        animate_text(chalk.magenta('\nMaid: ') + scene_three_text[2]) # Display maids dialougue in magenta
        maid_interaction = input(str(scene_three_text[3])) # Prompt player for interaction with maid
        if "yes" in maid_interaction.lower(): # If player responds wiht 'yes'
            animate_text(chalk.magenta("\nMaid: ") + scene_three_text[4]) # Displays maids dialogue in magenta
            while ('Broom' not in player_inventory and 'Broom' not in maid_inventory):   # Loop until player finds the broom
                time.sleep(3) # Delay for 3 seconds
                clear_screen() # Clear screen
                animate_text(chalk.magenta('\nMaid: ') + scene_three_text[5] + chalk.bold(scene_three_text[6]) + scene_three_text[7]) # Ask where player wants to look
                print(chalk.grey("\nTask: Find the maid's broom.")) # Provide task information
                broom_location = input(scene_three_text[8]) # Ask where player wants to look
                if "cupboard" in broom_location.lower(): # Various location options player can choose
                    animate_text(scene_three_text[9]) # Print cupboard text
                    animate_text(chalk.grey("\nYou have not found the broom. Continue searching. ")) # Prompt the player to continue searching
                elif "help" in broom_location.lower():
                    print(chalk.green_bright("Froggy the Guide:"), "Maybe you should look in the minibar. You never know what you'll end up finding!") # Give a hint

                elif "quit" in broom_location.lower():
                    quit_game() # Quits the game
                
                elif "pool table" in broom_location.lower():
                    animate_text(scene_three_text[10]) # Display pool table text
                    animate_text(chalk.grey("\nYou have not found the broom. Continue searching. ")) # Prompts the player to continue searching
                elif "minibar" in broom_location.lower():
                    animate_text(scene_three_text[11]) # Display minibar text
                    print(chalk.grey("\nBroom added to Inventory")) # Display that broo is added to inventory in grey 
                    player_inventory.append('Broom') # Add broom to players inventory
                    help_maid = True
                    while (help_maid == True):
                        help_maid_interaction = input("\nWould you like to go back to the maid? ") # Asks if the player wants to go back to the maid
                        
                        if "no" in help_maid_interaction.lower(): # Prompts the player to go back to the maid
                            print("To complete the game, you have to go back to the maid.") 
                        elif "help" in help_maid_interaction.lower():
                            print(chalk.green_bright("Froggy the Guide:"), "GO BACK TO THE MAID!") # Give a hint
                        elif "quit" in help_maid_interaction.lower():
                            quit_game() # Quits the game
                        elif "yes" in help_maid_interaction.lower():
                             animate_text(chalk.magenta("Maid: ") + "Thank you so much barve prince for saving me from the curse! You must find the princess, I know of a magical creature that lives in the castles laundry. Find it and it shall help you with your quest!") 
                             time.sleep(2)
                      
                             player_inventory.remove('Broom') # Remove broom from player inventory
                             maid_inventory.append('Broom') # Add broom to maid inventory
                             help_maid = False # End maid loop
                             scene_three_loop = False # End scene 3 loop
                        else:
                            print(chalk.red("I'm sorry but that is not an option. Please try again.")) # Invalid input message
                else:
                    print(chalk.red("That does not exist in this castle...")) # Invalid input message     
    
    
        elif "no" in maid_interaction.lower():
            print("To continue the game, you have to find the broom.") # Prompt the player to find broom

        elif "help" in maid_interaction.lower():
            print(chalk.green_bright("Froggy the Guide:"), "You should go find the broom, it might help you save the princess!") # Give a hint

        elif "quit" in maid_interaction.lower():
            quit_game() # Quits the game

        else:
            print(chalk.red("I'm sorry but that is not an option. Please try again.")) # Invalid input message

# Scene 4
def scene_four(): # Function for scene 4
    clear_screen() # Clears screen
    scene_four_loop = True # Set flag for scene 4 loop
    while scene_four_loop == True: # Loop until scene is completed
        time.sleep(2) # Delays text for 2 seconds
        clear_screen() # Clears screen
        animate_text(scene_four_text[8]) # Display initial scene 4 text
        animate_text(chalk.grey('\nLocation: Laundry ')) # Display location in grey
        donkey_interaction = input(scene_four_text[0]) # Prompt player for interaction
        if 'yes' in donkey_interaction.lower(): # If player responds with 'yes'
            animate_text(chalk.green_bright('\n\nDonkey: ') + scene_four_text[1] + player_name + scene_four_text[2]) # Print donkey dialogue in bright green
            time.sleep(2) # Delays text for 2 seconds
            donkey_choice = True
            while donkey_choice: # Loop until player chooses an option
                animate_text(scene_four_text[3])
                donkey_choice = input(chalk.green_bright('\n\nDonkey: ') + scene_four_text[4]) # Prompt for players choice
    
                if 'apple' in donkey_choice.lower():
                    animate_text(chalk.green_bright('\n\nDonkey:') + scene_four_text[5])
                    player_inventory.append('Apple') # Add apple to players inventoory
                    animate_text(chalk.gray('\nApple added to Inventory.')) # Display apple added to inventory in grey
                    time.sleep(2) # Delays text for 2 seconds
                    animate_text(chalk.green_bright('\n\nDonkey:') + scene_four_text[7])
                    scene_four_loop = False # End scene 4 loop
                    donkey_choice = False # End donkey choice loop
                    break # Exit the loop
    
                elif "help" in donkey_choice.lower(): # If player asks for 'help'
                     print(chalk.green_bright("Froggy the Guide:"), "I don't know man, they both seem pretty cool to me. I think this decision is up to you! Pick wisely...")   # Give a hint
                     time.sleep(2) # Delay for 2 seconds
                     clear_screen() # Clear screen
    
                elif "quit" in donkey_choice.lower():
                    quit_game() # Quits the game
                
                elif 'banana' in donkey_choice.lower():
                    animate_text(chalk.green_bright('Donkey:') + scene_four_text[6])
                    player_inventory.append('Banana') # Add banana to player inventory
                    animate_text(chalk.gray('\nBanana added to Inventory.')) # Display banana added to inventory in grey
                    time.sleep(2) # Delay text for 2 seconds
                    animate_text(chalk.green_bright('\nDonkey:') + scene_four_text[7])
                    scene_four_loop = False # End scene 4 loop
                    donkey_choice = False # End donkey choice loop
                    break # Exit the loop
                else:
                    print(chalk.red('Invalid, Please Try Again')) # Invalid input message
                    time.sleep(2) # Delay text for 2 seconds
                    clear_screen() # Clear screen
        
        elif 'no' in donkey_interaction.lower():
            print('Are you sure you do not want to talk to the donkey? Maybe try again!') # Prompts user to try again
        
        elif "help" in donkey_interaction.lower():
             print(chalk.green_bright("\n\nFroggy the Guide:"), "I reckon you should talk to the donkey, after all, we are of similar kind! He may have some useful information for you!") # Give a hint

        elif "quit" in donkey_interaction.lower():
            quit_game() # Quit game
        
        else:
            print(chalk.red('Invalid, Please Try Again')) # Invalid input message

# Scene 5
def scene_five(): # Scene 5 function
    scene_five_loop = True
    while(scene_five_loop == True): # Loop until scene is completed 
        global player_health # Access the global player_health variable
        clear_screen() # Clear screen
        animate_text(scene_five_text[0]) # Display initial scene 5 text
        print(chalk.grey('\nLocation: Kitchen')) # Display location in grey
        animate_text(scene_five_text[1]) # Display additional text
        chef_interaction = input(chalk.cyan('\nChef: ') + str(scene_five_text[2]))
        if 'no' in chef_interaction.lower(): # Prompt the player to talk to the chef
            print('I really think you should help the chef, try again!')
            time.sleep(2) # Delay text by 2 seconds

        elif 'quit' in chef_interaction.lower():
            quit_game() # Quit game

        elif 'help' in chef_interaction.lower():
            print(chalk.green_bright("Froggy the Guide:"), "Talk to the chef, it might be useful!") # Give a hint
            time.sleep(2) # Delay text by 2 seconds
        elif 'yes' in chef_interaction.lower(): # If player responds with 'yes'
                animate_text(chalk.cyan('Chef: ') + scene_five_text[3]) # Print Chefs dialogue in cyan
                chef_help = True # Set flag for chef help loop
                while (chef_help == True): # Loop until player completes tasks with chef
                    time.sleep(2) # Delay text by 3 seconds
                    clear_screen() # Clear screen
                    print('\nRecipe so far:' + str(chef_recipe)) # Display recipe so far
                    print('Ingredients to add: ' + str(ingredients_add)) # Display options for ingredients to add
                    other_ingredient = input(scene_five_text[4]) # Prompt for the next recipe
                    if 'extra sugar' in other_ingredient.lower(): # If player chooses to add extra sugar
                        animate_text(scene_five_text[5])
                        player_health = (player_health - 10) # Decrease player health
                        print(chalk.red('\n-10 Health')) # Display health loss in red
                        print(player_health) # Show current health
                        animate_text(scene_five_text[6]) 
                    elif 'eggs' in other_ingredient.lower(): # If player chooses to add eggs
                        animate_text(scene_five_text[7])
                        time.sleep(2) # Delay text by 2 seconds
                        animate_text(chalk.cyan('\nChef: ') + scene_five_text[8]) # Display chefs dialogue in cyan
                        print(chalk.gray('\nChocolate bar added to inventory.')) # Display chocolate bar added to inventory in grey
                        player_inventory.append('Chocolate bar') # Add chocolate bar to player inventory
                        time.sleep(2) # Delay text by 2 seconds
                        animate_text(scene_five_text[9])
                        chocolate_eat = input(scene_five_text[10]) # Prompt player for next actions
                        if 'eat' in chocolate_eat.lower(): # If player chooses to eat the chocolate bar
                            print(chalk.grey('Chocolate bar removed from inventory.')) # Display chocolate bar removed from inventory in grey
                            player_inventory.remove('Chocolate bar') # Remove chocolate bar from player inventory
                            chef_help = False # End chef help loop
                            scene_five_loop = False # end scene 5 loop
                            break # Exit loop
                        elif 'save' in chocolate_eat.lower(): # If player chooses to save the chocolate bar
                            print(chalk.grey('Chocolate bar kept in inventory.')) # Display chocolate bar kept in inventory in grey
                            chef_help = False # End chef help loop
                            scene_five_loop = False # End scene 5 loop
                            break # Exit loop

                        elif 'help' in chocolate_eat.lower():
                             print(chalk.green_bright("Froggy the Guide:"), "Well, if I was a princess locked away in a tower, I would be pretty hungry if you ask me, but no matter what, the decision is up to yo. Choose wisely...") # Give a hint

                        elif 'quit' in chocolate_eat.lower():
                            quit_game() # Quit game
                            
                        else:
                            print(chalk.red('Invalid input try again')) # Invalid input message
                    # If player chooses to add bleach
                    elif 'bleach' in other_ingredient.lower(): #Death outcome
                        animate_text(scene_five_text[11])
                        print(chalk.red(' -100 Health \nGAME OVER')) # Display game over and health loss in red
                        player_health = 0 # Set player health to 0
                        chef_help = False # End chef help loop
                        scene_five_loop = False # End scene 5 loop
                        break # Exits loop

                    elif 'help' in other_ingredient.lower():
                         print(chalk.green_bright("Froggy the Guide:"), "Hmmm, well if we think about this rationally, you should try either the extra sugar or the eggs. They both seem pretty good to me!") # Give a hint

                    elif 'quit' in other_ingredient.lower():
                        quit_game() # Quit game
                        
                    else:
                         print(chalk.red('This is not an option, please try again.'))    # Invalid input message
        
        else:
            print(chalk.red('This is not an option. Please Try Again')) # Invalid input message
            time.sleep(2) # Delay text by 2 seconds

# Scene 6
def scene_six(): # Scene 6 function
    scene_six_loop = True # Set flag for scene 6 loop
    while(scene_six_loop == True): # Loop until scene is completed
        time.sleep(3) # Delay text by 3 seconds
        clear_screen() # clear screen
        animate_text(scene_six_text[0]) # Display initial text for scene 6
        animate_text(chalk.grey(scene_six_text[1])) # Display additional text
        test_bridge = input (scene_six_text[2]) # Prompt the player to test the bridge
        if 'test' in test_bridge.lower(): # If player chooses to test bridge
            animate_text(scene_six_text[3])
            animate_text(scene_six_text[4])
            while ('Note' not in player_inventory):
                read_note = input(scene_six_text[5]) # Prompt player to read the note
                if 'yes' in read_note.lower(): # If yes to read not
                    player_inventory.append('Note') # Add note to player inventory
                    animate_text(chalk.grey(scene_six_text[6])) # Display text in grey
                    animate_text(scene_six_text[7])
                    time.sleep(2) # Pause for 2 seconds
                    animate_text(scene_six_text[8])
                    animate_text(chalk.grey(scene_six_text[9]))
                    swing = False # Set flag for swinging across bridge
                    while (swing == False): # Loop until player swings across bridge
                        swing_across = input(scene_six_text[10]) # Prompt player to swing across bridge
                        if 'yes' in swing_across.lower(): # If yes in swing across
                            swing = True # End swing loop
                            animate_text(scene_six_text[11])
                            scene_six_loop = False # End scene 6 loop
                            break # Exit loop
                        elif 'no' in swing_across.lower(): # If no in swing across
                            animate_text('Its getting dark, I think you should swing across') # Prompt player to swing across
                        else:
                            print(chalk.red('This is not an option. Please try again!')) # Invalid input message
    
                elif 'no' in read_note.lower():
                    animate_text("\nThis note looks like the princess’ handwriting…..maybe its from her? Are you sure you don't want to read it?") # Prompt to reconsider reading the note
                else:
                    print(chalk.red('This is not an option. Try again!')) # Invalid input message
    
    
        elif 'cross' in test_bridge.lower(): # If player wants to cross bridge
            animate_text(scene_six_text[12])
            player_health = 0 # Set players health to 0
            print(chalk.red("\n-100 health")) # Display health loss in red
            print(chalk.red('\nGAME OVER')) # Display game over in red
            scene_six_loop = False # End scene 6 loop
            break # Exit loop
        else:
            print(chalk.red('This is not an option. Please try again!')) # Invalid input message

# Dragon damage
def dragon_damage(): # Function to inflict random dragon damage on the player
    global player_health # Access the global player_health variable
    random_damage = random.choice(dragon_damage_options) # Choose random damage from dragon_damage_options list
    # Apply damage based on the chosen value
    if random_damage == 100:
        animate_text(chalk.red(dragon_damage_text[0]))
        player_health = (player_health - 100) # Subtract 100 from player health
    elif random_damage == 75:
        animate_text(chalk.red(dragon_damage_text[1]))
        player_health = (player_health - 75) # Subtract 75 from player health
    elif random_damage == 50:
        animate_text(chalk.red(dragon_damage_text[2]))
        player_health = (player_health - 50) # Subtract 50 from player health
    elif random_damage == 25:
        animate_text(chalk.red(dragon_damage_text[3]))
        player_health = (player_health - 25) # Subtract 25 from player health
    elif random_damage == 10:
        animate_text(chalk.red(dragon_damage_text[4]))
        player_health = (player_health - 10) # Subtract 10 from player health
    elif random_damage == 0:
        animate_text(chalk.green(dragon_damage_text[5]))
        player_health = (player_health - 0) # Subtract 0 from player health
    else:
        print('')

# Dragon Item
def random_item_dragon(): # Function to give player a random item to defeat dragon
    random_item = random.choice(player_item_options) # Choose random item from player_item_options list
    if random_item == 'Pencil':
        animate_text(scene_seven_text[12])
        animate_text(chalk.gray('\nPencil added to Inventory')) # Add pencil to inventory in grey
        player_inventory.append('Pencil') # Add pencil to player inventory
    elif random_item == 'Ruby Ring':
        animate_text(scene_seven_text[13])
        animate_text(chalk.gray('\nRuby Ring added to Inventory')) # Add ruby ring to inventory in grey
        player_inventory.append('Ruby Ring') # Add ruby ring to player inventory
    elif random_item == 'Golden Pizza':
        animate_text(scene_seven_text[14])
        animate_text(chalk.gray('\nGolden Pizza added to Inventory')) # Add golden pizza to inventory in grey
        player_inventory.append('Golden Pizza') # Add golden pizza to player inventory

    else:
        print('')

# Scene 7
def scene_seven(): # Scene 7 function
    global player_health # Access the global player_health variable
    global dragon_health # Access the global dragon_health variable
    scene_seven_loop = True # Set a flag for scene 7 loop
    while(scene_seven_loop == True): # Loop until scene is completed
        if dragon_health > 0:
            time.sleep(3) # Delay for 3 seconds
            clear_screen()  # Clear screen
            print(chalk.grey(scene_seven_text[0])) # Display text in grey
            animate_text(scene_seven_text[1])
            time.sleep(1) # Delay for 1 second
            random_item_dragon() # Give the player a random item from the dragon
            time.sleep(2) # Delay for 2 seconds
            animate_text(scene_seven_text[2])
            while(dragon_health > 0): # Loop until the dragon is defeated or the player is dead
                    if player_health > 0:
                        time.sleep(3) # Pause for 3 seconds
                        clear_screen() # Clear screen
                        animate_text(chalk.gray(scene_seven_text[3])) # Display text in grey           
                        print(chalk.red('\nDragon Health:' + str(dragon_health))) # Show dragons health in red
                        print(chalk.green(' Player Health:' + str(player_health))) # Show player's health in green
                        animate_text(chalk.grey('\nInventory: ') + str(player_inventory))        # Display player's inventory in grey
                        dragon_weapon = input(scene_seven_text[4]) # Prompt the player to choose a weapon
                        if ('sword' in dragon_weapon.lower()) and ('Sword' in player_inventory):   # If player uses sword and has sword in inventory
                                animate_text(scene_seven_text[5])
                                print(chalk.green('\n-75 Damage to Dragon')) # Display damage to dragon in green
                                dragon_health = (dragon_health - 75) # Subtract 75 from dragon health
                                dragon_damage() # Inflict random dragon damage on the player
                        elif ('apple' in dragon_weapon.lower()) and ('Apple' in player_inventory):
                                animate_text(scene_seven_text[6])
                                print(chalk.green('\n+100 Health')) # Display health gain in green
                                player_health = (player_health + 100) # Add 100 to player's health
                                player_inventory.remove('Apple') # Remove apple from inventory
                        elif ('banana' in dragon_weapon.lower()) and ('Banana' in player_inventory): # If player uses banana and has banana in inventory
                                animate_text(scene_seven_text[7])
                                print(chalk.red('\n-75 Health')) # Display health loss in red
                                player_health = (player_health - 75) # Subtract 75 from player's health
                                player_inventory.remove('Banana') # Remove banana from inventory
                        elif ('rope' in dragon_weapon.lower()) and ('Rope' in player_inventory):   # If player uses rope and has rope in inventory
                                animate_text(scene_seven_text[8])
                                print(chalk.green('\n-25 Damage to Dragon')) # Display damage to dragon in green
                                dragon_health = (dragon_health - 25) # Subtract 25 from dragon's health
                                dragon_damage() # Inflict random dragon damage on the player
                        elif ('pencil' in dragon_weapon.lower()) and ('Pencil' in player_inventory):
                                animate_text(scene_seven_text[9])
                                print(chalk.red('\n0 Damage to Dragon')) # Display 0 damage in red
                                dragon_damage() # Inflict random dragon damage on the player
                                player_inventory.remove('Pencil') # Remove pencil from inventory
                        elif ('golden pizza' in dragon_weapon.lower()) and ('Golden Pizza' in player_inventory): # If player uses golden pizza and has golden pizza in inventory
                                animate_text(scene_seven_text[10])
                                print(chalk.green('\n+200 Health')) # Display health gain in green
                                player_health = (player_health + 200) # Add 200 to player's health
                                player_inventory.remove('Golden Pizza') # Remove golden pizza from inventory
                
                        elif ('ruby ring' in dragon_weapon.lower()) and ('Ruby Ring' in player_inventory): # If player uses ruby ring and has ruby ring in inventory
                                animate_text(scene_seven_text[11])
                                print(chalk.green('\n-150 Damage to Dragon')) # Display damage to dragon in green
                                dragon_health = (dragon_health - 150) # Subtract 150 from dragon's health
                                dragon_damage() # Inflict random dragon damage on the player
                
                        else:
                                print(chalk.red('This is not an option or not able to be used for fighting! Please try again.')) # If the player provides an invalid input or uses an unsuitable item
                                continue # Continue to the next iteration of the loop
                    elif player_health <=0: # If the player's health is 0 or less
                        print(chalk.red('\nGame Over')) # Display game over message in red
                        scene_seven_loop = False # End scene seven loop
                        dragon_health = 0 # Set dragon's health to 0
                        quit_game() # Quit the game
                        break # Exit the loop
                    else:
                        print('')
        elif dragon_health <= 0:
            print(chalk.yellow(chalk.bold('\nYOU DEFEATED THE DRAGON!'))) # Display victory message in green
            scene_seven_loop = False # End scene seven loop

        else:
            print('')
# Scene 8
def scene_eight(): # Function for scene 8
    animate_text(str(scene_eight_text[0])) # Display initial text
    chocolate_princess_loop = True # Set flag for chocolate princess interaction
    while chocolate_princess_loop: # Loop until the player completes the interaction with the princess
        chocolate_princess = input(chalk.yellow("\n\nPrincess: ") +  str(scene_eight_text[1])) # Prompt the player for interaction with the princess
        # If the player responds with "no" and has chocolate in the inventory
        if ('no' in chocolate_princess.lower()) and ('Chocolate bar' not in player_inventory):
            animate_text(chalk.yellow("\nPrincess: ") + str(scene_eight_text[2])) # Display princess's dialogue in yellow
            print(chalk.grey(str(scene_eight_text[3]))) # Display text in grey
            print(chalk.red(str(scene_eight_text[4]))) # Display text in red
            time.sleep(2) # Delay for 2 seconds
            print(str(scene_eight_text[5]))
            clear_screen() # Clear screen
            quit_game() # Quit the game

        elif "help" in chocolate_princess.lower():
             print(chalk.green_bright("Froggy the Guide:"), "I sure would be hungry if I was locked in a tower") # Give a hint
             time.sleep(2) # Delay for 2 seconds
             clear_screen() # Clear screen

        elif "quit" in chocolate_princess.lower():
            quit_game() # Quit the game

        # If the player responds with "yes" and has chocolate in the inventory
        elif ("yes" in chocolate_princess.lower()) and ('Chocolate bar' in player_inventory):
            animate_text(chalk.grey(str(scene_eight_text[6]))) # Display text in grey
            animate_text(chalk.bold(str(scene_eight_text[7]))) # Display bold text
            animate_text(chalk.bold(str(scene_eight_text[8]))) # Display additional bold text
            time.sleep(2) # Delay for 2 seconds
            clear_screen() # Clear screen
            quit_game() # Quit the game
            chocolate_princess_loop = False # End chocolate princess interaction

        #If user provides invalid input
        else:
            print(chalk.red('This is not an option. Please try again!')) # Invalid input message
            time.sleep(2) # Delay for 2 seconds
            clear_screen() # Clear screen
        
        
              
#THE END

# Start the game
game_intro()
start_game()
scene_one()
scene_two()
scene_three()
scene_four()
scene_five()
scene_six()
scene_seven()
scene_eight()
