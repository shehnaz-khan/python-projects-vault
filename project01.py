# Print a welcome message to the user
print("Welcome to the Game Character Name Generator!")

# Ask the user for the character's main power and store it in a variable called 'power'
power = input("What is your character's power:\n")
# Uncomment the next line if you want to check what the user entered
# print("You entered: " + power)

# Ask the user for the character's personality trait and store it in a variable called 'personality'
personality = input("What is your character's personality trait:\n")
# Uncomment the next line if you want to check what the user entered
# print("You entered: " + personality)

# Combine the power and personality inputs to generate a character name
# The '#' symbol is added before the name as a prefix
print("Your character's name could be #" + power + personality)
