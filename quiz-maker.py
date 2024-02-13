#Name: Hamza Sheikh
#Description: This program is a general purpose quiz maker which allows
#the user to add or delete questions as they wish

"""
Functions:

main_menu(): prints the menu
play(): prints the play menu
create(): prints the create menu

get_option(n, prompt, new_line): lets the user choose an integer from 1 to n
get_letter(string, prompt, new_line): lets the user choose 1 letter in string

add_question(): adds a question
delete_question(): deletes a question

do_quiz(): prints and performs a 10 question quiz.

"""

####Description for Database####
"""
Data in the database(questions.txt) is read through in increments of 7 lines. Each line
is 1 part of the data for the entire question. The explanation for each line is listed
below:

line 1: The question

line 2-5: Options A through D

line 6: the answer to the question, set as an integer
A = 0, B = 1, C = 2, D = 3

line 7: "True" or "False" as to if the user wants the questions options to be
randomized or not

The program will read the file as 1 giant string, and then use .split(/n) to seperate
the file into 1 list. the program will then randomly select one of the multiples
of 7 (and 0) and set that as the current question

Example:
index 0 in the database list would be the first question
index 7 in the database list would be the second question

the program then adds a certain amount to find certain values when required

Example:
to find option "B" for question 2 you can add 2 to index of 7 
to find the answer for question 1 you can add 6 to the index of 0


"""
################################


#import random module
from random import *

def main_menu():
    """prints the menu of the main program

    Args:
    None

    Returns:
    None

    """
    print("Please choose one of the following options:")
    print("1. Play")
    print("2. Create")
    print("3. Exit")

def play():
    """prints the menu of the play portion

    Args:
    None

    Returns:
    None

    """

    print("Please choose one of the following options:")
    print("1. Start a New Quiz")
    print("2. Back to Main Menu")

def create():
    """prints the menu of the create portion

    Args:
    None

    Returns:
    None

    """

    print("Please choose one of the following options:")
    print("1. Add Question")
    print("2. Delete Question")
    print("3. Back to Main Menu")

def get_option(n, prompt, new_line=True):
    """allows the user to choose an option while
       preventing errors from bad input
       
       Args:
       n(int) the maximum amount of options the user can choose
       assumption: n >= 2
       
       prompt(str): the outputted message given to the user
       assumption: prompt will make sense to the user
       
       new_line(bool): optional argument that decides whether a new
       line will be printed after bad input
       
       Returns:
       option(int): the menu option chosen by the user
       
    """
    
    inputting = True
    while inputting:
        
        try:
            option = int(input(prompt))
            #check if option is in desired range
            if option not in range(1, n+1):
                print("You must select a number from 1 to ", n, "!", sep="")
                #add line if required
                if new_line:
                    print()
            else:
                #if proper input found, return value
                inputting = False
                return option
        except:
            print("Invalid Input. Please select a number from" \
            + " 1 to ", n, "!", sep="")
            if new_line:
                print()

def get_letter(string, prompt, new_line=True):
    """allows the user to choose a 1 letter response
       from a choice given by the program
       
       Args:
       string(str) all allowed letters
       assumption: string contains atleast 1  character
       
       prompt(str): the outputted message given to the user
       assumption: prompt will make sense to the user
       
       new_line(bool): optional argument that decides whether a new
       line will be printed after bad input
       
       Returns:
       option(int): the letter option chosen by the user
       
    """
    inputting = True
    while inputting:
        
        try:
            option = input(prompt)
            #check if option is only 1 letter
            if len(option) < 1:
                print("You must enter only 1 letter!")
                #add line if required
                if new_line:
                    print()
            #check if option is in allowed characters
            elif option not in string:
                print("You must select one of the options!")
                if new_line:
                    print()
            else:
                #if proper input found, return value
                inputting = False
                return option
        except:
            print("Invalid Input. Please select a valid letter.")
            if new_line:
                print()





def add_question():
    """Adds a question to the database

    Args:
    None

    Returns:
    None

    """
    #create a list of the possible options
    #used later when corresponding index number to letter
    ans_key = ["A", "B", "C", "D"]

    #open the file, if none exists one will be created
    infile = open("questions.txt", "a")
    print("add the text for the question you would like to add. Press " \
    + "enter when done.")
    question = input()
    
    print()
    
    #have user select options
    print("Now enter the options for choice A, B, C, D. Press enter after" \
    + " each entry.")
    A = input("(A) ")
    B = input("(B) ")
    C = input("(C) ")
    D = input("(D) ")
    print()
    
    #have user select the answer
    ans = get_letter("ABCDabcd","Now enter the answer(A, B, C or D): ")
    ans = ans.upper()
    print()

    #let user decide if they want the options randomized
    randomizer = get_letter("YNyn", "Would you like the options to be" \
    + " randomized (Y/N)? ")
    if randomizer.upper() == "Y":
        random = "True"
    else:
        random = "False"
    
    final_ans = get_letter("YNyn", "Would you like to add this" \
     + " question to the database (Y/N)? ")
    #data for each question is organized in 7 lines
    if final_ans.upper() == "Y":
        #lines 1-5 are all string values
        infile.write(question + "\n")
        infile.write(A + "\n")
        infile.write(B + "\n")
        infile.write(C + "\n")
        infile.write(D + "\n")

        #line 6 is a number from 0 to 3 which corresponds to the answer
        infile.write(str(ans_key.index(ans)) + "\n")
        #line 7 is set as "True" or "False" for randomization
        infile.write(random + "\n")
        print("Question Added.")

    
    print()
    infile.close()
    
def delete_question():
    """Deletes a question to the database

    Args:
    None

    Returns:
    None

    """
    
    error = False
    
    try:
        #attempt to read the database
        infile = open("questions.txt", "r")
        #turn file into a list split by each new line
        database = infile.read().split("\n")
        
        #remove empty line in database
        database.pop(-1)
    except:
        print("No file found. Please add questions or file to same directory.")
        error = True

    if error == False:
        #have user select keyword
        print("\n")
        print("To delete a question, you will need to enter a key phrase to")
        print("search for in the database. The first question to contain this")
        print("key phrase will be deleted. Press enter when done.")
        keyword = input()

        #remove extra spaces or caps in keyword
        keyword = keyword.strip()
        keyword = keyword.lower()
        print()
        
        #find the total matches of keyword in database
        matches = []
        for i in range(0, len(database), 7):
            #iterate through each question and find keyword
            if keyword in database[i].lower():
                matches.append([database[i], i])
        
        
        total_matches = len(matches)
        #if only 1 match found
        if total_matches == 1:
            print("1 match found.")
            print(matches[0][0])
            print()
            confirmation = get_letter("YNyn", "Would you like to delete this" \
            + " question (Y/N)?: ")
            if confirmation.upper() == "Y":
                for i in range(7):
                    database.pop(matches[0][1])
            else:
                print("no question was deleted.")

        #print all matches if multiple found
        elif total_matches > 1:
            print(total_matches, "matches found.")
            print()
            
            for i in range(total_matches):
                #print each question
                print("{0}. {1}".format(i + 1, matches[i][0]))
            
            #ask user which question to delete
            delete_choice = get_option(total_matches, "Which question would" \
             + " you like to delete: ")
            
            confirmation = get_letter("YNyn", "Are you sure you would like" \
            + " to delete this quesstion (Y/N)?: ")
            if confirmation.upper() == "Y":
                #find the chosen question in the list of matches
                deleted_question = matches[delete_choice - 1][1]
                
                 #delete the 7 lines of data for the queston
                for i in range(7):
                    #pop() will change the index value on its own
                    database.pop(deleted_question)
            else:
                print("no question was deleted.")
        else:
            print("Sorry, no question matches your key phrase in the database.")
            print("no question was deleted.")
            confirmation = "N"
        
        #if question was deleted, recreate database file using changed list
        if confirmation.upper() == "Y":
            infile = open("questions.txt", "w")
            for i in range(len(database)):
                infile.write(database[i] + "\n")
            #delete message
            print("Question Deleted.")
            infile.close()
    
    

def do_quiz():
    """Displays the main quiz program

    Args:
    None
    
    Returns:
    None
    """
    
    #variables to be used later
    ans_key = ["A","B","C","D"]
    letters = ["(A)", "(B)", "(C)", "(D)"]
    
    try:
        #attempt to read the database file
        infile = open("questions.txt", "r")
        database = infile.read().split("\n")
        
        #remove empty line from file
        database.pop(-1)
        infile.close()
        
        #check if atleast 10 questions exist
        if (len(database) // 7) < 10:
            print("You need atleast 10 questions. Please go to create menu.")
            print()
            error = True
        else:
            error = False
    except:
        print("You need atleast 10 questions. Please go to create menu.")
        print()
        error = True
    
    #create a list of the starting indexes of every question 
    total_questions = [int(i) for i in range(0, len(database), 7)]
    
    #randomize the list
    shuffle(total_questions)
    
    correct_ans = 0
    question_counter = 0
    
    #uses the first 10 indexes of randomized list as questions
    while (question_counter < 10) and error == False:
        question = total_questions[question_counter]
        question_counter += 1
            
        #prints the question number
        print("Question", question_counter)
        print("**********")
        print(database[question])
        
        #checks if user wants the options randomized
        if database[question + 6] == "True":
            i = 0
            #random num from 1 to 4 correspond with each option
            random_option = [1,2,3,4]
            shuffle(random_option)
            for i in range(4):
                #print the option + random_counter
                print(letters[i], database[question + random_option[i]])
                #if option is answer, change answer index to that value
                if (random_option[i] - 1) == int(database[question + 5]):
                    ans_index = i
        else:
            #if questions are not randomized, iterated through normally
            for i in range(4):
                print(letters[i], database[question + i + 1])
            ans_index = int(database[question + 5])
        
        #use the ans_key list to correspond index to string answer
        ans = ans_key[ans_index]
        
        #ask user for answer
        user_ans = get_letter("ABCDabcd", "Select your answer: ")
        user_ans = user_ans.upper()
        
        print()
        
        #check if correct
        if ans != user_ans:
            print("Incorrect! The Answer was:", ans)
        else:
            print("Correct!")
            correct_ans += 1
        print()
    
    if error == False:
        #print score
        print("Your score was {0}%".format(correct_ans * 10))
        print()
              
    
def main():
    #print starting menu
    print(("*" * 14).center(20))
    print("* Quiz Maker *".center(20))
    print(("*" * 14).center(20))
    
    #create main menu loop
    menu = True
    while menu:
        main_menu()
        print()
        user_choice = get_option(3, "My option is: ")
        print()
        if user_choice == 1:
            #create play menu loop
            play_menu = True
            while play_menu:
                play()
                print()
                user_choice = get_option(2, "My option is: ")
                print()
                #if user selects a quiz
                if user_choice == 1:
                    print("Please wait while I make your quiz...")
                    print()
                    do_quiz()
                #goes back to menu
                if user_choice == 2:
                    play_menu = False
                    
        elif user_choice == 2:
            create_menu = True
            #create menu loop
            while create_menu:
                create()
                print()
                user_choice = get_option(3, "My option is: ")
                #if user adds a question
                if user_choice == 1:
                    add_question()
                #if user deletes a question
                elif user_choice == 2:
                    delete_question()
                #goes back to menu
                else:
                    create_menu = False
        else:
            #ends program
            menu = False
            print("Thank you for Playing.")
    
if __name__ == '__main__':
    main()
