import os
import random
import time

# Shortcuts that create the colour for text
Red = "\033[31m"
Blue = "\033[34m"
Green = "\033[32m"
Yellow = "\033[33m"
White = "\033[37m"
grey = "\033[90m"
# Animation speed functions
def animate_text(text, color_code):
    for char in text:
        print(f"{color_code}{char}\033[0m", end="", flush=True)
        time.sleep(0.1)
    print()

def quick_animate(text, color_code):
    for char in text:
        print(f"{color_code}{char}\033[0m", end="", flush=True)
        time.sleep(0.05)
    print()

def Slow_animate(text, color_code):
    for char in text:
        print(f"{color_code}{char}\033[0m", end="", flush=True)
        time.sleep(0.50)
    print()

def instant_animate(text, color_code):
    for char in text:
        print(f"{color_code}{char}\033[0m", end="", flush=True)
        time.sleep(0.0001)
    print()

def exit(status=0):
    animate_text("Exiting in 1 second....", Red)
    time.sleep(1)
    os._exit(status)
def process_evidence():
    animate_text("Do you want to process your evidence? (yes/no)", White)
    choice = input("").lower()
    if choice == "yes":
        while True:
            success = blood_processor()
            if success:
                Slow_animate("processing....", Red)
                animate_text("Success, the processor revealed that The Killers name starts with the letter 'T'", Yellow)
                break
            else:
                animate_text("Try again.", Yellow)
    elif choice == "no":
        animate_text("You chose not to process the evidence. You won't get info about the killer.", Yellow)
    else:
        animate_text("Invalid choice, you do not get the hint3", Yellow)

def blood_processor():
    animate_text("This action requires elevation by proving you are a detective.", Yellow)
    binary_code = ''.join(random.choice(['0', '1']) for _ in range(10))
    animate_text(f"Memorize and reproduce this binary code: {binary_code}", Yellow)
    answer = input("")
    return answer == binary_code
def loadingscreen():
    Slow_animate("Hotel Homicide", Red)
    print("")

def scene1():
    animate_text("Constable: “Hey Doc, we have a major case on our hands. And it's not clean ", Blue)
    print("")
    animate_text("Sergeant: “ Yeah about that, I have some blood samples and Chloe is on the way.”", Green)
    animate_text(" In the meantime head upstairs and check out the scene.", Green)
    print("")
    animate_text("You: Yes Sir.", White)

def scene2():
    animate_text("what do you investigate", grey)
    while True:
        choice = input("")
        if choice == '1':
            animate_text("the torn piece of fabric turned out to be from the victim, try again", Yellow)
        elif choice == '3':
            animate_text("you open the bottle of baby oil, unfortunately, the killer trapped it with an IED, You have been killed", Yellow)
            exit()
        elif choice == '4':
            animate_text("the severed finger turned out to be from the victim, this would be helpful, but we know she's dead, try again", Yellow)
        elif choice == '2':
            animate_text("you scanned the bloodstain, it didn't match the DNA of Zofia Bosak, this must be the killer's, You can send it in to get identification,", Yellow)
            process_evidence()
            break
        else:
            animate_text("Invalid input, try again.", Yellow)
    buffer()

def buffer():
    print()

def loadText():
    with open('text.md', 'r') as file:
        gameText = file.read()
        quick_animate(gameText, grey)

def loadtext2():
    with open('text.md1', 'r') as file:
        gameText = file.read()
        quick_animate(gameText, grey)
visited_1_or_3 = False
#scenes
def new_choices():
    global visited_1_or_3
    animate_text("You have three options: ", White)
    animate_text("1. Go to the police station and read up on criminals' names", Blue)
    animate_text("2. Visit the big mansion", Blue)
    animate_text("3. Check the web for suspects", Blue)

    while True:
        choice = input("Choose 1, 2, or 3: ")

        if choice == '1' or choice == '3':
            if blood_processor():
                Slow_animate("processing....", Red)
                animate_text("Success, the full name of the murderer is 'Tyler Grayson', you can now pick another choice", Yellow)
                visited_1_or_3 = True
            else:
                animate_text("Try again.", Yellow)

        elif choice == '2':
            if visited_1_or_3:
                animate_text("You arrive at a big mansion. You're certain Tyler Grayson is the murderer now.", Yellow)
                break
            else:
                animate_text("You need to be 100% sure this house belongs to the murderer. Try something else..", Yellow)
        else:
            animate_text("Invalid input, try again.", Yellow)

def scene3and4_downstairsandup():
    animate_text("You head downstairs. The dimly lit basement smells bad with cobwebs hanging from the corners.", White)
    animate_text("In the corner of the room, you see a few items scattered around.", White)

    # Providing multiple areas to investigate
    animate_text("You can investigate the workbench, the storage shelf, or the tool rack. Where do you want to look first?", White)
    while True:
        area_choice = input("Type 'workbench', 'storage shelf', or 'tool rack': ").lower()

        if area_choice == 'workbench':
            animate_text("You approach the workbench. It’s cluttered with various tools and objects.", White)
            animate_text("You see a knife with a sharp blade gleaming under the faint light.", White)
            item_choice = "knife"
            break
        elif area_choice == 'storage shelf':
            animate_text("You walk over to the storage shelf. It’s packed with old and rusty items.", White)
            animate_text("You spot a sturdy shovel that could be useful.", White)
            item_choice = "shovel"
            break
        elif area_choice == 'tool rack':
            animate_text("You check the tool rack. It’s organized with various protective gear.", White)
            animate_text("You find a pair of goggles that seem to be in good condition.", White)
            item_choice = "goggles"
            break
        else:
            animate_text("Invalid choice. You can investigate the workbench, the storage shelf, or the tool rack.", Yellow)

    # Additional exploration interactions
    animate_text(f"As you take the {item_choice}, you notice some gory details scattered around.", grey)
    animate_text("You see a dusty old book on the workbench, covered in blood.", grey)
    animate_text("There’s also a locked box on the storage shelf. You wonder what's inside.", grey)
    animate_text("Lastly, there's a spooky head. Just as you try to look thoroughly, you realise you have to deal with Tyler first.", grey)
    animate_text("", White)

    # Letting user know it's final
    animate_text(f"You chose the {item_choice}. Now, head upstairs to face Tyler Grayson.", White)
    choice = input("You head upstairs. You see a beartrap, do you avoid it? ").lower()

    if choice == "yes":
        animate_text("You avoid the beartrap and continue upstairs.", White)
    elif choice == "no":
        animate_text("You step on the beartrap. You silly goose, you die.", Red)
        exit()
    else:
        animate_text("Yes or no, bucko.", Yellow)

    print("You meet with the killer. You use your", item_choice, "to defeat him.")
# Inserting the new scene into your game sequence
loadingscreen()
time.sleep(1.5457)
loadText()
buffer()
time.sleep(1.8)
scene1()
loadtext2()
scene2()
new_choices()
scene3and4_downstairsandup()






