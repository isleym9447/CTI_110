#Mattea Isley
#11/30/2023
#Using if/else statements to determine an employee's pay

#Create variables to hold totals paid to employees
num_emp = 0
total_ot= 0
total_reg = 0
total_gross = 0



#Get input from the user
emp_name = input("Enter employee's name or type 'Done' to terminate: ")
#Loop to control adding employees
while emp_name != "Done":
    num_emp += 1
    emp_hours = int(input("Enter number of hours worked: "))
    emp_pay = float(input("Enter employee's pay rate: "))
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
    total_ot += ot_pay

    reg_pay = (emp_pay * reg_hours)
    total_reg += reg_pay

    gross_pay = (ot_pay + reg_pay)
    total_gross += gross_pay

    #Display calculated data back to user
    print()
    print("Hours worked", "  ", "Pay Rate", "  ", "OverTime", "  ", "OverTime Pay", "  ", "RegHour Pay",  "  ", "Gross Pay") 
    print("---------------------------------------------------------------------------------")
    print(emp_hours, "         ", emp_pay, "         ", ot_hours, "         ", ot_pay, "          ", "$",reg_pay,
          "         ", "$",gross_pay)
    print()
    emp_name = input("Enter another employee's name or type 'Done' to terminate and get results: ")

#This code executes after the code breaks ie user enters 'Done'
print("--------------------")    
print("Done adding employees! :)")
print("--------------------")
print(f"Total number of employees entered: {num_emp}")
print(f"Total amount paid for overtime: ${total_ot}" )
print(f"Total amount paid for regular hours: ${total_reg}")
print(f"Total amount paid in gross: ${total_gross}")
