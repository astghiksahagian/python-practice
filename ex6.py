types_of_people = 10
x = f"there are {types_of_people} types of people."
#this variable is using f formating to include a variable inside of a string. 

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}."
#this variable is using f formating to include 2 variables inside of a string. 

print(x)
print(y)

print(f"I said: {x}")
# this variable is using f formating to include a variable (which is a string) inside of a string.
print(f"I also said: '{y}'")
# this variable is using f formating to include a variable (which is a string) with single quotation marks inside of a string. The single quoes emphasize the fact that something was said.

hilarious = False
# this variable is assigned a boolean value: False. False needs to be written with first letter upper-case to be recognized as a boolean value.

joke_evaluation = "Isn't that joke so funny?! {}"
# this variable is assigned a string with an empty placeholder, which will be assigned a value in the following print statement.

print(joke_evaluation.format(hilarious))
#the {} acts as a placeholder, which is then identified by using the .format() after the end of variable's value or a variable in a print statement, as seen above.
# The placeholders can be identified using:                               
    # - named indexes {price},
    # - numbered indexes {0}, 
    # - empty placeholders {}.

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
#this statement combine 2 different  variables into a single line. 
#Result: This is the left side of... a string with a right side."


