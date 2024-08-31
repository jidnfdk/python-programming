'''
A 2-player game is being programmed.
The following program allows each player, in turn, to enter the names of 5 animals. 
It converts the name of each animal to lower case. 
Each animal entered by player 2 is their guess for the animal entered by player1.
'''

# num_of_animals = 5
# for x in range(num_of_animals):
#   p1_animal = input("Player 1, please enter an animal: ")
#   p1_animal = p1_animal.lower()
#   p2_guess = input("Player 2, please enter your guess: ")
#   p2_guess = p2_guess.lower()

'''
# Open the file ANIMALGAME.py
# Save the file as ANIMAL_2023_<your name>_<centre number>_<index number>.py

#######################
Question 1: 
6.	Edit the program to allow player 1 to keep entering animals until that player 
does not want to enter any more. All animals entered by player 1 must 
be stored in a list. 

Once all animals have been entered by player 1, player 2 will enter a single guess. 

All inputs and outputs must have suitable messages. 

Save your program. 
'''
# Write your code here

# while True:
#   p1_animal = input("Player 1, please enter an animal: ")
#   p1_animal = p1_animal.lower()
#   p1_decision = input("If you would like to stop entering animals type Stop else type continue ")
#   p1_decision = p1_decision.lower()
#   if p1_decision == "stop":
#     break

# p2_guess = input("Player 2, please enter your guess: ")
# p2_guess = p2_guess.lower()

'''
#######################
Question 2:
7.	Save your program as ANIMAL2_2023_<your name>_<centre number>_<index number>.py [3 marks]

Edit your program to search the list of animals to find the guess 
entered by player 2. 
Player 2 has a score that starts at 0. 
If the guess entered by player 2 is found in the list:

> the animal is removed from the list
> the score for player 2 is incremented by 1

Save your program.
########################
'''
# p1_animal = []
# score = 0
# while True:
#   Animal = input("Player 1, please enter an animal: ")
#   Animal = Animal.lower()
#   p1_animal.append(Animal)

#   p1_decision = input("If you would like to stop entering animals type Stop else type continue ")
#   p1_decision = p1_decision.lower()
#   if p1_decision == "stop":
#     break

# p2_guess = input("Player 2, please enter your guess: ")
# p2_guess = p2_guess.lower()
# print(p1_animal) # testing
# if p2_guess in p1_animal:
#   score = score + 1
#   p1_animal.remove(p2_guess)
# print(p1_animal)
'''
Question 3:
8.	Save your program as ANIMAL3_2023_<your name>_<centre number>_<index number>.py

Edit your program to allow player 2 to keep entering guesses until they 
enter an animal that is not found in the list, or until the list is empty. 
When player 2 enters an animal that is not found in the list:

> the game ends and informs player 2 the game is over
> a message is displayed showing:
- player 2 their score
- the animals that are still in the list.

All inputs and outputs must have suitable messages.
Save your program.

[3 marks]
'''
p1_animal = []
score = 0
while True:
  Animal = input("Player 1, please enter an animal: ")
  Animal = Animal.lower()
  p1_animal.append(Animal)

  p1_decision = input("If you would like to stop entering animals type Stop else type continue ")
  p1_decision = p1_decision.lower()
  if p1_decision == "stop":
    break
while True:

    # check if list is already empty
    if len(p1_animal) > 0:
        p2_guess = input("Player 2, please enter your guess: ")
        p2_guess = p2_guess.lower()
        if p2_guess in p1_animal:
            score = score + 1
            p1_animal.remove(p2_guess)
        else:
            print("Game over! Your score is : ", score)
            print("The animals that are still in the list are :")
            for a in p1_animal:
                print(a)
            break
    else:
        # you win because no more animals
        print("Congrats you win")
        break

       
 