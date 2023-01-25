print("""You enter a dark room with two doors. 
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input (">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bears eats your legs off. Good job!")
    else: 
        print(f"Well, doing {bear} is probably better, but it looks like...")
        print("The bear is approacing you!")
        print("What do you do?")
        print("1. Run away.")
        print("2. Attack the bear.")
        
        action = input ("> ")

        if action == "1" or action == "run away":
            print("Woohoo! You got away!")
        elif action == "2" or action == "attack the bear":
            print("Oops you died :(")
        else:
            print("Uh oh. Looks like you didn't do anything. The bear killed you.")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!") 
        
else:
    print("You stumble around and fall on a knife and die. Good job!")
    