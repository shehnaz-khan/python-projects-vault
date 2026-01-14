print("welcome to the rollercoaster Ride!")

# Ask user height and convert input to integer
height = int(input("what is your height in cm?\n"))

# Initialize bill amount
bill = 0

# Check if user is tall enough to ride
if height >= 120:
    print("you can ride the rollercoaster")
    
    # Ask user age
    age = int(input("what is your age?\n"))
    
    # Child ticket price
    if age <= 12:
        bill = 5  # $5 for children
    
    # Teen ticket price
    elif age <= 18:
        bill = 7  # $7 for teens
    
    # Free ride for age between 45 and 55
    elif age >= 45 and age <= 55:
        print("you can ride for free!")  # No charge
    
    # Adult ticket price
    else:
        bill = 12  # $12 for adults
        
    # Ask if user wants a photo
    photo = input("Do you want to have a photo take? type yes or no.\n")
    
    # Add photo cost if chosen
    if photo == "yes":
        bill += 3  # Add $3 for photo
        
    # Show final bill
    print(f"your final bill is {bill}$")

# If height condition fails
else:
    print("Sorry you can't ride")
