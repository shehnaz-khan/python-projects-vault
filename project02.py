# Print a welcome message
print("Welcome to the Tip Calculator!")

# Ask the user for the total bill amount
# input() returns a string, so we convert it to float for calculations
bill = float(input("What was the total bill? $"))

# Ask the user for the tip percentage
# Convert the input to float so percentages like 12.5 would work
Tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask how many people will split the bill
# Convert to int because number of people must be a whole number
num_people = int(input("How many people to split the bill? "))

# Calculate the total bill including tip
# Tip / 100 converts percentage into decimal
# Tip amount is added to the original bill
bill_with_tip = (Tip / 100) * bill + bill

# Calculate how much each person should pay
bill_per_person = bill_with_tip/ num_people

# Print the amount each person should pay

print(f"Each person should pay:{bill_per_person} $")
