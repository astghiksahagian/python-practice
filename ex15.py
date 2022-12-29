#*** use extra sample text file (ex15_sample.txt) to open and read file within ex15.py. Opening a file create a file object (container) and reading the file prints out the text.

from sys import argv

script, filename = argv
#takes 2 arguments

txt = open(filename)
#opens a file based on the one chosen in filename

print(f"Here's your file {filename}:")
print(txt.read())
#prints (reads) the text inside the filename file onto this file

print("Type the filename again:")
file_again = input("> ")
#prompts user input to manually type name of the file being used

txt_again = open(file_again)
print(txt_again.read())
#opens the file name stored inside of file_again and reads (prints) it using the .read() function.