#valid_password= {}
password = input('Enter your password here :\n>')

if  password.isnumeric():
     print('invalid password')
elif (len(password) < 8):
     print('invalid password')
elif password.isdigit():
     print('invalid password')
elif password.islower():
     print('invalid password')
elif password.isupper():
     print('invalid  password')
# elif special_characters:
#       print('invalid password')
else:
     #password = True
     print('Valid Password')




#      user_input = input('>').lower()
#      user_input = input('>').title()
#      special_characters =
# for i in password >= 8:
#     print('You have successfully created a new password')
# else:
#     print('invalid password') 
    
#correction
password = input("Enter your password. Password must contain:\r\nat least an integer, \r\na capital letter, \r\na capital letter, \r\na small letter, \r\na specialcharacter\r\nand must be more than 8 character\r\n> ")
special_char = ['@','$','#']
invalid = True

if len(password)< 8:
    print("password length should not be less than 8")
    isvalid = False
if len(password) > 16:
    print("password length should not be more than 16")
    isvalid = False
if not any(char.isdigit() for char in password):
    print("password should contain at least a number")
    isvalid = False
if not any(char.islower() for char in password):
    print("password should contain at least a lowercase letter [a-z")
    isvalid = False
if not any(char.isupper() for char in password):
    print("password should contain at least a special character [A-Z]")
    isvalid = False
if not any(char in special_char for char in password):
    print("password should contain at least a special character[@&#]")
    isvalid = False
if isvalid:
    print("password is valid")
else:
    print("invalid password")
