#CTI-110
#Mattea Isley
#11/28/2023
#Homework content P4HW1

from statistics import mean


#Get number of grades from user
num_grades = int(input("How many grades will you enter? "))

#Create list from grade values
grades_list = []

#Get grades from the user
for i in range(num_grades):
    grade = float(input(f"Enter grade for module {i + 1}: "))
#Grade is invalid if less than 0 or more than 100
    while grade < 0 or grade > 100:
        print("- - - - - - -")
        print("Invalid grade! Try again and make sure grade values are between 0 and 100!")
        print("- - - - - - -")
        grade = float(input(f"Enter grade for module {i + 1}: "))
    grades_list.append(grade)

print("- - - - - - -")
print("You entered: ", grades_list)
print("- - - - - - -")

#Calculte grade stats
print("------Results------")

min_grade = min(grades_list)
max_grade = max(grades_list)
sum_grade = sum(grades_list)
avg_grade = mean(grades_list)

#Output tp user formatted with f-string
print(f"Lowest grade:   {min_grade:.1f}")
print(f"Highest grade:   {max_grade:.1f}")
print(f"Sum of grades:   {sum_grade:.1f}")
print(f"Average:         {avg_grade:.2f}")

print("----------------------")
