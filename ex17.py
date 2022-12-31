from sys import argv
from os.path import exists
#importing a command named exists, which returns a True or False value depending on if a file exists.

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file).read()
#opening and reading content from ex15_sample.txt to prepapre to copy paste into ex16_sample.txt.

print(f"The input file is {len(in_file)} bytes long")
#len() returns the length of the string that is passed; returns a number.

print(f"Does the output file exist? {exists(to_file)}")
#returns a True or False value depending on if a file exists.

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w").write(in_file)
#opening content from ex16_sample.txt and pasting content from ex15_sample.txt using .write()

print("Alright, all done.")

