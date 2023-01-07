#*** this exercise uses argv from the sys module to be assigned to variables that will later be assigned to arguments that are passed down to it"
    #step 1: assign paramters (called variables in python) to argv (from sys module)
    #step 2: pass arguments to parameters when running code
    #result: see below.


from sys import argv

script, love, that, look, on, you = argv

print("This script is called:", script)
print("Your love variable is:", love)
print("Your that variable is:", that)
print("Your look variable is:", look)
print("Your on variable is:", on)
print("Your you variable is:", you)


fashion_favorite = input(f"What's your favorite type of {look} or accessory? ")
fashion_style = input("What's your favorite type of fashion style? ")
#practice using input along with argv.
