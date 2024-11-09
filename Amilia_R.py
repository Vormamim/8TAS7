import sys
import os
import random
import time #this line imports time so that we can use the time.sleep() fucntion
import io
import threading #this is used later on to create a timer

# variables
player_location = 'the House'
game_over = False
potion = 0

locations = [ #This is a list that stores all the locations 
    ['the Pathway', 'You climb out of the window and reach a path', 'A path surrounded by trees and flowers, and a castle in the distance'],
    ['the Forest', 'You step into the forest, where the trees whisper and the air is fresh.', 'The sunlight filters through the leaves, and you hear a tree calling for your attention.'],
    ['the River', 'You wade into the river, feeling the cool water rush around you.', 'A shimmering fish swims by, and its eyes seem to sparkle with wisdom.'],
    ['the Entrance', 'You look up to find a towering castle that looms ahead, its stone walls entwined with enchanted vines that shimmer with a faint, magical glow. Its entrance is blocked by a rusted metal gate.'],
    ['the House', 'You are at the start of the game.', 'A house filled with personalized furniture and posters of cats, as well as the warm and welcoming presence of John and Mary.'],
    ['the Castle', 'You stare in awe at the grand hall, high ceilings, stone walls draped in tapestries, glowing chandeliers, and the roaring fireplace.']
]

# functions
#these are all functions that are sections of code that are only used when they are called
def clear_screen(): #this function clears the screen to make it less chaou=tic
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.01): #This function animates the text 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def display_location(location_name): #This displays the location from the locations list
    for location in locations:
        if location[0] == location_name:
            print('You are at ' + ', '.join(location))

def read_text(text_file): #This opens a text file, prints it, and then closes it so it doesn't lock
    with open(text_file, 'r',encoding='utf8') as f:
        text = f.read()
        f.close()    
        return text
    
def timer_input(prompt, timeout): #This is a timer input that sets a timer for a certain amount of seconds
    user_input = [None]
    input_thread = threading.Thread(target=lambda: user_input.__setitem__(0, input(prompt)))
    input_thread.start()
    input_thread.join(timeout)
   
    if input_thread.is_alive():
        print("\nTime's up! You failed.")
        return None
    else:
        return user_input[0]


# Game scenes
#Each scene is a function which the gets called in the main game loop
def scene_one(): 
    display_location('the House') #This calls the function and displays the location
    animate_text('You are Amber. A fluffy orange cat that is practically the daughter of John and Mary.')
    print()
    time.sleep(0.7)
    animate_text('You love John and Mary, but you have always dreamed of going on an adventure.')
    print()
    time.sleep(0.7)
    animate_text('One day, when they leave for work, you decide to escape.')
    print()
    time.sleep(0.7)

def scene_path():
    global game_over, potion
    display_location('the Pathway')
    animate_text(read_text('scene_path.txt')) #This calls the read_text function and prints a text file 
    time.sleep(0.7)
    print()
    while True: #A while loop is executed as long as the statement is true
        lev_powder = input("Do you want to take the levitation powder? (yes/no): ").lower()
        if lev_powder in ['yes', 'no']:
            break #This stops the loop from repeating infinitely
        else:
            animate_text("That is not a valid option.")
            print()
            time.sleep(0.7)
    if lev_powder == 'yes': # this is an if statement, this allows the use to make a descion, with each decison having a different outcome
        potion = potion + 1
        animate_text("You take the packet and thank the cat.")
    else:
        animate_text("You do not take the powder from the cat.")
    print()
    time.sleep(0.7)
    animate_text("You say goodbye to the cat and continue on the path until you reach a river. To the left, there is a forest.")
    print()
    time.sleep(0.7)
    while True:
        path = input("Do you go down the river or through the forest? (river/forest): ").lower()
        if path in ['river', 'forest']:
            break
        else:
            animate_text("That is not a valid option.")
            print()
            time.sleep(0.7)
    if path == 'forest':
        scene_forest() #The choice of the usser determine which function isnext
    else:
        scene_river()


def scene_forest():
    global game_over
    display_location('the Forest')
    animate_text(read_text('forest_scene.txt'))


def scene_river():
    global game_over
    display_location('the River')
    animate_text(read_text('river_scene.txt'))


def scene_gate():
    global game_over
    display_location('the Entrance')
    print()
    time.sleep(0.7)
    animate_text("You try to open the gate, but no matter how hard you push it, it won't budge.")
    print()
    time.sleep(0.7)
    animate_text("'You thought it would be that easy?' says a loud booming voice.")
    print()
    time.sleep(0.7)
    animate_text("'In order to open the gate you must answer a riddle.'")
    print()
    time.sleep(0.7)
    animate_text("'I'll give you 5 attempts'")
    print()
    time.sleep(0.7)
    answer = input("What can’t talk but will reply when spoken to?' ")
    lives = 4
    while lives > 0: 
        if answer.lower() == "echo" or answer.lower() == "an echo":
            print('That is correct!')
            print()
            time.sleep(0.7)
            animate_text("There is a loud squeaking noise as the rusted metal gates open.")
            print()
            time.sleep(0.7)
            animate_text("You slowly wander towards the interior.")
            break
        else:
            lives = lives - 1
            print('That is incorrect. Please try again')
            answer = input("What can’t talk but will reply when spoken to? ")
    if lives == 0:
        print('You have run out of lives')
       
        print('GAME OVER')
        game_over = True


   
#TODO: Raha
def scene_fairy():
    global game_over, potion
    fail = ("You were unable to save the fairy") #This is a variable which helps reduce rewriting the same line multiple times
    display_location('the Castle')
    print()
    time.sleep(0.7)
    animate_text("As you begin to explore, you hear a faint whimpering noise coming from ahead.")
    print()
    time.sleep(0.7)
    animate_text("You begin aproach where the noise is coming from and find a fairy clutching her wing")
    print()
    time.sleep(0.7)
    animate_text("'Is everything ok?' you ask her, concern rushing over you")
    print()
    time.sleep(0.7)
    animate_text("'Please help me!' she cries")
    print()
    time.sleep(0.7)
    animate_text("'I hurt my wing when I was trying to clean the windows, and now I cant fly!'")
    print()
    time.sleep(0.7)
    animate_text("'Of course I can help you!' you say as you look at your surroundings in hopes that you can find something to help her")
    print()
    time.sleep(0.7)
    animate_text("Three objects on top of a bookshelf catch your eye. A sandwich, a stick and a flask containing an unkown liquid")
    print()
    time.sleep(0.7)
    while True:
        
        object=input("What do you think will help the fairy? The sandwich, the stick or the flask? ")
        if object.lower() in ('sandwich', 'the sandwich', 'a sandwich'):
            animate_text("You hand the fairy the sandwich and she starts to eat it ")
            print()
            time.sleep(0.7)
            animate_text("However, her wing doesn't seem to be healing")
            print()
            time.sleep(0.7)
            animate_text("You realise a sandwich probably isn't the best solution for a broken wing")
            print()
            time.sleep(0.7)
            print(fail)
            print('GAME OVER')
            game_over = True
            break
        
        elif object.lower() in ('flask', 'the flask', 'a flask'):
            animate_text("You take the flask and hand it to the fairy")
            print()
            time.sleep(0.7)
            animate_text("She begins to drink but nothing seems to happen")
            print()
            time.sleep(0.7)
            animate_text("Then suddenly...")
            print()
            time.sleep(4) #It pauses for longer to build suspense
            animate_text("She falls asleep!")
            print()
            time.sleep(0.7)
            animate_text("There was a sleeping potion in the flask!")
            print()
            time.sleep(0.7)
            print(fail)
            print('GAME OVER')
            game_over = True
            break
        
        elif object.lower() in ('stick', 'the stick','a stick'):
            animate_text("You pick up the stick and notice that it is glowing")
            print()
            time.sleep(0.7)
            animate_text("'Is this a wand?' you think to yourself, anticipation building up inside you")
            print()
            time.sleep(0.7)
            animate_text("You raise the wand in the air and wave it around")
            print()
            time.sleep(0.7)
            animate_text("Suddenly a cloud of fog appears around the fairy and dissapears after a second")
            print()
            time.sleep(0.7)
            animate_text("You look up to find the fairy flying in the air! You saved her!")
            print()
            time.sleep(0.7)
            animate_text("'Thank you so much for your help!' she exclaims as she reaches for her pocket and pulls out a small bag containing a pink, sparkly powder")
            print()
            time.sleep(0.7)
            animate_text("'Here, take this sleeping powder, it might help you later on' she says, handing you the bag")
            print()
            time.sleep(0.7)
            powder = input("Do you want to take the powder? ")
        if powder.lower() == 'no':
            animate_text("You thank the fairy but do not take the powder")
            print()
            time.sleep(0.7)
            animate_text("You continue ahead with your journey")
        elif powder.lower() == 'yes':
            potion = potion + 1
            animate_text("You take the powder from the fairy and she thanks you for your help")
            print()
            time.sleep(0.7)
            animate_text("You continue ahead with your journey")
        else:
            animate_text("That is not a valid option please try again")
            print()
            time.sleep(0.7)
            powder = input("Do you want to take the powder? ")
        break

   
   
#TODO: Raha
def scene_dragon():
    global game_over, potion
    animate_text("You reach the dragon's castle and see a group of cats caged! They evidently looked distressed, paws sweaty, meowing desperately.")
    print()
    time.sleep(0.7)
    animate_text("What are you going to do?")
    print()
    time.sleep(0.7)
    animate_text("If only there was a way to get the dragon to fall asleep")
    print()
    time.sleep(0.7)
    if potion == 2:
        animate_text("Then the realization hits you")
        print()
        time.sleep(0.7)
        animate_text("You can use the potion ingredients you recieved to make the dragon fall asleep!")
        print()
        time.sleep(0.7)
        animate_text("You combine the two ingredients and offer it to the dragon, saying it is a strength potion")
        print()
        time.sleep(0.7)
        animate_text("The dragon belives you and takes the potion, not suspecting a thing")
        print()
        time.sleep(0.7)
        animate_text("Suddenly, the dragon falls asleep and levitates in the sky")
        print()
        time.sleep(0.7)
        animate_text("Your plan is working!")
        print()
        time.sleep(0.7)
        animate_text("You crawl under the dragon and reach the cage where the cats are in")
        print()
        time.sleep(0.7)
        animate_text("But there is a slight problem")
        print()
        time.sleep(2)
        animate_text("The cage needs a code to open it!")
        print()
        time.sleep(0.7)
        animate_text("What could the code possibly be?")
        print()
        time.sleep(0.7)
        animate_text("You have 20 seconds to guess the code")
        print()
        time.sleep(0.7)
        animate_text("Your time starts NOW")
        print()
        timeout_seconds = 20
        result = timer_input("Code: ", timeout_seconds)
        code = ('123')

    if result is not None:
        print(f"You entered: {result}")
        if result == code:
            animate_text('You guessed the code and saved the cats!')
            print()
            time.sleep(0.7)
            animate_text('Congratulations, you have won!')
        else:
            animate_text('That is not the correct code')
            print()
            time.sleep(0.7)
            animate_text('You were unable to save the cats')
            print()
            time.sleep(0.7)
            print('GAME OVER')
            game_over = True


    else:
        print("You didn't guess the code in time")
        print("GAME OVER")
        game_over = True

    if potion != 2:
        animate_text("Since you didn't gather all of the potion ingredients, you weren't able to pass the dragon and save the cats")
        print()
        time.sleep(0.7)
        print('GAME OVER')
        game_over = True
        



  






   


# main game loop


clear_screen()
animate_text('Loading game...')
print()
time.sleep(1)
def main():
    global game_over
    scene_one()
    while not game_over:
        scene_path()
        clear_screen()
        if game_over: break
        scene_gate()
        clear_screen()
        if game_over: break
        scene_fairy()
        clear_screen()
        if game_over: break
        scene_dragon()
        if game_over: break
        break

main()

