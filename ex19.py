from os.path import exists

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def desserts(dessert_amount):
    print(f"We have {dessert_amount} types of dessert at the party tonight!\n")

dessert_count = 10

desserts(dessert_count)
desserts(dessert_count + 10)
desserts(30)
desserts(30+10)
desserts(int(input("How many desserts do we have?")) + 9)
#this line takes the input (number given by user) and uses the int() function to convertf the string to an integer. After that it adds the user input number to 9.
#Ex.) userinput: 9 
    #  + 9
    #  = 18