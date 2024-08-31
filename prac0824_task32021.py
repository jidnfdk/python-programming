'''
A program asks the user to enter a word. The program convers the word 
entered to lower case. 

The program checks if the word entered is valid or invalid.
A word is invalid if it:
    -	Begins with the letter ‘a’; or
    -	Ends with the letter ‘a’; or
    -	Contains the letter ‘e’
The program displays a suitable message to indicate why the word is invalid. 
This will be for the first error that is found and not for all errors. 

For example, if the word apple is entered, the error reported is that it 
begins with the letter ‘a’.

If the word is valid, the program categorises the word as :
    -	Short if the word is 4 characters or less in length
    -	Medium if the word is 5 to 8 characters in length
    -	Long if the word is more than 8 characters in length
    The program displays a suitable message to show the category of the word.
'''
word = input("Please enter your word: ")
word = word.lower() #Error 3
begin_a = word.startswith("a") #Error 4
end_a = word.endswith("a")
contain_e = word.find("e") #error 5
word_length = len(word) #Error 10
if not begin_a and not end_a and contain_e == -1: #Error 1
    if word_length <= 4: #Error 7
        print("The length of the word is short.")
    elif word_length <= 8: #Error 6
        print("The length of the word is medium.")
    else:  #Error 2
        print("The length of the word is long.")
if begin_a:
    print ("You entered a word that begins with 'a'.")
elif end_a:
    print("You entered a word that ends with 'a'.")
elif  contain_e: #Error 8
    print("You entered a word that contains 'e'.") #Error 9

'''
Open the file WORDGAME.py
Save the file as MYWORDGAME_2021_<your name>_<centre number>_<index number>.py
9.	Identify and correct the errors in the program so that it works 
according to the requirements given. 

Save your program.

[10]
'''
# word = input("Please enter your word: ")
# word = word.islower()
# begin_a = word.beginswith("a")
# end_a = word.endswith("a")
# contain_e = word("e")
# word_length = word.length()
# if not begin_a and not end_a and contain_e = -1:
#     if word_length < 4:
#         print("The length of the word is short.")
#     elif word <= 8:
#         print("The length of the word is medium.")
#     elif:
#         print("The length of the word is long.")
# if begin_a:
#     print ("You entered a word that begins with 'a'.")
# elif end_a:
#     print("You entered a word that ends with 'a'.")
# elif not contain_e:
#     print("You entered a word that contains 'a'.")