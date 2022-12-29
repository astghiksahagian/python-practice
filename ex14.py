from sys import argv

script, user_name, user_last_name = argv
prompt = "- "

print(f"Hi {user_name} {user_last_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me {user_name} {user_last_name}?")
likes = input(prompt)

print(f"Where do you live {user_name} {user_last_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me. 
You live in {lives}. Not sure where that is. 
And you have a {computer} computer. Nice.
""")

