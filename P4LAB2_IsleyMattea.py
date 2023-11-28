#Mattea Isley
#11/28/2023
#Use a for loop with the range function


#Get two integers from user
#Make sure the first value is less than the second value
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number greater than the first: "))

#If the first number is smaller
if num_1 < num_2:
    for i in range(num_1, num_2 + 1, 5):
        print(i)
else:
    #Send them back to the beginning to start over after invalid data
    while num_1 > num_2 or num_1 == num_2:
        print()
        print("Please choose another number that is GREATER than the first!")
        print()
    
        #Get two integers from user
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter a number greater than the first: "))
    for i in range(num_1, num_2 + 1, 5):
        print(i)




