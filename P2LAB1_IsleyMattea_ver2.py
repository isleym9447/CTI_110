#get the input from the user
#mpg convert to float
#cost_gal convert to float
#input how far they want to drive
#20mpg/20mi = 1 gallon required
#gal required x cost_gal
#1 * 3.1599 = 3.16 to drive 20 miles

#Mattea Isley
#11/14/2023
#LAB: Use float values to represent the cost to drive a specified distance :)


#Get input from user
mpg = float(input("Enter the car's miles per gallon as a decimal number: "))
cost_gal = float(input("Enter the cost for one gallon of gas as a decimial: "))

#Calculate cost to drive 20 miles
Drive_cost_20 = (20/mpg) * cost_gal

#Calculate cost to drive 75 miles
Drive_cost_75 = (75/mpg) * cost_gal

#Calculate cost to drive 500 miles
Drive_cost_500 = (500/mpg) * cost_gal

#Calculate cost to drive 1000 miles
Drive_cost_1000 = (1000/mpg) * cost_gal

#Calculate cost to drive 2000 miles
Drive_cost_2000 = (2000/mpg) * cost_gal

#Output the cost with two decimal places using an f string
print(f"Cost to drive 20 miles is: ${Drive_cost_20:.2f}")

#Output the cost with two decimal places using an f string
print(f"Cost to drive 75 miles is: ${Drive_cost_75:.2f}")

#Output the cost with two decimal places using an f string
print(f"Cost to drive 500 miles is: ${Drive_cost_500:.2f}")

#Output the cost with two decimal places using an f string
print(f"Cost to drive 1000 miles is: ${Drive_cost_1000:.2f}")

#Output the cost with two decimal places using an f string
print(f"Cost to drive 2000 miles is: ${Drive_cost_2000:.2f}")
