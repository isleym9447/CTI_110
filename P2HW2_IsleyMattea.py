#CTI-110
#Mattea Isley
#11/16/2023
#Homework content

from statistics import mean

#Get info from user

grade_m1 = float(input("Enter grade for module 1: ")) 
grade_m2 = float(input("Enter grade for module 2: ")) 
grade_m3 = float(input("Enter grade for module 3: "))
grade_m4 = float(input("Enter grade for module 4: "))
grade_m5 = float(input("Enter grade for module 5: "))
grade_m6 = float(input("Enter grade for module 6: "))

#Create list from grade values
grades_list = []

#Add values to list
grades_list.append(grade_m1)
grades_list.append(grade_m2)
grades_list.append(grade_m3)
grades_list.append(grade_m4)
grades_list.append(grade_m5)
grades_list.append(grade_m6)

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

print("-------------------")
