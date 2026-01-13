print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))

Tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

bill_with_tip = Tip / 100 * bill + bill

print("Each person should pay:" , bill_with_tip / num_people , "$")

