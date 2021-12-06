# #Classwork
# import random
# import time

# user = {
#    "Gloria":{
#      "password":"ritadominic",
#      "highest_score" : 0
#    }
# }

# list_of_unique_words = ["Fast", "Mingle", "Safe", "Univelcity", "Students", "Intelligent", "Nice", "Questions", "Assignments", "Reflection"]
# random.shuffle(list_of_unique_words)
# computer_choice = random.choice(list_of_unique_words)
# print('welcome To Guessing Game!!! \r\nDo you have an account, yes or no?')

# user_input = input('>').lower()

# if input == 'yes':
#      time.sleep(1)
#      user_login = print(input('Username :'))
#      time.sleep(1)
#      user_password = print(input('Password :'))
#      if user_login == user and user_password == "ritadominic":
#         time.sleep(2)
#         print('Login to your account')
# else:
#     signup_ = """
# CREATE YOUR ACCOUNT
#  """ 
#     print(signup_)


# userName = input('username :')
# password = input('Create Password :')
# special_char = ['@','$','#','!','.','^','&','*',',']
# isvalid = True
# if len(password) < 8:
#      print("password length should not be less than 8")
#      svalid = False
# if len(password) > 16:
#     print("password length should not be more than 16")
#     isvalid = False
# if not any(char.isdigit() for char in password):
#     print("password should contain at least a number")
#     isvalid = False
# if not any(char.islower() for char in password):
#     print("password should contain at least a lowercase letter [a-z")
#     isvalid = False
# if not any(char.isupper() for char in password):
#     print("password should contain at least a special character [A-Z]")
#     isvalid = False
# if not any(char in special_char for char in password):
#     print("password should contain at least a special character[@$#!.^&*,]")
#     isvalid = False

# comfirm_password = input('Comfirm Password :')
# for i in range(1):
#    if password == comfirm_password:
#      print('You have successfully created an accout, please login to start')
#    else:
#      print('invali user, try again')
#      time.sleep(2)



# print('If you want to read instructions, Press H')
# user = input().lower()
# if user == 'h':
# print('The instruction of the game states that when a player guesses a word that was randomly picked by the the computer, the player wins, else the player looses.... ')
# # else:
# #     print('Invalid command')
# print("Please select from the list below")
# print(list_of_unique_words)
# users_guess = input('Guess a word:\n>')
# if users_guess == computer_choice:
#      print('WINS')
# elif users_guess != computer_choice:
#      print('LOOSE')
# elif users_guess != list_of_unique_words:
#      print('Sorry, word not on the list')
# else:
#      print('Game Over')
# print(f'Computer selected word is {computer_choice}')



# CORRECTION

import random
users = {
     'gloria':{
          'password':'backendwithdjango',
          'high_score':0
     }
}

print("Welcome to this game")

while True:


     input_data = input("Enter l to login or s to signup. \nEnter any other key to quit.\n>").lower()

     if input_data == 'l':
          username = input("username: ")
          password = input("password: ")

          user = users.get(username)

          if user is not None and user['password'] == password:
               print("Enter H for help or any other key to continue")
               user_input = input('>').lower()
               help_ = """
               This is a simple terminal game where you have to guess a word and if
               your word is equal to the computer's choice then you win!!!
               
               Select from the given list of words.
               """ 
               if user_input == 'h':
                    print(help_)
               trial = 3
               score = 0
               while trial > 0:

                    my_list = ['cherry', 'queen', 'ball', 'ace', 'hearts', 'jack']
                    random.shuffle(my_list)
                    print('\n', my_list)
                    user_choice = input("\nGuess the Word:\n>").lower()
                    computer = random.choice(my_list)

                    if user_choice in my_list:
                         if user_choice ==computer:
                              print("You Win")
                              trial += 1
                              print(f'\n{trial} trial(s) left\n')

                              scores = 3
                              continue
                         else:
                              print(f'Computer selected {computer}')
                              print('Try again')

                    else:
                         print('Invalid input. Try again.')
                    trial -=1
                    print(f'\n{trial} trial(s) left\n')
               if score > user['high_score']:
                    user['high_score'] = scores   
          else:
               print('Please enter a valid username and password')
     elif input_data == 's':
          #print()
          username = input("username: ")
          password = input("password: ")

          users[username] = {
               "password": password,
               "high_score": 0
          }                          

     else:
          print('\nGood bye')
          break
     
     
print(users)


