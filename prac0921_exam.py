'''
Task 4
Open the file SPLIT_SENTENCE.py. You will see the following function that 
takes a string of words, passed as the parameter word_string, splits it 
into individual words and stores these words in a list. 
It returns the list of words. 

You can assume the string does not contain punctuation marks.
'''
def split_sentence(word_string):
    list_sentence = word_string.split(" ")
    return list_sentence

'''
10.	Save the program as CHECK_LIST_2023_<your name>_<centre number>_<index number>.py [7 marks]

Extend the program by writing another function check_list() that searches 
through the list of words to find a certain word. 

If it finds the word in the list, it returns "Yes", otherwise it returns "No". 
The variable word needs to be passed to the function. 
The function you write must use the function split_sentence() already provided.

Save your program.
'''
# write your code here
def check_list(word, sentence):
    # to process the sentence into a list of words
    sentence_list = split_sentence(sentence)
    if word in sentence_list:
        return "Yes"
    else:
        return "No"

print(check_list("hungry", "i am hungry")) # returns yes
print(check_list("full", "i am hungry")) # returns no

'''
11.	Save your program as REVERSE_2023_<your name>_<centre number>_<index number>.py [7 marks]

Extend your program by writing another function reverse_sentence() 
that reverses the words in the string and returns the whole string reversed, 
with spaces between the words. 

For example, 
"the cat sat on the mat" would return: "mat the on sat cat the". 

The function you write must use the function split_sentence() already provided. 
You must not use the slice operator or the reverse function available in Python. 
Your program does not need to consider any spaces before or after 
the reversed sentence.

Save your program.
'''
# write your code here
def reverse_sentence(sentence):
    sentence_list = split_sentence(sentence)
    #print(sentence_list)
    list_reversed = []
    for s in sentence_list:
        list_reversed.insert(0, s)
    #print(list_reversed)

    # s = " ".join(list_reversed)
    # print(s)

    output = ""
    for item in list_reversed:
        output = output + item + " "
    return output



print(reverse_sentence("the cat sat on the mat"))

'''
12.	Save your program as FUNCTIONS_2023_<your name>_<centre number>_<index number>.py [6 marks]

Extend your program by using the functions created such that it:
•	allows the user to input a string of words (validation of this is not necessary)
•	allows the user to input a word to search for in the string of words
•	outputs the string of words, split into a list
•	outputs the string of words, reversed
•	outputs whether the word input is found in the string of words.
Save your program.
'''
sentence = input("What is your sentence? ")
word = input("What is your word? ")

listsentence = split_sentence(sentence)
print(listsentence)

reversed = reverse_sentence(sentence)
print(reversed)

output = check_list(word, sentence)
print("The word ", word, " is in ", sentence)
print("The word {} is in {}".format(word, sentence))
