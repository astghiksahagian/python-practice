the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

for number in the_count:
    print(f"this is count {number}")
#In python, the syntax is a structured so that you say for “element” in “list”. 
    #Fuit and number are being considered the element that corresponds to the starting index
    #whats happening is that python is just iterating until the end of the list (incrementing), and letting you define the callback for each element (as the inside of the for loop block).

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []
#defining an empty list to append elements to in the for loop below

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")

