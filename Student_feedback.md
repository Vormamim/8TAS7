# Student feedback

## Reha, Diya and Amilia


Strong Points:

Well-structured game flow with clear scene transitions and modular functions
Good use of global variables for tracking game state (player_location, game_over, potion)
Excellent implementation of text animation and timing effects for storytelling
Smart use of threading for timed input challenges
Clear location management using a list data structure
Interactive choices with input validation loops
Engaging story progression with branching paths
Good file handling for external text content
Clear comments explaining code functionality
Effective use of clear_screen() for better user experience

User and Developer Feedback

Threading implementation for timed challenges work well (supplied)
Text animation system for engaging output with text an appropriate lenght
Impressive story telling and progression
Modular scene system making the code maintainable
Input validation with while loops
Global state management
File I/O handling with proper encoding
impressive logic used: if x in [yes, y, yes], if x in [no, n, no] in impressive skill development
No errors in the code itself, but the text files were not supplied initially.


Areas for Enhancement:
text files not supplied at submistion. Testing the code would had identify the issue.
text animation and timing effects could be more polished. Text tends to run too fast (user experience)
Speed of text animation could be controlled by a variable or user choice (slow, middle, fast)
Use of colours would help break up the  text and make it more visually appealing



## Xavier Dickeson, Benjamin Saunders, Jace Saengmanee, Justin Liu
Strong Points:

Well-structured text adventure game with multiple endings and branching storylines
Good use of game state management through global variables and conditions
Nice implementation of text animation and screen clearing for better UX
Rich narrative with detailed story elements and character interactions
Multiple gameplay mechanics including inventory system, location navigation, and decision points
Clear action system with defined commands like 'take', 'look', 'help', etc.
Good use of color coding for different types of text output using chalk library
Areas for Enhancement:

The code could benefit from organising the locations data into a dictionary for easier access
Some functions like basicFunctions() could be more modular
Adding docstrings would make the code more maintainable
The story variables could be consolidated into a game state object
Input validation could be strengthened in some areas
Technical Implementation Highlights:

Good use of Python standard libraries (os, sys, time)
Clean implementation of text-based UI
Smart use of boolean flags to track game progress
Well-thought-out location navigation system
Effective inventory management system
The code creates an engaging text adventure with meaningful choices and consequences, while maintaining good code organization and readability.

*Errors*
there are a few technical errors in the code:

In the wifeNpc() function, there's a syntax error with an unmatched parenthesis in the animateText(celebrationText() line

Some global variables are referenced before being defined:

gotMary in the house() function
stablesFirstTime in the stables() function
action is used in multiple functions but not always properly declared global
The displayLocation() function takes a location name but in some calls it's given the entire locations list

In the basicFunctions() function, the locations parameter is undefined when passed to displayLocation()

These were be fixed by:

Adding proper global declarations
Initialising all state variables at the start
Correcting the function parameters
Completing the unfinished celebrationText() call
Some minor syntax errors (bugs)

The core game logic and structure are solid - these were straightforward fixes that didn't impact the overall gameplay design. The use of narrative was exceptional and the colour changes were a nice touch.
Comments were clear and the code was well-structured. However the commentss could be improved by providing more detail on the purpose of each function and variable.


## phoebe greenwood, matilda Jackson, amelia rutherford

Excellent modular design
The typewriter effect function creates engaging text output

Functions have clear single responsibilities

Code ran without any errors

Control Flow
Strong use of while loops for input validation
Good nested if-else structures for decision branching
Effective use of break statements to control game flow

Input/Output
Robust input handling with .strip() and .lower() for consistency
Creative use of typewriter_print() for text display
Clear prompts for user input

Variables & Data Types
Good use of descriptive variable names (sandwichforbarb, lighthouseentry)
Appropriate use of strings and booleans
Simple but effective list usage (listforpack)

Narrative & User Experience
Engaging storyline with Barbie theme
Multiple story branches based on user choices
Good pacing with clear_screen() and time.sleep()
Creative narrative twists and dark humor elements

Error Handling
Input validation loops ensure valid responses
Help system available for user guidance
Quit functionality implemented

Areas for Enhancement:

Comments
More inline comments explaining complex logic
Section headers could be more consistent

Structure
Some repeated code could be consolidated into functions
Long text strings could be stored separately
Main game loop could be more structured

Variables
Some variables could have more consistent naming conventions
Some unused variables (listforpack)

Control Flow
Some nested if statements could be simplified
Break statements could be more consistently used
Some redundant condition checks

## William, Kai


Strong Points:

Well-structured combat system with clear attack and healing mechanics
Good use of random number generation for combat variability
Nice implementation of text animation for storytelling
Clear game state management through global variables
Interactive combat choices with basic input validation
Engaging boss fight mechanics with dodge chances
Good implementation of healing system with maximum health cap
Clear function separation for different combat actions
Technical Implementation Highlights:

Good use of Python standard libraries (random, sys, time)
Clean implementation of text-based UI with animated text
Smart use of while loop for continuous boss battle
Effective health and potion management system
Well-thought-out combat turn system

Areas for Enhancement:

Combat Balance:
Adjust healing values to match documented amounts
Balance player/boss damage ratios
Fine-tune dodge chances
Code Structure:
Add player death condition
Implement proper file handling with context managers
Add more varied combat messages
Include clear game rules introduction
The code creates an engaging boss battle system with meaningful choices and consequences, while maintaining good code organization and readability. The combat mechanics are solid and the narrative elements add depth to the gameplay experience.

Code files are not connected and the game itself is not directly playable without some modifications.
However the code is well-structured and the game mechanics are solid. The use of multiple files and functions makes the code more modular and easier to maintain.

Some more use of lists to control the flow of the game would be beneficial.


## Oscar, Aiden

The code shows clear signs of being derived from teacher-provided core structures, particularly in the scene-based progression system. While it uses classes which weren't in the course prerequisites, the implementation reveals:

Direct adoption of the scene-based structure seen in other student works
Similar narrative flow patterns (scene1, scene2, etc.)
Familiar health/inventory management systems

The code does show some original elements:

Custom random events in the forest scene
Unique branching paths with Khaleed character
Health management system with multiple ways to gain/lose health
Integration of the chalk library for colored output
The core game mechanics and scene progression are heavily influenced by the teacher's template, but there are attempts to build upon it with additional features. This suggests the students understood the base concepts but relied heavily on existing structures rather than creating their own unique implementation.

A more independent approach would have been to create their own scene structure and game flow while still maintaining the text adventure format within the course constraints.

Class structures are not taught and the use of classes is not a prerequisite for the course. It is however a sign of using GenAI and not a sign of understanding the course content or following policy around using GenAI and academic honesty.

Log book Oscar is empty and shows no evidence of the student working on the assignment. 20% deduction as Aidens logbook indicate he was far more involved in the assignment.

## Michela Rospigliosi Chocano, Ellyana Rains, Sarah Tang, Zoe Laffan

Strong Points:

Excellent modular design with clear function separation for each scene
Strong use of global state management through player_inventory and health variables
Creative implementation of random dragon damage and item generation systems
Good use of color coding with chalk library for different character dialogues
Good input validation with consistent lowercase handling
Well-structured game flow with clear scene transitions
Good use of time.sleep() for pacing and clear_screen() for readability
Rich narrative with multiple branching paths and consequences
Smart implementation of inventory system

### Technical Implementation Highlights:

Effective use of while loops for scene control and input validation
Good implementation of combat mechanics with health tracking
Strong random number generation for combat variability
Clear function responsibilities (dragon_damage, random_item_dragon)
Good use of Python standard libraries (random, time, os, sys)
The combat system and inventory management are particularly well implemented.


### Areas for Enhancement:

Scene text could be moved to separate files to improve maintainability
Some repeated input validation code could be consolidated into helper functions
Long text strings could be broken into smaller chunks
Some functions are quite long and could be split into smaller sub-functions
Comments could provide more detail about function purposes

No major errors found

## Heritika, Elizabeth

### Strengths:

Excellent use of functions to structure the game into distinct scenes
Good implementation of a location-based system with descriptions and exits
Strong use of global variables for player inventory and location tracking
Creative use of the chalk library for colored text output
Well-implemented input validation and error handling
Good use of randomization for items and events
Engaging narrative with multiple paths and consequences
Effective use of time delays and text animation for pacing

### Game mechanics:

Solid inventory system with item usage mechanics
Good implementation of movement between locations
Interesting use of a boat for special movement
Creative use of a torch and battery mechanic for progression

### Narrative:

Engaging storyline with a mysterious and foreboding atmosphere
Good use of descriptive text to set the scene
Multiple endings based on player choices
Interesting twist with the "not-so-mythical" dragon


### 
Improvements:

Reduce code repetition, especially in the scene functions
Implement a main game loop to handle scene transitions more efficiently
Use dictionaries or classes to manage game state and reduce global variables
Improve code organization by grouping related functions together
Add more comments to explain complex logic
Implement a save/load system for game progress
Expand the narrative with more diverse outcomes and player choices
Overall, this is an impressive project, showcasing a good understanding of core programming concepts and game design principles.
More than ready to tackle Software Engineering in the future (wink)


### Caelen, Adrian, Cedric

The code implements a text-based adventure game with a grid-based map system, inventory management, and various scenes and interactions.

The well done bits

Well-structured map system using a 2D grid
Player movement and location tracking
Inventory system with permanent and temporary items
Multiple scenes and interactions (Beach, Manor, Town Square, Shop, Docks, Cave)
Minigames and challenges (word typing game, robot fight)
Use of external text files for intro and fight scenes
Clear screen functionality for better user experience
Good use of time delays for pacing the story
The code demonstrates good organization with separate functions for different scenes and actions. It uses global variables to manage game state across functions.

### Areas for potential improvement:

Consider using classes to encapsulate related functionality and state
Implement error handling for user inputs
Refactor repeated code blocks into reusable functions
Use more descriptive variable names in some cases
Text is descriptive and moves the story forward, but could be more engaging.

### Vanessa, Hayley

This is an impressive piece of work for a beginner Python student! Let's break down the strengths:

Narrative Strengths:

Excellent atmospheric storytelling with vivid descriptions of the haunted hospital setting
Well-paced story progression from the dramatic opening scene to the exploration phase
Creative use of chalk colors to differentiate narrative text types
Strong horror/survival theme maintained throughout
Engaging descriptions that build tension ("discarded debris", "ghostly whispers", "eerie shadows")

Gameplay Elements:

Clear core mechanics: exploration, inventory management, health system
Smart use of interconnected locations with logical navigation
Meaningful item collection and usage (flashlight needed for dark areas, key for locked doors)
Good tension building with random entity encounters
Strategic elements like health management and item choices
Compass system provides helpful guidance without being too direct
Technical Implementation:

Clean function organisation for different rooms and actions
Good use of global state management for player location and inventory
Effective input validation and command processing
Nice quality-of-life features like screen clearing and text delays
Smart use of lists for items, locations, and entities

The code shows strong foundational understanding of:
 
Functions and scope
Control flow (if/elif/else, while loops)
Lists and list operations
Input/output handling
String manipulation


This is a well-structured text adventure that successfully combines storytelling with gameplay mechanics in an engaging way. The code is clean, well-commented, and demonstrates a good understanding of Python fundamentals.


### Isabella, Geetika, Juliet, Miel

Code Structure:

Excellent organization with clear function definitions for different scenes and actions
Smart use of global variables for tracking game state (health, inventory, location)
Well-separated functions for different rooms and actions
Clean implementation of utility functions like cls() and quit_game()

Data Types:

Good use of lists for inventory, locations, actions, and items
Appropriate use of strings for text and player input
Smart use of integers for health tracking
Effective use of boolean for game state

Conditionals:

Strong implementation of nested if-else statements for decision branching
Good input validation throughout
Effective use of condition checking for items in inventory
Smart room access controls (requiring keys/items)

Gameplay:

Engaging inventory system
Health management with healing items
Random entity encounters add unpredictability
Multiple rooms to explore with different items
Compass system provides helpful guidance
Good balance of exploration and objective gathering
Narrative:

Strong atmospheric writing creating a spooky hospital setting
Good use of chalk library for color-coded text
Well-paced story progression
Detailed room descriptions
Engaging horror elements with ghosts and entities
The code shows excellent understanding of fundamental programming concepts while creating an engaging game experience. The combination of exploration, inventory management, and survival elements makes for a compelling text adventure.


### Louis, George

Strong Points:

Excellent use of modular design with clear function separation for different game mechanics

Smart implementation of colored text output using yachalk for different types of messages:

Yellow for dialogue
Green for game output
Red for errors
Well-structured location system using dictionaries with:

Clear descriptions
Logical exits
Item management
Monster placement
Connected navigation paths
Good implementation of core game mechanics:

Inventory system
Movement between locations
Scene management
Text animation for better user experience
Strong technical fundamentals:

Clean imports
Global state management
Input validation
Error handling

Suggestions for Enhancement:

Add combat system to interact with the monsters defined in locations
Implement the item usage system (the 'use' action is in the actions list but not implemented)
Complete scene_two() and scene_three() functions
Add save/load game functionality
Consider adding character stats or leveling system
The code shows excellent organization and demonstrates solid understanding of Python fundamentals. The game structure provides a strong foundation for expanding the adventure with additional features and content.

Issues:
Much of the code is a slight modification of the provided code, with some minor changes to the functions and variables.
Dictionaries were not taught or expected, so question the advanced use of dictionaries in this code.
Scenes are not connected, and the game does not progress beyond the first scene.
Overall,the this shows a developing understanding of Python fundamentals and the ability to adapt and modify existing code. However, there is room for improvement in terms of creating more complex game mechanics and expanding the story.
Overall, this is a poor effort and does not meet the requirements of the assignment.
You have not used the time provided to create a game that is engaging and enjoyable for the user independently.
George submitted nothing and there is no evidence of any work being done.
There is no game manual.

### stanley, euan, eziekial, fletcher

Scene transitions follow a similar pattern of:

Display text
Get choice
Validate input
Show consequences

you could:

Create a single input validation function that takes valid choices as parameters
Make a unified text animation function with speed options
Store common text patterns in variables
Create a standard scene transition function

Comments:

Clear color code comments at the top
Could benefit from more inline comments explaining complex logic
Function purposes could be better documented

Variables & Data Types:

Good use of color constants with clear naming
Appropriate use of strings for text and user input
Boolean flag 'visited_1_or_3' tracks game state
Strong use of string formatting with color codes

Functions:

Excellent variety of text animation functions with different speeds
Clear function separation for different scenes
Good modular design with single-purpose functions
Smart implementation of blood_processor() for verification
Effective file handling with loadText() functions

Input/Output:

Consistent input validation in choice loops
Good use of colored text output for different characters/situations
Clear user prompts and feedback
Nice implementation of animated text output

Lists:

Good use of list operations in binary code generation
Could expand use of lists for storing choices and game states

Conditionals:

Strong if-elif-else structures for decision branching
Good validation of user choices
Clear consequence handling for different paths

Loops:

Effective while loops for input validation
Good use of for loops in text animation
Smart loop control with break statements

'''
while True:
    choice = input("")
    if choice == "something":
        # do stuff
    elif choice == "something else":
        # do other stuff
    else:
        animate_text("Invalid input, try again.", Yellow)
'''


Code Quality:

Clean, consistent formatting
Good function organisation
Clear variable naming
Well-structured scene progression

Gameplay:

Engaging detective mystery theme
Multiple paths and choices
Consequences for player decisions
Good balance of exploration and challenge

Narrative:

Strong atmospheric storytelling
Good character dialogue
Clear progression through the mystery
Engaging crime scene investigation elements
Overall, the code demonstrates strong fundamentals with room for some minor enhancements in documentation and data structure usage

The dialogue and interaction elements show strong design choices:

Character Voices:

Distinct character voices through color coding (Blue for Constable, Green for Sergeant, White for player)
Clear role identification through dialogue style
Natural conversational flow between characters

Interactive Elements:

Multiple meaningful choice points that affect story progression
Engaging mini-games like the binary code memory challenge
Investigation mechanics with different areas to explore (workbench, storage shelf, tool rack)
Consequences for player decisions (like the beartrap scenario)

Narrative Flow:

Good scene transitions with clear progression
Building tension through evidence collection
Mystery elements revealed gradually
Environmental storytelling through scene descriptions

Meaningful choices in evidence processing
Multiple investigation paths
Different tools/items to collect and use
Strategic decisions in approaching the killer

#### end