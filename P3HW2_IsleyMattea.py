#Mattea Isley
#11/21/2023
#Using if/else statements to determine an employee's pay


#Get input from the user
emp_name = input("Enter employee's name: ")
emp_hours = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("----------------------------")
print("Employee name: ", emp_name)

#Calculations
if emp_hours > 40:
    ot_hours = emp_hours - 40
    reg_hours = 40

else: #This represents if emp_hours is 40 or less
    ot_hours = 0
    reg_hours = emp_hours

#Calculate pay
ot_pay = (emp_pay * 1.5) * ot_hours
reg_pay = (emp_pay * reg_hours)
gross_pay = ot_pay + reg_pay



