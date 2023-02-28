#**TIP: Use Control + C to end a loop on the terminal


#OPTION 1: takes in one argument to use as max number in range:
def while_smaller (number):
    i = 0 
    numbers = []

    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print(numbers)
    #total numbers list after finising while loop 
        #result = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    for num in numbers:
        print(num)
   

while_smaller(8)


#OPTION 2: takes in one argument to use as max number in range AND takes in an increment argument to adjust how to much to increment by in each loop:
def while_smaller (number, increment):
    i = 0 
    numbers = []

    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print(numbers)
    #total numbers list after finising while loop 
        #result = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    for num in numbers:
        print(num)
   

while_smaller(8, 2)


#OPTION 3: use a for loop with range

numbers = []

print("when using for loop:")

for i in range(0, 8):
    print(f"current i is {i}")
    numbers.append(i)

print(numbers)



