'''2019-Task4 (20 marks)
You have been asked to create a word game program for two players.

The program must:

> Allow player 1 to input a word that will be converted to lower case 
by the program after entry. The program must ask for another word each 
time the player enters a word that is more than 10 letters.

> Output a message to state how many letters are in the word input by player 1.

> Allow player 2 to enter a single lower case letter (on 10 separate occasions)

> Search for each letter input by player 2, in the word input by player 1

> Output “It is letter number X in the word.” Every a letter is found. 
X must be replaced by the position of the letter in the word.

> Output “That letter is not in the word.: when player 2 inputs a 
letter that is not in the word.

> Output “You have now entered 10 letters.” When player 2 has input all 10 letters.

> Output “What is the word entered by player 1?” after player 2 has input all 10 letters, 
and allow player 2 to enter the word. This is converted to lower case by the program.

> Output “That is the correct word. You win!” if player 2 inputs the same word as player 1.

> Output “That is not the correct word. Player 1 wins!” if player 2 does not input the 
same word as player 1.

Write your program and test that it works.
Save your program as WORDGAME1__<your name>_<center number>_<index number>.py
[13 marks]
'''
# player1 = input("Enter your word that has no more than 10 characters. ")
# player1 = player1.lower()
# while True:
#  if len(player1) > 10:
#      print("Error, word must not be more than 10 characters ")
#      player1 = input("Enter your word again ")
#  else:
#      break
# print("There are",len(player1),"characters in the word. ")

# for i in range(10):
#     player2 = input("enter a letter ")
#     player2 = player2.lower()
#     if len(player2) != 1:
#         print("guess only ONE letter ")
#     position = player1.find(player2) + 1
#     if player2 in player1:
#         print("It is letter number",position,"in the word ")
#     else:
#         print("That letter is not in the word ")
# print("You have now entered 10 letters ")
# print("What is the word entered by player 1? ")
# player2_guess = input("Enter your guess. ")
# player2_guess = player2_guess.lower()
# if player2_guess == player1:
#     print("That is the correct word. you win! ")
# else:
#     print("That is not the correct word. Player 1 wins! ")

    
'''
When your program is complete, test it for the following:

Test 1 – Player 1 inputs the word indescribable
Test 2 – Player 1 inputs the word excited
Player 2 inputs the letters a, c, s, i, m, d, u, e, o, t and inputs the word excited
Test 3 – Player 1 inputs the word xylophone
Player 2 inputs the letters e, f, u, o, i, p, h, d, c, t and inputs the word saxophone
Take a screenshot of Test 1 and Test 2. Save this single screenshot as:

TEST1and2_<your name>_<center number>_<index number>
Take a screenshot of Test 3. Save this screenshot as:
Test3_<your name>_<center number>_<index number>
Save your file in either .png or .jpg format.
[3 marks]
'''

'''
Save your program as WORDGAME2__<your name>_<center number>_<index number>.py

Extend your program to:

> Output a message to ask whether player 2 wants to enter the word input 
by player 1, each time player 2 enters a correct letter from the word. 
The program must then allow player 2 to enter this word if the answer is yes.

> Allow player 2 to enter another letter, even if the word they input is 
incorrect. This is repeated until all 10 letters have been input or the 
correct word is input.

> Output a suitable message and end the game if, at any point, player 2 
inputs the correct player 1 word.
[4 marks]
'''
player1 = input("Enter your word that has no more than 10 characters. ")
player1 = player1.lower()
empty = 0

while True:
 if len(player1) > 10:
     print("Error, word must not be more than 10 characters ")
     player1 = input("Enter your word again ")
 else:
     break
print("There are",len(player1),"characters in the word. ")

for i in range(10):
    player2 = input("enter a letter ")
    player2 = player2.lower()   
    if len(player2) != 1:
        print("guess only ONE letter ")
        
    position = player1.find(player2) + 1
    
    if player2 in player1:
        print("It is letter number",position,"in the word ")
        ask_question = input("Would you like to enter the word input by player 1 (yes/no)")
        ask_question = ask_question.lower()
        if ask_question == "yes":
            player2_guess = input("Enter your guess ")
            if player2_guess == player1:
                print("You have guessed correctly")
                empty = 1
                break
            else:
                print("Your guess is wrong ")
    else:
        print("That letter is not in the word ")

if empty == 0:
    print("You have now entered 10 letters ")
    print("What is the word entered by player 1? ")
    player2_guess = input("Enter your guess. ")
    player2_guess = player2_guess.lower()
    if player2_guess == player1:
        print("That is the correct word. you win! ")
    else:
        print("That is not the correct word. Player 1 wins! ")
    

