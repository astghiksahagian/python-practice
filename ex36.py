#create text based adventure game (bear chase) that includes the following:
    #functions
    #lists 
        # - ask Shant how to incorporate.
    #modules (argv) 
        # - ask Shant how to incorporate.
        # something like this: 
        #print(f"Hi {user_name} {user_last_name}, I'm the {script} script.")
        #print(f"I'd like to ask you a few questions.")


from sys import exit

def dead(why):
    print(why)
    exit(0)

print("To start this game list 2 of some of your closest friends.\n")
friend1 = input("first friend: ")
friend2 = input("second friend: ")

print("\nAlright then, let's start.\n")

def start():
    print(f"You're in Big Bear, CA for a fun weekend trip with your friends, {friend1} and {friend2}.")
    print("You guys went to do some grocery shopping and scored a bunch of food and snacks. AWESOME!")
    print("When you guys come back to your cabin to unload the groceries, you hear a strange noise from one of the rooms...")  
    print(f"Which room are you heading to - yours, {friend1}'s, or {friend2}'s?\n")

    room_choice = input("> ")

    if "mine" in room_choice or "my room" in room_choice:
        user_room()
    elif friend1 in room_choice or "{friend1}'s" in room_choice or "{friend1}'s room" in room_choice:
        friend1_room()
    elif friend2 in room_choice or "{friend2}'s" in room_choice or "{friend2}'s room" in room_choice:
        friend2_room()
    else: 
        print(f"{room_choice} does not match {friend1} or {friend2}")
        # print("\nThat doesn't sound like you or either one of your friends. Let's try again :)\n")
        start()


def user_room():
    print("\nThe sound on the way to your room is sounding more and more clear...")
    print("But what is it?")
    print("You open the door and BAM!")
    print("There it is! An 8ft tall grizzly bear standing on it's hind legs!")
    print("Do you run for your life or attack the bear?\n")
    
    action_choice = input("> ")

    if "run" in action_choice or "run away" in action_choice or "run for my life" in action_choice:
        print(f"\nWhich room are you heading to now - {friend1}'s or {friend2}'s?\n")

        room_choice = input("> ")

        #below if and elif statements are not executing!!
        #friend1_room and friend2_room not running
        if friend1 in room_choice or "{friend1}'s" in room_choice or "{friend1}'s room" in room_choice:
            friend1_room()
        elif friend2 in room_choice or "{friend2}'s" in room_choice or "{friend2}'s room" in room_choice:
            friend2_room()
        else:
            user_room()
    elif "attack" in action_choice or "attack bear" in action_choice or "attack the bear" in action_choice:
        dead("\nSorry pal, you didn't win this battle. Better decision making in the next life.")
    else:
        user_room()

def friend1_room():
    print(f"\nYou entered {friend1}'s room. Everything looks good so far.")
    print("Oh wait, what's that?")
    print("Aww! it's a small little bear cub!")
    print("Do you pet it or back away to enter another room?\n")

    action_choice = input("> ")

    if "pet" in action_choice or "pet it" in action_choice or "pet cub" in action_choice or "pet bear cub" in action_choice:
        dead("\nIt looks like Mama bear was nearby and she took you straight down with one bite. Ouch!")
    elif "back away" in action_choice or "back away to enter another room" in action_choice or "back away and enter another room" in action_choice or "enter another room" in action_choice:
        print(f"\nWhich room are you heading to now - yours or {friend2}'s?\n")

        room_choice = input("> ")

        if "mine" in room_choice or "my room" in room_choice:
            user_room()
        elif friend2 in room_choice or "{friend2}'s" in room_choice or "{friend2}'s room" in room_choice:
            friend2_room()
        else:
            friend1_room()
    else:
        friend1_room()

def friend2_room():
    print(f"\nYou entered {friend2}'s room. Everything looks good so far.")
    print("Let's check around the room and make sure the coast is clear")
    print("Alright everything is good in this room")
    print("You still hear the sound from afar though...")
    print("It's time to decide whether you want to face the uncertainty head-on or flee from the house while you have a chance.")
    print("Are you going to fight or flight?")

    action_choice = input("> ")

    if "fight" in action_choice:
        dead("\nIt looks like that sound came from a bear, who successfuly ate you up. I guess it wasn't successful for you though :/")
    elif "flight" in action_choice: 
        print("\nCongrats! You made the smartest choice you can make in this game, you win!")
        exit(0)
    else:
        friend2_room()

start()
    

