print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
an requires an explanation
\n\t\twhere there is none
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
#defines 3 variables referenced from the function secret_formula and assigns it to the function's return value. Because the return value is each of those variables, then each variable will be assigned a number.

print("With a starting point of: {}". format(start_point))

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
#different way of storing the multiple return values (e.g. beans, jars, crates) than the above.

print("We'd have {} beans, {} jars, and {} crates.".format(*formula)
# * unpacks an iterable (e.g. list, tupple) so that the values can be passed into their distinct arguments, instead of being grouped together like an array or tupple.
    # tupple is like an array, but consists of elements within parantheses(). Tupple is a phrase for multiple values.


