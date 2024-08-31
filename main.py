import prac0824_task32021

### NOTES FOr FUNCTIONS
#abs() # returns the absolute value ignores negative or positive
# num = -4
# print(abs(num))

# print(ord("A")) # find the ascii value of capital A
# print(chr(65)) # find the character value of ascii 65

# split, splits a string to a list with a delimiter
# sentence = "I-like-to-eat-chicken-rice"
# newlist = sentence.split("-")
# print(newlist)


### **Q9** Print the integers between 0 and 4 inclusive, in one line.
# for i in range(5):
#   print(i, end = ' ')#0, 1, 2, 3

### **Q10** Print the even numbers between 0 and 10 inclusive 
#(solve using two different methods)
# for i in range(11):
#   if i%2 == 0:
#     print(i)

# for i in range(0,11,2):
#   print(i)

# option 1: range(stop)
# option 2: range(start, stop) 
# option 3: range(start, stop, step)    

### **Q11** Print the even numbers between 0 and 10 inclusive, in descending order.
# for i in range(10,-1,-2):
#   print(i)
  
### **Q12** Write a code to find the sum from 1 to 5 (i.e. 1 + 2 + 3 + 4 + 5)
# num = 0
# for i in range(1,6):
#   num = num + i
# print(num)

### **Q17** Write a program to print the multiplication table of a given number.
'''

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
5 x 11 = 55
5 x 12 = 60
'''
# ask_number = int(input("what is the number you want? "))

# for i in range (1,13):
#   print(ask_number, "x",i,"=",ask_number*i)


### **Q1** Use for i in string to print each character of the given text.
# name = input("Cheer for who? ")
# for c in name:
#   print("Give me a",c,"!")

# print("WHO IS THE BEST?!?!?!?")
# print(name)

  
### **Q2** Use for i in range() to print each character of the given text.
name = 'SAWYERSON'  # ['S', 'A', 'W', 'Y', 'E', 'R']
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

# for i in range(len(name)):
#  print(name[i])


### **Q3** Write a code to print the first 3 uppercase letters of the given word.
'''
word = "WoNdRousLY"
YOU
'''
# another string to remember the upper case letters
# word = "WoNdRousLY"
# upper = ""
# for i in word:
#   if i.isupper():
#     upper = upper+ i
# print(upper[0:3])
#[start:stop:step]


### **Q4** Write a code to print the last 3 uppercase letters of the given word.
# word = "joYOUS"
# upper = ""
# for i in word:
#   if i.isupper():
#     upper = upper+ i
# print(upper[::-1])

#word = "BASKETBALL"

# last 3 characters:
#print(word[-3:])
  # [start:stop:step]


## **Using for loops to print patterns**
### **Q5** Print the following using a for loop.
# word = "DURIAN"
# for i in range(1,len(word)+1):
#   print(word[:i])

'''
A
AP
APP
APPL
APPLE
'''

### **Q6** Print the following pattern using nested for loops.
'''
* * * * *
* * * *
* * *
* *
*
'''
# word = " * "
# for i in range(5,0,-1):
#   print(word*i)