def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print ("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

cherries = divide(68, 2)
apples = subtract((divide(68, 2), 1023))
peaches = add(((divide(34, 100), 1023), 24))

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

puzzle1 = add(age, subtract(height, multiply(weight, divide(iq, 2))))

puzzle2 = add(peaches, subtract(apples, divide(cherries, 2)))

print("Puzzle1 becomes:", puzzle1, "Can you do it by hand?")

print("Puzzle1 becomes:", puzzle2)

# *** ASK SHANT HOW TO SOLVE STUDY DRILL ***
