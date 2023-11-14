#Mattea Isley
#11/14/23
#Mathmatical expressions, lists, and f-string

from statistics import mean

#Get input from the user (4 values means 4 variables)
num1 = float(input("Enter a decimal value: "))
num2 = float(input("Enter a decimal value: "))
num3 = float(input("Enter a decimal value: "))
num4 = float(input("Enter a decimal value: "))

#Create an empty list
num_list = []

#Add values to list
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)

print(num_list)

#Call methods on the list to get the sum and product
list_sum = sum(num_list)
list_avg = mean(num_list)

#Output to user formatted with f-string
print(f"{list_sum:.0f} {list_avg:.0f}")
print(f"{list_sum:.3f} {list_avg:.3f}")
      


