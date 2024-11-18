# Define rooms
rooms = {
    "Entrance": {
        "description": "a grand entrance with carvings on the walls containing images of the golden pharaoh mask crested with diamonds running along the middle of the face leading down the back of the head.",
        "paths": {"north": "Hallway"}
    },
    "Hallway": {
        "description": "a long hallway with ancient paintings and cracked sandstone walls containing ancient scripts!",
        "paths": {"east": "Trap Room", "west": "Entrance", "south": "Entrance"}
    },
    "Trap Room": {
        "description": "a room filled with hidden traps. Be careful! You could fall in a hole filled with hungry, bloodthirsty diamondback python waiting for you at the bottom",
        "paths": {"west": "Hallway", "north": "Safe Area", "south": "death", "east": "death"}
    },
    "Treasure Room": {
        "description": "a room with a golden chest containing the golden, diamond crested mask! Be careful, it is surrounded by snake pits",
        "has_mask": True,
        "paths": {"west": "Long Hallway", "south": "Safe Area Hallway", "north": "Snake Pit", "east": "Snake Pit"}
        
    },
    "Safe Area": {
        "description": "You are safe for now, but watch for your next move.",  
    "paths": {"north": "Treasure Room", "south": "Trap Room", "east": "Entrance", "west": "death"}
    },
    "Snake Pit": {
        "description": "You have fallen into a pit of deadly snakes. You are dead.",
    "Long Hallway": {
        "description": "You have reached the hallway that leades to the exit of this pyramid! These leads to the desert where you will be picked up by troopers and taken back home.",
        "paths": {"north": "Treasure Room", "south": "Home", "east": "Snake Pit", "west": "Snake Pit"},
    },
}
}

# Define player
player = {
    "location": "Entrance",
    "inventory": []
}

def explore_room(room):
    room_info = rooms[room]
    print(f"\nYou are in the {room}. {room_info['description']}")
    if "has_mask" in room_info and room_info["has_mask"]:
        print("🎭 You found the Golden mask! 🎉")
        return True
    return False
  

def navigate_pyramid():
    current_room = "Entrance"
    while True:
        found = explore_room(current_room)
        if found:
            break
        command = input("Where do you want to go? (north, south, east, west): ").lower()
        if command in rooms[current_room].get("paths", {}):
            current_room = rooms[current_room]["paths"][command]
        else:
            print("You can't go that way!")
    print("Congratulations! You've completed your quest.")

# Game loop
if __name__ == "__main__":
    current_room = "Entrance"
    while True:
        found = explore_room(current_room)
        if found:
            break
        command = input("Where do you want to go? (north, south, east, west): ").lower()
        if command in rooms[current_room]["paths"] :
            current_room = rooms[current_room]["paths"][command]
        else:
            print("You can't go that way!")
    print("Congratulations! You've completed your quest.")

# Game loop
if __name__ == "__main__":
    navigate_pyramid()
def navigate_pyramid():
    current_room = "Entrance"
    while True:
        found = explore_room(current_room)
        if found:
            break
        command = input("Where do you want to go? (north, south, east, west): ").lower()
        if command in rooms[current_room]["paths"]:
            current_room = rooms[current_room]["paths"][command]
        else:
            print("You can't go that way! There is a snake pit over there, be careful where you step!")
    print("Congratulations! You've completed your quest.")
# Define rooms
rooms = {
    "Entrance": {
        "description": "a grand entrance with carvings on the walls containing images of the golden pharaoh mask crested with diamonds running along the middle of the face leading down the back of the head.",
        "paths": {"north": "Hallway"}
    },
    "Hallway": {
        "description": "a long hallway with ancient paintings and cracked sandstone walls containing ancient scripts!",
        "paths": {"east": "Trap Room", "west": "Entrance", "south": "Entrance"}
    },
    "Trap Room": {
        "description": "a room filled with hidden traps. Be careful! You could fall in a hole filled with hungry, bloodthirsty diamondback python waiting for you at the bottom",
        "paths": {"west": "Hallway", "north": "Safe Area", "south": "death", "east": "death"}
    },
    "Treasure Room": {
        "description": "a room with a golden chest containing the golden, diamond crested mask! Be careful, it is surrounded by snake pits",
        "has_mask": True,
        "paths": {"west": "Long Hallway", "south": "Safe Area Hallway", "north": "Snake Pit", "east": "Snake Pit"}

    },
    "Safe Area": {
        "description": "You are safe for now, but watch for your next move.",  
    "paths": {"north": "Treasure Room", "south": "Trap Room", "east": "Entrance", "west": "death"}
    },

}
# Define player
player = {
    "location": "Entrance",
    "inventory": []
}

def explore_room(room):
    room_info = rooms[room]
    print(f"\nYou are in the {room}. {room_info['description']}")
    if "has_mask" in room_info and room_info["has_mask"]:
        print("🎭 You found the Golden mask! 🎉")
        return True
    return False

def navigate_pyramid():
    current_room = "Entrance"
    while True:
        found = explore_room(current_room)
        if found:
            break
        command = input("Where do you want to go? (north, south, east, west): ").lower()
        if command in rooms[current_room]["paths"]:
            current_room = rooms[current_room]["paths"][command]
        else:
            print("You can't go that way!")
    print("Congratulations! You've completed your quest.")




