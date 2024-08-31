'''
2019 – Task 2 [10] 
The following program creates a username for a user. It creates the 
username by taking the first letter of the user’s first name and 
combining it with the user’s last name. It will also allow the user to enter a password. 
The first name is entered without a space, for example, Ah Seng is input as AhSeng. 
'''
# firstname = input("Please enter your first name: ") 
# lastname = input("Please enter your last name: ") 
# username = firstname[0] + lastname 
# print("Your username is " + username) 
# password = input("Please enter a password: ") 

 
'''
Open the file USERNAME.py 
Save the file as MYUSERNAME_<your name>_<center number>_<index number>.py 
Edit the program so that the username is created using the 
first three letters of the first name, along with the lastname.  

[1] 
'''
# firstname = input("Please enter your first name: ") 
# lastname = input("Please enter your last name: ") 
# username = firstname[:3] + lastname 
# print(username)
# print("Your username is " + username) 
# password = input("Please enter a password: ") 
'''
The program needs to validate both the length of the password and 
whether the user has correctly re-entered their password. 
Edit the program to: 

Test whether the user has entered a password of eight characters or more. 
Output a suitable error message that asks the user to enter a 
password again if the password is less than eight characters, and 
repeat this until the user enters a valid password. 
[4] 
'''
# firstname = input("Please enter your first name: ") 
# lastname = input("Please enter your last name: ") 
# username = firstname[:3] + lastname 
# print(username)
# print("Your username is " + username) 

# while True:
#     password = input("Please enter a password: ") 
#     if len(password) < 8:
#         print("Invalid password . Password must be equal to or more than eight characters")
#     else:
#         print("Password verified ok.")
#         break

    
'''
Edit the program to: 

Asks the user to re-enter their password 
Check that the second entry of the password matches the first entry 
Output the message “Your password has been set.” If the password entries match 
Otherwise, output the message “Password entries do not match. 
Please repeat the second entry of your password: “ and read in the 
password again, and repeat this until the password entries match. 
[5] 

Save your program. 
'''

firstname = input("Please enter your first name: ") 
lastname = input("Please enter your last name: ") 
username = firstname[:3] + lastname 
print(username)
print("Your username is " + username) 

while True:
    password = input("Please enter a password: ") 
    if len(password) > 8:
        print("Invalid password . Password must be less than eight characters")
    else:
        break

while True:
    repeated_pass = input("Please re-enter your password. ")
    if repeated_pass == password:
        print("Your password has been set.")
        break
    else:
        print("Your password entries do not match. Please repeat the second entry of your password :")
        
