'''
2020 – Task 3 [10]
A company sells pens that are packaged and sent to customers.
The program on the next page checks the size and 
weight of each package before it is sent.
The package will be rejected if it does not have the following 
length, width and weight:
-	Length of 15 cm
-	Width of 5 cm
-	Weight of 25g

The program counts and outputs:
-	The total number of packages that are sent as they have the correct 
    length, width and weight
-	The total number of packages that are rejected
-	The total number of packages that are checked.
The program allows a user to continue to check packages until the user enters 
the letter “N” when prompted.
There are several syntax errors and logic errors in the program.
'''

sent = 0
rejected = 0
length_check = 15
width_check = 5
weight_check = 25
count = 0 #Error 10
flag = True
while flag == True: #Error 3
    package_length = int(input("Enter the length of the package: "))
    package_width = int(input("Enter the width of the package: "))
    package_weight = int(input("Enter the weight of the package: ")) #syntax error 2
    count = count + 1 #Error 11
    if package_length > length_check or package_length < length_check:
        print("The package is rejected")
        rejected = rejected + 1
    elif package_width > width_check or package_width < width_check: #Error3
        print("The package is rejected")
        rejected = rejected + 1 #Error 4
    elif package_weight > weight_check or package_weight < weight_check:
        print("The package is rejected")
        rejected = rejected + 1
    else:
        print("The package is the correct size and weight")
        sent = sent + 1  #Error 5
    more_packages = str(input("Would you like to check another package, Y or N?: ")).upper() #Error 6 #Error 9
    
    if more_packages == "N": #Error 7
        flag = False
    
    print("You checked " + str(count) + " packages.")
print(str(sent) + " " + "packages were sent and " + str(rejected) + " " + "packages were rejected") #Syntax error 1 #error 8 #Error 12

'''
Open the file PACKAGES.py
Save the file as MYPACKAGES_2020_<your name>_<center number>_<index number>.py

1.	Identify and correct the errors in the program so that it works 
according to the requirements given.
Save your program.
[10]
'''
# sent = 0
# rejected = 0
# length_check = 15
# width_check = 5
# weight_check = 25
# count = 10
# flag = True
# while flag == False:
#     package_length = int(input("Enter the length of the package: "))
#     package_width = int(input("Enter the width of the package: "))
#     package_weight = int(input("Enter the weight of the package: ")
#     count = count - 1
#     if package_length > length_check or package_length < length_check:
#         print("The package is rejected")
#         rejected = rejected + 1
#     elif package_width > width_check or package_width < length_check:
#         print("The package is rejected")
#         rejected = sent + 1
#     elif package_weight > weight_check or package_weight < weight_check:
#         print("The package is rejected")
#         rejected = rejected + 1
#     else:
#         print("The package is the correct size and weight")
#         rejected = sent + 1
#     more_packages = int(input("Would you like to check another package, Y or N?: "))

#     if more_packages == N:
#         flag = False

#     print("You checked " + str(count) + " packages.")
#     print((sent) + " " + "packages were sent and " + str(rejected) + " " + "packages were rejected")