# String and List Operators
# Using + to Concatenate
# List Slicing
'''
Question 1: Extract a portion of a list.
Write a function that takes a list and returns a new list 
that contains only the first three elements of the original list.
Example Input: [1, 2, 3, 4, 5]
Example Output: [1, 2, 3]
'''
## Write and test your code here
def first3(list2):
    
    return list2[:3]

list2 = [123,4,235,345,7,4,5,6,7,8]
print(first3(list2))

'''
Question 2: Get the last three items of a list.
Ask the user for a list of numbers and print the last three items.
Example Input: [10, 20, 30, 40, 50]
Example Output: [30, 40, 50]
'''
## Write and test your code here


'''
Question 3: Create a sub-list from a list using slicing.
Given a list of elements, write a function that returns a 
sublist from the second element to the second last element.
Example Input: [0, 1, 2, 3, 4, 5]
Example Output: [1, 2, 3, 4]
'''
## Write and test your code here
def sublist(list1):
    return list1[1:-1]

list1 = [1,2,3,4,5,6,7,8,9]
print(sublist(list1))

'''
Question 4: Reverse a list using slicing.
Write a function that takes a list and returns it reversed.
Example Input: [1, 2, 3, 4, 5]
Example Output: [5, 4, 3, 2, 1]
'''
## Write and test your code here
def reverselist(list3):
    return list3[::-1]
list3 = [1,2,3,4,5,6,7,8,9,10]
print(reverselist(list3))

'''
Question 5: Slice a list into halves.
Divide a list into two equal halves and returns both halves.
You may assume that the list has an even number of items
Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [1, 2, 3]  [4, 5, 6]
'''
## Write and test your code here

    
list4 = [1, 2, 3, 4, 5, 6]
half1 = list4[:len(list4)//2]
half2 = list4[len(list4)//2: ]
print(half1)
print(half2)
    

'''
Question 6: Extract every second element from a list.
Write a function that returns a list of every second element from the given list.
Example Input: ['a', 'b', 'c', 'd', 'e', 'f']
Example Output: ['b', 'd', 'f']
'''
## Write and test your code here
def secondelement(list5):
    return list5[1::2]
list5 = ['a', 'b', 'c', 'd', 'e', 'f']
print(secondelement(list5))

'''
Question 7: Remove the first and last elements of a list using slicing.
Create a function that takes a list and returns it without 
the first and last elements.
Example Input: [0, 1, 2, 3, 4]
Example Output: [1, 2, 3]
'''
## Write and test your code here



'''
Question 8: Create a function to reverse the order of elements in a 
list only from the second to the last but one.
Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [1, 5, 4, 3, 2, 6]
'''
## Write and test your code here
def reverseorder(list6):
    # return list6[1::]
    middle = list6[1:-1]
    revmiddle = middle[::-1]
    return [list6[0]] + revmiddle + [list6[-1]]
exlist = [1, 2, 3, 4, 5, 6,4,56,46,35,74,345,4353]
print(reverseorder(exlist))
    

'''
# Question 9: Extract the first three characters from a string
# Test case 1: example input: hello, example output: hel
# Test case 2: example input: Python, example output: Pyt
'''
## Write and test your code here

'''
# Question 10: Extract the last three characters from a string
# Test case 1: example input: hello, example output: llo
# Test case 2: example input: Python, example output: hon
'''
## Write and test your code here


'''
# Question 11: Extract a subset of a list from index 2 to 5
# Test case 1: example input: 1 2 3 4 5 6 7, 
example output: [3, 4, 5, 6]
# Test case 2: example input: 10 20 30 40 50 60, 
example output: [30, 40, 50]
'''
## Write and test your code here


'''
# Question 12: Extract every second character from a string
# Test case 1: example input: hello, example output: hlo
# Test case 2: example input: Python, example output: Pto
'''
## Write and test your code here



'''
# Question 13: 
# Write a function called mid3(instring)
# Extract the middle three characters from a string
# Check that the incoming string must be an odd length, 
# Test case 1: example input: abcdefg, example output: cde
# Test case 2: example input: helloworld, example output: Invalid, Even length
'''
## Write and test your code here


'''
# Question 14: Extract the first half of a string
# Test case 1: example input: hello, example output: hel
# Test case 2: example input: Python, example output: Pyt
'''
## Write and test your code here


'''
# Question 15: Extract the second half of a string
# Test case 1: example input: hello, example output: llo
# Test case 2: example input: Python, example output: hon
'''
## Write and test your code here

'''
Question 16:
Write a function to split a string into half
and return the first half and second half
Your function must handle an even/ odd number length of characters
# If the length is odd, you will ignore the middle character
Example Input: "SINGING" Example Output: SIN, ING
Example Input: "FLYING" Example Output: FLY, ING
'''

'''
# Challenge 1:
Write a function `validate_nric(nric: str) -> bool` to 
validate if a given input is a valid Singapore NRIC number. 
A valid NRIC must start with 'S', 'T', 'F', or 'G', followed by 7 digits, 
and ends with an uppercase letter.

* In this case, assume that as long as the last character 
is an uppercase letter it is valid.

Normal Test: Input: "S1234567D", Output: True
Error Test: Input: "A1234567D", Output: False
Boundary Test: Input: "S123456", Output: False
'''

'''
# Challenge 2:
Write a function `is_valid_username(username: str) -> bool` to 
check if a username is correctly generated. A valid username 
should be at least 6 characters long, should not contain any spaces, 
and must start with an uppercase letter followed by lowercase letters.

Normal Test: Input: "Johndoe", Output: True
Error Test: Input: "johnDoe", Output: False
Error Test: Input: "John Doe", Output: False
Boundary Test: Input: "John", Output: False
'''

'''
# Challenge 3:
Write a function `validate_license_plate(plate: str) -> bool` 
to check if a vehicle license plate is valid. 
A valid plate starts with 3 uppercase letters, followed by 4 digits, 
and ends with an uppercase letter.

Normal Test: Input: "SAB1234Z", Output: True
Error Test: Input: "SA1234Z", Output: False
Boundary Test: Input: "SAB123Z", Output: False
'''

'''
# Challenge 4:
Write a function `is_valid_postal_code(postal_code: str) -> bool` 
to validate a Singaporean postal code. A valid postal code consists 
of exactly 6 digits where the first digit must be between 1 and 7.

Normal Test: Input: "123456", Output: True
Error Test: Input: "823456", Output: False
Boundary Test: Input: "12345", Output: False
'''

'''
# Challenge 5:
Write a function `validate_date_format(date_str: str) -> bool` 
to check if a date string is in the format "DD/MM/YYYY" 
where DD, MM, and YYYY are valid digits. 

The function should ensure that DD is between 01 and 31, 
MM is between 01 and 12, and YYYY is a valid 4-digit positive integer.

Normal Test: Input: "29/02/2020", Output: True
Error Test: Input: "32/13/2020", Output: False
Boundary Test: Input: "01/01/0001", Output: True
'''