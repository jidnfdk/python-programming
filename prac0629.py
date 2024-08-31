'''
# Task 3
# The eggs in most European countries must be stamped with a 
# code to help consumers track the origin and supply chain of the eggs sold.

# Here is an example of the code and an explanation of how it works:
# 1UK56789

# • The first character is a number between 0 to 3 (inclusive).
# It represents the type of farming method of the eggs
# 0: Organic, 1: Free Range, 2: Barn, 3: Cage

# • The second and third character represents the country of origin
# UK: United Kingdom, FR: France, NL: Netherlands

# • The remaining characters, ranging from 2 to 5 digits, 
# represents the farm identification number

# The program below is used to check the validity of the egg codes 
# for a sample of 5 eggs. If the egg codes are all valid, 
# the program should display the number of eggs in the sample 
# according to their farming method and country of origin.

# egg_code = ['1UK42211','2FR9292','1UK29292','0NL24555','0NL93933']

##########################################################

Save your program as MYEGG_2023_<Your name>_<Centre number>_<Index number>.py
11 Identify and correct the errors in the program so that it works according to the requirements given.
Save your program.
'''
# egg_code = ['1UK42211','2FR9292','1UK29292','0NL24555','0NL93933']
# valid = 0

# for i in range(len(egg_code)):
#     check = 0
#     if len(egg_code[i]) > 7:
#         check += 1
#     if egg_code[i][0] in [0123]:
#         check += 1
#     if egg_code[i][1:3].isalpha:
#         check += 1
#     if egg_code[i][3:].isdigit:
#         check += 1
#     if check == 3:
#         valid = 1
# if valid == len(egg_code):
#     print("Codes for the entire batch of eggs are valid.")
#     # Collate the number of eggs sampled according to farm method
#     farm_method_eggs = [0,0,0,0]
#     for j in range(len(egg_code)):
#         farm_method_eggs[egg_code[j][0]] += 1
#     farm_method = ['Organic','Free Range','Barn','Cage']
#     for k in range(len(egg_code)):
#         print("Number of {0} eggs: {1}".format(farm_method[k],farm_method_eggs[k]))
#     # Collate the number of eggs sampled according to country of origin
#     countries = ['UK', 'FR', 'NL']
#     countries_eggs = [0,0,0]
#     for m in range(len(egg_code)):
#         for n in range(len(countries)):
#             if egg_code[m][:2] == countries[n]:
#             countries_eggs[m] += 1
#     for p in range(len(countries_eggs)):
#         print("Number of {0} eggs: {1}".format(countries[p], countries_eggs[p]))
# else
#     print("Invalid egg codes found for this batch of eggs.")
#     print("No data will be presented.")

##THIS IS BACKUP CODE

egg_code = ['1UK42211','2FR9292','1UK29292','0NL24555','0NL93933']
valid = 0

for i in range(len(egg_code)):
    print('inside the loop')
    check = 0
    if len(egg_code[i]) >= 5 and len(egg_code[i]) <= 8: #ERROR 4 change to 8
        print("inside the 1st condition")
        check += 1
    if egg_code[i][0] in ['0','1','2','3']: #ERROR
        print("inside 2")
        check += 1
    if egg_code[i][1:3].isalpha(): #ERROR
        print("inside 3")
        check += 1
    if egg_code[i][3:].isdigit(): #ERROR
        print("inside 4")
        check += 1
    if check == 4: # ERROR 
        valid = valid + 1
        
if valid == len(egg_code):
    print("Codes for the entire batch of eggs are valid.")
    # Collate the number of eggs sampled according to farm method
    farm_method_eggs = [0,0,0,0] # using this to count the farming method
    for j in range(len(egg_code)):
        print(egg_code[j][0])
        farm_method_eggs[int(egg_code[j][0])] += 1 # temp comment, uncomment later
    print(farm_method_eggs)
    farm_method = ['Organic','Free Range','Barn','Cage']
    for k in range(len(farm_method)):
        print("Number of {0} eggs:{1}".format(farm_method[k],farm_method_eggs[k]))
    # Collate the number of eggs sampled according to country of origin
    countries = ['UK', 'FR', 'NL']
    countries_eggs = [0,0,0]
    for m in range(len(egg_code)):
        for n in range(len(countries)):
            # print(egg_code[m][1:3])
            # print(countries[n])
            if egg_code[m][1:3] == countries[n]: #Error wrong slicing
                countries_eggs[n] += 1 #ERROR 2 INDENT
    for p in range(len(countries_eggs)):
        print("Number of {0} eggs: {1}".format(countries[p], countries_eggs[p]))
else: #ERROR 3 COLON
    print("Invalid egg codes found for this batch of eggs.")
    print("No data will be presented.")
