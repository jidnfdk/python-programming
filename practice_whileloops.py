# While Loops, Continue, and Break
'''
Task 1: Print numbers from 1 to 10 using a while loop.
Create a program that uses a while loop to print numbers from 1 to 10.
Example Output: 1 2 3 4 5 6 7 8 9 10
'''
# count = 1
# while count < 11:
#   print(count, end = ' ')
#   count = count + 1

'''
Task 2: Use a while loop to sum numbers from 1 to 100.
Write a program that uses a while loop to sum numbers from 1 to 100 
and prints the result.
Example Output: 5050
'''
# count = 0
# sum = 0
# while count <101:
#   sum = sum + count
#   count = count + 1
# print(sum)
  

'''
Task 3: Repeat user input until they type 'exit'.
Write a program that continuously asks the user for input 
and prints it back, until the user types 'exit'.
Example Input/Output Loop: Hello -> Hello, Python -> Python, exit
'''
# count = 0
# while count == 0:
#   ask_exit = input("Enter exit: ")
#   if ask_exit == "exit":
#     count = count + 1

# import random
# num1 = random.randint(1,50)
# num2 = random.randint(1,50)
# answer = '0' # just a placeholder

# sentence = 'What is ' + str(num1) + ' + ' +  str(num2) + '? '  # + concatenation
# sentence2 = 'What is {} + {}?'.format(num1, num2)
# print(sentence2)
# # expected output is: What is 33 + 44?
# while answer != num1 + num2:
#   answer = int(input(sentence))
  

'''
Task 4: Skip even numbers up to 10 using continue.
Create a program that uses a while loop and continue statement 
to print only odd numbers from 1 to 10.
Example Output: 1 3 5 7 9
'''
# num = 0
# while num <10:
#   num = num + 1
#   if num % 2 == 1:
#     print(num, end=' ')

# num = 0
# while num <10:
#   num = num + 1
#   if num % 2 == 0:
#     continue
#   else:
#     print(num, end=' ')
'''
Task 5: Break a loop when a number greater than 100 is entered.
Write a program that repeatedly asks the user for numbers 
and breaks the loop if the number entered is greater than 100.
Example Input/Output Loop: 10 -> 20 -> 150
'''
# num = 0
# while num <100:
#   num = int(("enter your number: "))
'''
Task 6: Count down from 10 to 1 and then print "Blast off!".
Use a while loop to count down from 10 to 1, then break the loop 
and print "Blast off!".
Example Output: 10 9 8 7 6 5 4 3 2 1 Blast off!
'''

'''
Task 7: Use continue to print all numbers from 1 to 10 except 5.
Create a program that uses a while loop and the continue statement 
to print all numbers from 1 to 10 except 5.
Example Output: 1 2 3 4 6 7 8 9 10
'''

'''
Task 8: Ask for password with a while loop.
Write a program that uses a while loop to ask the user for a password.
Break the loop if the password "python123" is entered.
Example Input/Output Loop: 
Enter password: 1234 -> 
Enter password: abcde -> 
Enter password: python123
'''

'''
Task 9: Use a while loop to create a simple number guessing game.
Write a program that generates a random number between 1 and 10 
and uses a while loop to let the user guess. 
Break the loop when the correct number is guessed.
Example Input/Output Loop: 
Guess the number: 5 -> Wrong, try again. -> 
Guess the number: 7 -> Correct!
'''

'''
Task 10: Create a menu that repeats until a user selects 'Exit'.
Use a while loop to present a user with a set of menu options, 
and use continue to keep showing the menu until 'Exit' is selected.
Example Menu: 
1. Print Hello 
2. Print Goodbye 
3. Exit -> User selects 2 ->
Goodbye -> Menu shown again.
'''

'''
Task 11: Count occurrences of a character until a period is encountered.
Write a program that prompts the user to enter a string and 
counts the occurrence of 'a' until a '.' is encountered.
Example Input: "This is a test string."
Example Output: Number of 'a's: 1
'''

'''
Task 12: Use a while loop to print a triangle using '*'.
Create a program that asks the user for the height of 
the triangle and prints a triangle using '*'.
Example Input: 5
Example Output:
*
**
***
****
*****

'''

'''
Task 13: Implement a simple ATM menu using a while loop.
Write a program that simulates an ATM interface where users 
can choose to display balance, deposit, withdraw, or exit. 
Use continue and break appropriately.
Example Menu: 1. Display Balance 2. Deposit 3. Withdraw 4. Exit
'''

'''
Task 14: Validate user input with a while loop.
Create a program that asks for a user's age and uses a while loop 
to keep asking until they enter a valid age (any positive number).
START
SET valid to False
WHILE NOT valid
    DISPLAY "Enter your age: "
    READ age
    IF age > 0 THEN
        SET valid to True
        DISPLAY "Thank you. Your age is " + age
    ELSE
        DISPLAY "Invalid age. Please enter a positive number."
    ENDIF
ENDWHILE
END
Example Input/Output Loop: 
Enter your age: -1 -> Invalid age. 
Enter your age: 20
'''

'''
Task 15: Use a while loop to reverse a string.
Write a program that takes a string input and uses a while loop 
to reverse the string without using slicing.
Example Input: "hello"
Example Output: "olleh"
'''