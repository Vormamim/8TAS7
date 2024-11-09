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
Technical Highlights:

Threading implementation for timed challenges
Text animation system for engaging output
Modular scene system making the code maintainable
Input validation with while loops
Global state management
File I/O handling with proper encoding

## Xavier Dickeson, Benjamin Saunders, Jace Saengmanee, Justin Liu
trong Points:

Well-structured text adventure game with multiple endings and branching storylines
Good use of game state management through global variables and conditions
Nice implementation of text animation and screen clearing for better UX
Rich narrative with detailed story elements and character interactions
Multiple gameplay mechanics including inventory system, location navigation, and decision points
Clear action system with defined commands like 'take', 'look', 'help', etc.
Good use of color coding for different types of text output using chalk library
Areas for Enhancement:

The code could benefit from organizing the locations data into a dictionary for easier access
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

These can be fixed by:

Adding proper global declarations
Initialising all state variables at the start
Correcting the function parameters
Completing the unfinished celebrationText() call
The core game logic and structure are solid - these are straightforward fixes that won't impact the overall gameplay design.
