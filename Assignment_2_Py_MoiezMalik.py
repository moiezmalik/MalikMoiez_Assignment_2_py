import user_login
#ask user to enter first name
first_name = str(input('Enter Student First Name: '))
##ask user to enter last name
last_name = str(input('Enter Student Last Name: '))
#ask user to enter user student ID
student_id = str(input('Enter Student ID: '))

#call get_login_name method and print the username
print(user_login.get_login_name(first_name,last_name,student_id))




#-----Generate Password Start-------
print('Create your password, Password must be minimum 7 character and contian 1 uppercase, 1 lowercase and 1 special character')

password = input('Enter Your password: ')

#validate if password contain Uppercase, Lowcase and special charactor and 7 char or longer. 
def validate_password(p):
    upperCase = False
    isDigit = False
    isLowerCase = False
    correct_length = False
	
    if len(p) >= 7:
        correct_length = True    
        for character in p:
            if character.islower():
                isLowerCase = True
            if character.isdigit():
                isDigit = True
            if character.isupper():
                upperCase = True

    if upperCase & isDigit & isLowerCase & correct_length:
        valid_password = True
    else:
        valid_password = False
    return valid_password

if validate_password(password):
    input('Your password been created, Press Enter to exit...')
else:
    input('Invalid password. Press Enter to exit...')

