#module
import sys
import os
import random
import time
#variables
#file = open('test.txt')
#content = file.readlines()
currentLocation = '0'
playerX = 0
playerY = 0
#imports
from monster import attackMonster, useHeal, monsterTurn, playerTurn, battleSequence, scene3
from finalboss import attackBoss, useHealBoss, bossAttack, playerTurnBoss, bossBattleSequence, scene5
enterBossFight = open('enteringBossfight.txt', 'r')
bossfightTXT = enterBossFight.read()


#Find random colours in the list for wire matching puzzle
colours = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
randColour1 = random.choice(colours)
colours.remove(randColour1)
randColour2 = random.choice(colours)
colours.remove(randColour2)
randColour3 = random.choice(colours)
colours.remove(randColour3)
randColour4 = random.choice(colours)
colours.remove(randColour4)
randColour5 = random.choice(colours)
colours.remove(randColour5)
randColour6 = random.choice(colours)
colours.remove(randColour6)

#Find random shapes in the list for square matching puzzle
shapes = ['square', 'triangle', 'circle', ]
randShape1 = random.choice(shapes)
shapes.remove(randShape1)
randShape2 = random.choice(shapes)
shapes.remove(randShape2)
randShape3 = random.choice(shapes)
shapes.remove(randShape3)
#Actions for fighting the monster and the Boss.



#Clears the terminal screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
#Shows location
def showLocation():
    print(f'You are in currently in {currentLocation}')
#Animates text       
def animateText(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def sceneOne():
    currentLocation = 'Research Facility'
    animateText('Scientist 1: The machine is almost complete, just a few more tweaks... \n')
    time.sleep(0)
    animateText('Scientist 2: Imagine it, teleportation within our grasp! \n')
    time.sleep(0)
    animateText('The labatory is a symphony of blinking lights and humming machines, the air thick with anticipation. The main console is sleek, with holographic displays of data floating in mid-air. I\'ve studied every parameter a thousand times over. My finger hovers over the button, ready to bridge the chasm between here and there. The atmosphere tingles with the potential of something incredible about to unfold.')
    animateText('The final button is under your fingers, do you wish to press it?: \n')
    startButton = input('yes/no: ').upper()
    if startButton == ('YES'):
        animateText('You hear the sound of a massive explosion, everything you see is lit up with orange and yellow, but before you die, a wormhole appears in front of you,\nYou jump in without looking in it and you get sucked into the wormhole.')
    elif startButton == ('NO'):
        animateText('You didn\'t press the big red button for some reason\n')
        animateText('The time machine exploded anyway and you died an unimaginable death.')

    else:
        print('That isn\'t an option')
    continue1 = input('Press any key to continue.')
    clearScreen()

def sceneTwo():
        currentLocation = 'Control Room'
        animateText('You awaken on the cold, hard floor of an abandoned warehouse, the air thick with the scent of rust and decay.\n')
        time.sleep(1)
        animateText('Sunlight filters through the broken windows high above, casting eerie shadows on the walls.\n')
        time.sleep(1)
        animateText('There is in front of you, a locked door...you spot a metallic box next to it.\n')
        time.sleep(1)
        #move to box??
        animateText('You open up the box and you see in front of you multiple wires inside the control box, all of them seems to be cut, looks like you have to match them up\n')
        time.sleep(1)
        print(f'You see a {randColour1} wire which wire do you connect it to?\n')
        #very horrendous
        wire1 = input(': ').lower()
        if wire1 == randColour1:
            animateText('wow! you got that correct!\n')
        else:
            print('how??')
            exit()
        wire2 = input(f'You see a {randColour2} wire, which wire do you connect it to?\n').lower()
        if wire2 == randColour2:
            animateText('wow! you got that correct!\n')
        else:
            print('how??')
            exit()
        wire3 = input(f'You see a {randColour3} wire, which wire do you connect it to?\n').lower()
        if wire3 == randColour3:
            animateText('wow! you got that correct!\n')
        else:
            print('how??')
            exit()
        wire4 = input(f'You see a {randColour4} wire, which wire do you connect it to?\n').lower()
        if wire4 == randColour4:
            animateText('wow! you got that correct!\n')
        else:
            print('how??')
            exit()
        wire5 = input(f'You see a {randColour5} wire, which wire do you connect it to?\n').lower()
        if wire5 == randColour5:
            animateText('wow! you got that correct!\n')
        else:
            print('how??')
            exit()
        wire6 = input(f'You see a {randColour6} wire, which wire do you connect it to?\n').lower()
        if wire6 == randColour6:
            animateText('wow! you got that correct!\n')
        else:
            print('how??')
            exit()
        animateText('The light next to the door lights up, and you open the door into outside the ruined building.')
        continue2 = input('Enter any key to continue.')
        clearScreen()

def sceneFour():
    #s is every less shape you have on you
    s = 3 
    animateText('As you approach the puzzle, you can see a puzzle with shapes on it.\nThe smooth, cold metal triangle, the weathered texture of a wooden square, and the polished glass circle. ')
    animateText('\nIt looks like you have to find the respective shapes to match onto the puzzle...')
    #if player location is 0,3, do following
    if playerY == 3 and playerX == 0:
        if s == 0:
            while s == 0:
                clearScreen()
                #no cheating :)
                puzzle2 = input('You have all the shapes, but what was the order?').lower
                #remove anything not answer in user input?
                if puzzle2 == f'{randShape1} {randShape2} {randShape3}':
                    animateText('You slotted in all the shapes and the door swiftly swung open to the next room')
                    s+=1
                else:
                    #to be fair most people would not try to check the puzzle first and instead find the shapes
                    animateText('You inputted the shapes wrong it seems. Try again?') 
        #if player has not gotten all shapes     
        else:
            animateText(f'You looked at the puzzle more closely, it looks like it\'s ordered as {randShape1}, {randShape2}, {randShape3}.')
    else:
         #pass is a placeholder
         pass
    if playerY == 0 and playerX == 3:
        animateText(f'You found the {randShape1}! You have {s} more shapes to find.')
        s -= 1
        if s == 0:
            animateText('Looks like you found all the shapes, you should return back to the puzzle.')
        else:
            pass
    else:
        pass
    if playerY == 0 and playerX == -3:
        animateText(f'You found the {randShape2}! You have {s} more shapes to find.')
        s -= 1 
        if s == 0:
            animateText('Looks like you found all the shapes, you should return back to the puzzle.')
        else:
            pass
    else:
        pass
    if playerY == -3 and playerX == 0:
        animateText(f'You found the {randShape3}! You have {s} more shapes to find.')
        s -= 1
        if s == 0:
            animateText('Looks like you found all the shapes, you should return back to the puzzle.')
        else:
            pass
    continue4 = input('Enter any key to continue.')
    clearScreen
    
    

#scenes, creating the game
def play_game():
    sceneOne()
    sceneTwo()
    scene3()
    sceneFour
    scene5()

#RUN THE GAME!!!
play_game()
#thanks for all the fish
