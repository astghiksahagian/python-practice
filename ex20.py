from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())
#this function prints the current_line (an integer) when passed into the 1st parameter, line_count as well as the what the first line of the file reads after passing it to the 2nd parameter, f. After each readline(), it will print the next line afterwards if the function is executed again.

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("\nNow let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print 3 lines")
current_line = 1
print_a_line(current_line, current_file)
#current_line is equal to 1 and is passed into print_a_line as the first argument.

current_line += 1
print_a_line(current_line, current_file)
#current_line is now 1 + 1, which is 2 and is passed into print_a_line as the first argument.

current_line += 1
print_a_line(current_line, current_file)
#current_line is now 2 + 1, which is 3 and is passed into print_a_line as the first argument.