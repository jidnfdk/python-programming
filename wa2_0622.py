'''
Open the file DONATIONS.ipynb

Save the file as

This task is to edit program code so that donations for different types
of beneficiary organisations (e.g. Children, Elderly, Disabled, Religious)
can be added to a dictionary.

The following program has a dictionary that contains the different
types of beneficiary organisations and the donations they have received.

The program allows the user to :
input  whether they want to add a donation record to the dictionary
'''

donations = {'Children': 1200,
             'Elderly': 1000,
             'Disabled': 800,
             'Religious':2000
            }
add = input("Would you like to add a donation record? (Y or N): ")

'''
For each of the sub-tasks, add a comment using the hash symbol "#" at
the beginning of your code to indicate the sub-task that the program code belongs to.
For Example:
# Task 1.1
Program Code

For all sub-tasks, you can assume that all user input is valid.
'''

'''
##############  Task 1.1 ##############
Edit the program so that if the user enters the value 'Y' for add, the program:
- Allows the user to input the type of benedificiary organisation they want to donate to
- Allows the user to input the amount they want to donate
- Adds the type of beneficiary organisation and the donation amount to the dictionary
  in the format "beneficiary organisation": amount
- Outputs the dictionary at the end of the program

Save your program [3]
'''
#write your code here

'''
############## Task 1.2##############
Copy and paste your program from sub-task 1.1
Edit the program to check that the donation is at least $10
and in multiples of $10.

Otherwise, the program should inform the user about the input requirements
and ask the user to re-enter the information

Save your program [3]
'''
#write your code here


'''
############### Task 1.3 ##############
Copy and paste your program from sub-task 1.2

Edit the program to display the type of beneficiary organisation that received the highest donation
and the amount received. A suitable output message must be used.

Save your program [3]
'''
#write your code here

'''
############## Task 1.4 ##############
Copy and paste your program from sub-task 1.3

Edit the program to find the total amount donated across all the types of beneficiary
organisation. A suitable output message must be used.

Save your JupyterLab notebook for Task 1    [1]

'''
#write your code here