#Mattea Isley
#12-7-23
#Homework and math quiz
#Functions, random numbers, and while loops



#Import random library
import random



#This function displays the main menu
def show_menu():
        print("Welcome to Math Quiz!")
        print()
        print()
        print("----------MAIN MENU----------")
        print("-----------------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print("-----------------------------")
        print()
        print()

        
#This function adds random numbers
def add():
    rand_num1 = random.randint(0, 10)
    rand_num2 = random.randint(0, 10)
    print(f"{rand_num1} + {rand_num2}")
    return (rand_num1 + rand_num2)

#This function subtracts random numbers
def subtract():
    rand_num1 = random.randint(0, 10)
    rand_num2 = random.randint(0, 10)
    print(f"{rand_num1} - {rand_num2}")
    return (rand_num1 - rand_num2)

#This function defines the user guessing the answer. While the user inputs
#the wrong answer, allow the user to guess again until correct.
def guessing(guess, correct_answer):
    num_guesses = 0
    
    while guess != correct_answer:
        num_guesses += 1
        if guess > correct_answer:     #If guess is too high
            print("Sorry, your guess is too high. Try again!")
            guess = int(input("Guess again?: "))
        else:                               #If guess is too low
            print("Sorry, your guess is too low. Try again!")
            guess = int(input("Guess again?: "))   #Represents guess
        #Guess is correct, the while loop breaks
    print()
    print("Congratulations!! Your guess is correct! You smarty pants! :)")
    print()
    print(f"It took you {num_guesses} incorrect guesses to get the answer correct.")


    


#Main function
def main():
    show_menu()
    user_option = int(input("Please choose one of the menu options: "))
    while user_option != 3:
        if user_option == 1:
            rand_sum = add()   #Represents the correct answer in this case the added random numbers
            my_guess = int(input("Enter your guess!: "))   #Represents guess
            guessing (my_guess, rand_sum)
            print()
            show_menu()
            user_option = int(input("Please choose one of the menu options: "))
        if user_option == 2:
            rand_sum = subtract()   #Represents the correct answer in this case the added random numbers
            my_guess = int(input("Enter your guess!: "))   #Represents guess
            guessing (my_guess, rand_sum)
            print()
            show_menu()
            user_option = int(input("Please choose one of the menu options: "))

    #If user_choice == 3, the while loop breaks
    print()
    print("Thank you for playing! Goodbye!")
            
    
#Call main function
if __name__ == "__main__":
    main()

