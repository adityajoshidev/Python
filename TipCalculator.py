print("Welcome to the Tip Calculator!")
bill=float(input("What is the total bill amount? $"))
tip=int(input("How much percentage tip do you want to give? "))
people=int(input("How many people to split the bill between? "))
payment=(bill*(tip/100)+bill)/5
print(f"Each person should pay ${round(payment,2)}")
