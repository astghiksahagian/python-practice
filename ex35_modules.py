# import ex35 as room_module

# room_module.bear_room()

import ex35 

print("You are in a dark room.")
print("There is a door to your right and left.")
print("which one do you take?")

choice = input("> ")

if choice == "left":
    bear_room()
elif choice == "right":
    cthulhu_room()
else:
    dead("You stumble around the room until you starve")

#example of how to import modules