"""
Assignment 1: Input and Output Assignment
January 11, 2024
Samantha Aguiar
"""

def knows_python(name, rating):
    """
    This function gives a specific, personalized message based on user rating.
    input: takes a name as a str and a rating from 1 to 5 as an integer
    output: a str stating an evaluation based on user self reflection
    """
    print(f"Thank you for your answers, {name}.")
    if rating == 1 or rating == 2:
        print(f"{name}, Python is a good language to learn!")
        print("A great book to get started with is 'Introduction to Computation and Programming Using Python, 3rd edition' by John V. Guttag.")
    elif rating == 3 or rating == 4:
        print(f'Wow, {name}! It is great to hear that you know python well.')
        print('You should look into classes at University of Cumberlands to further your skills!')
    else:
        return(f'{name}, you are a master at Python!')

def python_resources(name, wants_resources, list):
    """
    This function provides a resource list if the user indicates that they want one.
    input: takes a name as a str and wants_resources as a str
    output: string with resources
    """
    if wants_resources.upper() == 'Y':
        list.append(f'Would you like some resources to start learning python? Yes')
        print(f"Awesome, {name}. Some great books to get started with are: \n 'Introduction to Computation and Programming Using Python, 3rd edition' by John V. Guttag; and \n 'Murach's Python Programming, 2nd Edition' by Michael Urban and Joel Murach.")
    elif wants_resources.upper() == 'N':
        list.append(f'Would you like some resources to start learning python? No')
        print(f"Sounds good, {name}!")

def view_answers(name, answer_list):
    """
    This function provides a list of user's answers if user indicates that they want one.
    input: takes a user's name as a str and a dictionary with the user's answers
    output: 1) provides a list of answers or 2) Exits program.
    """
    # created while loop to ensure user inputed correct input for the final question
    valid_input = False
    while not valid_input:
        final_input = input(f'Do you want to see your responses? Press Y for Yes or N for No. ')
        if final_input.upper() == 'Y':
            print('Here are your answers:')
            for answer in answer_list:
                print(f'- {answer}')
                print(f'The program has been exited. Have a good day, {name}!')
            break
        elif final_input.upper() == 'N':
            print(f"Okay, {name}. Have a great day. You have exited the program.")
            break
        else:
            print("Please enter a valid input.")
            final_input = input(f'Do you want to see your responses? Press Y for Yes or N for No. ')



def main():
    """
    This function is the main function that asks generalized questions from the user.
    input: none
    output: various str statements based on user input.
    """
    # empty list to store user answer for each question
    input_answers = []

    # question asking user name
    # input is then captialized and appended to list
    input_1 = input('What is your name? ')
    input_1 = input_1.capitalize()
    input_answers.append(f'What is your name? {input_1}')

    # question asking user if they know python
    # user must enter y/n (or Y/N). if not, an error message appears.
    input_2 = input('Do you know Python? Press Y for Yes and N for No. ')
    
    # created to run while loop to help with errors in responses
    answer_2 = False
    
    while not answer_2:
        if input_2.upper() == 'Y':
            # appends question 2 and "yes" to list
            input_answers.append('Do you know Python? Yes')

            input_3 = int(input('Using the scale 1 (lowest) to 5 (highest), what is your level of Python? '))
            answer_3 = False
            while not answer_3:    
                if 0 < input_3 < 5:
                    input_answers.append(f'Using the scale 1 (lowest) to 5 (highest), what is your level of Python? {input_3}')
                    knows_python(input_1, input_3)
                    answer_3 = True
                else:
                    print('Invalid Response.')
                    input_3 = int(input('Using the scale 1 (lowest) to 5 (highest), what is your level of Python? '))
            break

        elif input_2.upper() == 'N':
            # appends question 2 and "no" to list
            input_answers.append('Do you know Python? No')
            print("Python is a great language to learn!")
            
            # if users answer no to question 2, user will be asked if they want resources
            # user must enter y/n or Y/N
            input_4 = input('Would you like some resources to start learning python? Press Y for Yes and N for No. ')
            # created variable to ensure while loop will ask user the question again if error
            answer_4 = False
            
            while not answer_4:
                if input_4.upper() == 'Y' or input_4.upper() == 'N':
                    python_resources(input_1, input_4, input_answers)
                    answer_4 = True
                else:
                    print("Please enter a valid input.")
                    input_4 = input('Would you like some resources to start learning python? Press Y for Yes and N for No. ')
            break
        else:
            print("Please enter a valid input.")
            input_2 = input('Do you know Python? Press Y for Yes and N for No. ')

    view_answers(input_1, input_answers)

if __name__ == "__main__":
    main()
    