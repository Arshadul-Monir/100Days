print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
each = bill*(1+tip/100)/people
print(f"Each person should pay: ${round(each,2)}")