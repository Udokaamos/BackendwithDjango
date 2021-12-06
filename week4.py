#LIST COMPREHENSION

# My_list = []
# for i in range(5):
#     My_list.append(i**2)
# print(My_list)

# a_List = [i**2 for i in range(5)]
# print(a_List)

# b_List = [element+2 for element in range(5)]
# print(b_List)

# c_List = [element+1 for element in range(10) if (element+1)%2==0]
# print(c_List)

# #Dictionary comprehension
# my_dict = {element:element**2 for element in range(10)}
# print(my_dict)

# my_wiki = "I had a great weekend and I know alot of my friends did too even with the assignment"
# my_dict = {}
# for i in my_wiki.split():
#    my_dict[i]=my_dict.get(i, 0) + 1

# print(my_dict)

# #WHILE LOOP
# # from collections import _UserStringT
# from os import write
# import time

# count = 10
# while count >= 0:
#     print(count)
#     count-=1
#     time.sleep(2)

# user_input = int(input('Enter your number :'))
# if user_input >= 0:
#    while user_input >= 0:
#       print(user_input)
#       user_input -= 1
# else:
#     while user_input <0:
#         print(user_input)
#         user_input+=1

#FILE I/O 1/12/2021
# file = open('my_file.txt', 'w')
# file.write("""This is a very good file.
# This us another line. But, i don't like this.
#     Welcome on board.

#       How are you today

# """
# )

# file.close()

# file.writelines(["This is my brother, \nHe's a very good boy"])
# file.close()
#READLINES
# file = open('my_file.txt', 'r')
#To read only
#print(file.read())
#To Read and Write 
# lines = file.readlines()

# for line in lines:
#     print(line)

# #APPEND 
# file = open('my_file.txt', 'a')
# file.write("\nI just got appended.")
# file.close()

# with open('my_file.txt', 'r' ) as file:
#     print(file.read())

# data = {
#     "name":"Gloria"
# }
# with open('my_file.txt', 'w') as file:
#     file.write(f'{data}')
#     print(f'{data}')


# with open('my_file.txt', 'r') as file:
#     doc = file.read()
#     s = eval(doc)
#     print(type(s))

# print(s.get("title"))

# a = "5"
# b = "6"
# c = "['4', '3', '45']"
# print(eval(a)+eval(b))
# print(type(b))
# print(sum(map(int, eval(c))))



import random

with open('game_file.txt','r') as file:
    doc = file.read()
    users = eval(doc)

print("Welcome to this game")

while True:


     input_data = input("Enter l to login or s to signup. \nEnter any other key to quit.\n>").lower()
     with open('game_file.txt') as file:
          if input_data == 'l':
               username = input("username: ")
               password = input("password: ")

               user = users.get(username)

               if user is not None and user['password'] == password:
                    print(f"Enter H for help or any other key to continue. Your highest score is {user['high_score']}")
                    
                    user_input = input('>').lower()
                    help_ = """
                    This is a simple terminal game where you have to guess a word and if
                    your word is equal to the computer's choice then you win!!!
                    
                    Select from the given list of words.
                    """ 
                    if user_input == 'h':
                         print(help_)
                    trial = 3
                    scores = 0
                    while trial > 0:

                         my_list = ['cherry', 'queen', 'ball', 'ace', 'hearts', 'jack']
                         random.shuffle(my_list)
                         print('\n', my_list)
                         user_choice = input("\nGuess the Word:\n>").lower()
                         computer = random.choice(my_list)

                         if user_choice in my_list:
                              if user_choice == computer:
                                   print("You Win")
                                   trial += 1
                                   print(f'\n{trial} trial(s) left\n')

                                   scores += 3
                                   continue
                              else:
                                   print(f'Computer selected {computer}')
                                   print(f"Your new high score is user {user['high_score']}")
                                   print('Try again')

                         else:
                              print('Invalid input. Try again.')
                         trial -=1
                         print(f'\n{trial} trial(s) left\n')
                    if scores > user['high_score']:
                         user['high_score'] = scores
                         # print(scores)   
               else:
                    print('Please enter a valid username and password')
          elif input_data == 's':
               print()
               username = input("username: ")
               password = input("password: ")

               users[username] = {
                    "password": password,
                    "high_score": 0
               }                          

          else:
               print('\nGood bye')
               break
          
# print(users)     
with open('game_file.txt', 'w') as file:
    file.write(f'{users}')
     

    
#FUNTIONS
# def nameoffunction(a, b):
#     c = (a+b)/2
#     return c
# print(nameoffunction(2,3))

# def isPrime(number):
#     if number <= 1:
#         return  False
#     if number == 2:
#         return True

#     for i in range(2, number):
#       if number%i == 0:
#           return False
#       else:
#           return True

# print(isPrime(5))



# def add_num(a,b):
#     print(a-b)
# add_num(b=2, a=5)

# def add_num(*args):
#     return sum(args)
# data = [1,2,3,4,5,6,7,8]
# print(add_num(*data))

# def adsss(**kwargs):
#     print(kwargs)

# def ads(a,b,c):
#     return a*b+c

# a = {'a':3, 'b':4, 'c':2 }
# print(ads(**a))

# def ads(a,b,c=3):
#     return a*b+c

# a = {'a':3, 'b':4, 'c':2 }
# print(ads(**a))