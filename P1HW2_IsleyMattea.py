#Mattea Isley
#11/7/2023
#CTI-110 P1HW2 - Travel Expense

print("This program calculates and displays travel expenses!")

#Get input from user
Budget = int(input("Enter budget: "))
Destination = (input("Enter your travel destination: "))
Gas = int(input("How much do you thnk you will spend on gas?: "))
Hotel = int(input("Approximately, how much will you need for accomodation/hotel: "))
Food = int(input("Last, how much do you need for food?: "))

#Display calculated input
print("-----Travel Expenses-----")
print("Location: ", Destination)

print("Initial budget:", (Budget))

print("Fuel: ", Gas)

print("Accomodation", Hotel)

print("Food", Food)

#Final answer
print("Remaining balance: ", (Budget) - (Gas) - (Hotel) - (Food))





print("Have a fun vacation!")

