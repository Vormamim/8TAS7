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