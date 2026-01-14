print("Welcome to Pizza Deliveries")

# Ask user for pizza size
size = input("what size pizza you want? S, M or L: ")

# Ask if user wants pepperoni
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

# Ask if user wants extra cheese
cheese = input("Do you want extra cheese? Y or N: ")

# Initialize bill amount
bill = 0

# Base price based on pizza size
if size == "S":
    bill = 15      # Small pizza price
elif size == "M":
    bill = 20      # Medium pizza price
elif size == "L":
    bill = 25      # Large pizza price
else:
    print("You have entered a wrong input")

# Add pepperoni cost
if pepperoni == "Y":
    if size == "S":
        bill += 2  # $2 for pepperoni on small pizza
    else:
        bill += 3  # $3 for pepperoni on medium or large pizza

# Add extra cheese cost
if cheese == "Y":
    bill += 1      # $1 for extra cheese

# Print final bill
print(f"Your final bill is : {bill}")
