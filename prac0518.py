'''
### Task 1a : Square Integers

In wireless communication, the signal strength decreases as the distance 
from the transmitter increases. The decrease is proportional to the square 
of the distance, which is known as the inverse square law.

Let *dist* be an infinite set of square integers : {1, 4, 9, 16, 25, ...}, 
describing each step of signal loss, where *x* is the distance 
from the transmitter to receiver.

Write a user-defined function, `signal_loss(x)`, where *x* is an integer, 
that returns the number of square integers less than *x*. 
`signal_loss(x)` will return an integer.

E.g.  
*x* = 10 returns `3`.  
[4m]
'''
# def signal_loss(x):
#   number = 1
#   count = 0
#   while number**2 < x:
#     number = number + 1
#     count = count+ 1
#   return count
# test = signal_loss(10)
# print(test)
  
  
#Function practice
# def areaofcircle(rad):
#   area= 3.14*rad*rad
#   return area

# circle1 = areaofcircle(14)
# circle2 = areaofcircle(89)
# circle3 = areaofcircle(55)
# print(circle1)
# print(circle2)
# print(circle3)
# circle 1 = 14, circle 2 = 89, circle 3 = 55

'''
### Task 1b : UI
Write a simple User Interface to do the following:
- Ask user to input a number, *x*.  
- Use `signal_loss()` and display the number of square integers in *dist* 
that are less than *x*.
- Repeatedly ask if the user wants to enter another number. 
- Quit the program when the user indicates that he or she does not want 
to enter another number.  

Appropriate input and output prompts must be included.  
[6m]
'''


# def signal_loss(x):
#   number = 1
#   count = 0
#   while number**2 < x:
#     number = number + 1
#     count = count+ 1
#   return count

# while True:
#   ask_user = input("Enter a number, type stop to end ")
#   ask_user = ask_user.lower()
#   if ask_user == 'stop':
#     break
#   else:
#     distance = signal_loss(int(ask_user))
#     print(distance)
  


'''
#### Task 2a : Repetitive Pattern
String Matching is the classical and existing problem. 
String matching strategies or algorithms provide a key role in 
various real world problems or applications. A few of its imperative applications 
are Spell Checkers, Spam Filters, Intrusion Detection System, Search Engines, 
Plagiarism Detection, Bioinformatics, Digital Forensics and 
Information Retrieval Systems etc.

A message, *s*, may contain corrupted characters during the transmission process 
(e.g. due to signal loss). Some clean-up processes may be employed to 
improve message integrity.

Write a user-defined function, `is_repetitive(s)`, where *s* is a string. 
The function will **only retain all characters that are letters and numbers**. 
All characters will be converted to lower case. 
The string *s* is said to have a 
repetitive pattern if both the halves of *s* are the same. 
If the length of *s* is odd, then the character in the middle of *s* is ignored. 
If *s* has a repetitive pattern, `is_repetitive(s)` will return the Boolean value `True`, 
and otherwise return `False`. Strings with 1 or less character will also return `False`.

E.g.   
"SGD$5S GD5" returns `True`.  # remove spaces sgd5 == sgd5
"abcdabc" returns `True`.  
"SST10SST" returns `False`.  
[6m]
'''

# def is_repetitive(s):
#   clean = ''
#   for text in s:
#     if text.isdigit() or text.isalpha():
#       clean = clean + text
#   clean = clean.lower()
   
#   wordlength = len(clean) 
#   midindex = wordlength // 2
#   if midindex%2 == 0:
#     half1 = clean[:midindex]
#     half2 = clean[midindex:]
#   else:
#     indexafter = midindex + 1
#     half1 = clean[:midindex]
#     half2 = clean[indexafter:]
  
#   if wordlength < 2:
#     return False
  
#   if half1 == half2:
#     return True
#   else:
#     return False

# answer1 = is_repetitive('SGD$5S GD5')
# answer2 = is_repetitive('abcdabc')
# answer3 = is_repetitive('SST10SST')
# print(answer1)
# print(answer2)
# print(answer3)
#print(is_repetitive)




'''
#### Task 2b : FileIO
In the file **Task2B_data.txt**, the first line contains a number, *n*.  
Subsequently, there are *n* number of lines, each contains a string.  

Write a program to read in **Task2B_data.txt**. For each string, display if the string 
has a repetitive pattern.  

Your program should use the `is_repetitive(s)` function.

Appropriate formatted output prompts must be included.  
[4m]
'''
def is_repetitive(s):
  clean = ''
  for text in s:
    if text.isdigit() or text.isalpha():
      clean = clean + text
  clean = clean.lower()

  wordlength = len(clean) 
  midindex = wordlength // 2
  if midindex%2 == 0:
    half1 = clean[:midindex]
    half2 = clean[midindex:]
  else:
    indexafter = midindex + 1
    half1 = clean[:midindex]
    half2 = clean[indexafter:]

  if wordlength < 2:
    return False

  if half1 == half2:
    return True
  else:
    return False

# answer1 = is_repetitive('SGD$5S GD5')
# answer2 = is_repetitive('abcdabc')
# answer3 = is_repetitive('a b c a b c')
# answer4 = is_repetitive('PoowPee')
# answer5 = is_repetitive('Booboo')
# print(answer1)
# print(answer2)
# print(answer3)
# print(answer4)
# print(answer5)

# open a file and read it
f = open('task2b_data.txt', 'r') # opens a file with read option 

lines = f.readlines() # read every single line in file, line by line, and puts in in a list
print(lines)

for l in lines:
  # print(l)
  temp = is_repetitive(l)
  #print(l.strip(), ' is repetitive = ', temp)
  print(f'{l.strip()} is repetitive = {temp}')