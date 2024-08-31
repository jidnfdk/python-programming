'''
2018 - Task 4 [20]
You have been asked to create a guessing game program.
The program should:
-	Allow player 1 to input a whole number between 1 and 50 inclusive, 
for player 2 to guess. There must be validation present to check that the 
number entered is between 1 and 50 inclusive.

-	Allow player 2 to have 5 guesses to correctly guess the number input by player 1. 
You do not need to validate the input for player 2.

-	Output “You guessed the correct number.” When player 2 inputs the same number 
as player 1. The game must end if the correct number is guessed.

-	Output “You did not guess the correct number.” When player 2 does not input 
the same number as player 1.

-	Output “Game over!” when player 2 has five incorrect guesses.
'''

'''
10.	Write your program and test that it works.
Save your program as MYGUESS1_<your name>_<center number>_<index number>.py
[10]
'''
# Write and test your code here
#create input for player 1 number
#validate the input is 1 to 50
#loop 5 times for player 2 input
#Ask player 2 for input
#check player 2 input == player 1 input


# while True:
#     player1 = input("Enter a number from between 1 to 50 ")
#     if player1.isdigit():
#         player1 = int(player1)
#         if player1 < 1 or player1 > 50:
#             print("Incorrect number. Number should be between 1 to 50.")
#         else:
#             print("Number accepted.")
#             break
#     else:
#         print("Incorrect number. Number should be between 1 to 50.")
        
# for i in range(5):
#     player2 = int(input("Guess player 1 number "))
#     if player2 == player1:
#         print("You guessed the correct number ")
#         break
#     else:
#         print("You did not guess the correct number ")
# # else:
# #     ## run if the loop completed successfully
# #     print("Game over!")

# if player2 != player1:
#     print("Game over!")
'''
11.	When your program is complete, test it for the following:
a.	Test 1 – Player 1 inputs the number 55
b.	Test 2 – Player 1 inputs the number 0
c.	Test 3 – Player 1 inputs the number 10 and player 2 guesses 
    the numbers 15 and 10
d.	Test 4 – Player 1 inputs the number 20 and player 2 guesses 
    the numbers 30, 35, 22, 15, 49
Take a screenshot of :
-	Test 1, 2 and 3. Save this single screenshot as: 
o	TEST123_<your name>_<center number>_<index number>
-	Test 4. Save this screenshot as:
o	Test4_<your name>_<center number>_<index number>
-	Save your files in either .png or .jpg format
[4]
'''
# Write and test your code here

'''
12.	Save your program as MYGUESS2_<your name>_<center number>_<index number>.py

Extend your program to identify if player 2’s guess is lower or higher 
than the number input by player 1. A suitable message must then be output.

Save your program.
[2]
'''
# Copy your code from above. Write and test your code here
# while True:
#     player1 = int(input("Enter a number from between 1 to 50 "))
#     if player1 < 1 or player1 > 50:
#         print("Incorrect number. Number should be between 1 to 50.")
#     else:
#         print("Number accepted.")
#         break
# for i in range(5):
#     player2 = int(input("Guess player 1 number "))
#     if player2 == player1:
#         print("You guessed the correct number ")
#         break
#     else:
#         print("You did not guess the correct number ")
#         if player2 < player1:
#             print("Your guess is lower than player 1 guess ")
#         elif player2 > player1:
#             print("Your guess is higher than player 1 guess ")
# if player2 != player1:
#     print("Game over!")
'''
13.	Save your program as MYGUESS3_<your name>_<center number>_<index number>.py

Extend your program to allow player 2 to choose an easy, medium or hard game. 
An easy game allows eight guesses, a medium game allows six guesses and a 
hard game allows four guesses.

If player 2 inputs a correct guess, the program must output the 
number of guesses made.

You are not required to validate the input for player 2.

Save your program.
[4]
'''
# Copy your code from above. Write and test your code here
numoftries = 0

num_guesses = 0

while True:
    difficulty = input("would you like to play with easy, medium or hard difficulty. ")
    if difficulty == 'easy':
        num_guesses = 8
    elif difficulty == 'medium':
        num_guesses = 6
    elif difficulty == 'hard':
        num_guesses = 4
    else:
        print("You must choose easy, medium or hard only.")
    
while True:
    player1 = int(input("Enter a number from between 1 to 50 "))
    if player1 < 1 or player1 > 50:
        print("Incorrect number. Number should be between 1 to 50.")
    else:
        print("Number accepted.")
        break
        
for i in range(num_guesses):
    player2 = int(input("Guess player 1 number "))
    if player2 == player1:
        print("You guessed the correct number ")
        print("The number of guesses made is: ", numoftries)
        break
    else:
        print("You did not guess the correct number ")
        numoftries = numoftries + 1
        if player2 < player1:
            print("Your guess is lower than player 1 guess ")
        elif player2 > player1:
            print("Your guess is higher than player 1 guess ")
            
if player2 != player1:
    print("Game over!")