from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice  = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
        #using the built-in keyword "in" inside of the if statement ensures that any number input will be accepted as long as it includes a 0 or 1.
            #the "in" keyword is a smart way to allow flexible responses from users.
    else: 
        dead("Man learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
        #adding 0 to built-in exit function to ensure a smooth exit, free of any errors or problems.
            #need to confirm understanding with Shant/
    else:
        dead("You greedy bastard!")
    

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = True


    #why is the while loop below necessary?
        #need to confirm understanding with Shant.
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else: 
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():

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
    

start()