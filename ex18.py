#create functions using the word, def in python

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
#the * in *ards tell Python to take all the arguments to the function and put them in args as a list. It's similar to argv (used in previous lessons), but used for functions. This method is not commonly used for functions, it is easer to write out arguments in the parameters as seen in the exercise below.

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
