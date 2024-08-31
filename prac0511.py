# Practice 1
'''Create a Password Validator program that checks if a password is strong.
1. Ask the user to input a password.
2. Check if the password is at least 8 characters long.
3. Check if it contains at least one uppercase letter and one lowercase letter
4. Check if it contains one digit.
5. Check if it contains a special character "!@#$%^&*()"
6. Provide feedback on which criteria the password pass/ or fail.
7. Indicate if the password is strong if all criteria are met.'''
# checklength = False
# checkupper = False
# checklower = False
# checkdigit = False
# checkspecial = False
# password = input("Enter your password for check ")
# if len(password) >= 8:
#   checklength = True
# for i in password:
#   if i.isupper():
#     checkupper = True
#   if i.islower():
#     checklower = True
#   if i.isdigit():
#    checkdigit = True
#   if i in "!@#$%^&*()":
#     checkspecial = True

# if checklength and checkupper and checklower and checkdigit and checkspecial:
#   print("Your password is strong")
# else:
#   print("Your password fails the criteria and is weak.")

# Practice 2
'''
Code a Word Guessing Game between 2 persons.
1. Ask Player 1 to input a word for player 2 to guess.
2. Ask Player 2 to input a guess.
  2a. The program will keep asking Player 2 to enter the guess until the correct word is given
3. If Player 2's word guess is too long, inform the player with a suitable message
4. If Player 2's word guess is too short, inform the player with a suitable message
5. If Player 2's word guess is the correct length, inform the player with a suitable message
6. If the word length is correct, give player 2 a hint as to the word
For example: if the Player 1's word is "five", and Player 2 guesses "four",
the program will print "f _ _ _"
7. End the game with suitable messages when Player 2 guesses correctly.
'''
outputword = ''
player1_guess = input("player 1 Enter your word ")
while True:
  player2_guess = input("player 2 Enter your guess ")
  player1_guess = player1_guess.lower()
  player2_guess = player2_guess.lower()
  if len(player2_guess) > len(player1_guess):
    print("Your guess is too long")
  if len(player2_guess) < len(player1_guess):
    print("Your guess is too short")
  if len(player2_guess) == len(player1_guess):
    print("Your guess has the correct length")
    for i in range (len(player1_guess)):
      if player1_guess[i] == player2_guess[i]:
        outputword = outputword + player1_guess[i]
      else:
        outputword = outputword + "_"
        print(outputword)
        break
    if player1_guess == player2_guess:
      print("You won! Your guess matches player 1 word.")
  

# word1 = 'poor'
# word2 = 'poos'
# outputword = ''

# for i in range(len(word1)):
#   if word1[i] == word2[i]:
#     outputword = outputword + word1[i]
#   else:
#     outputword = outputword + " _ "

# print(outputword)