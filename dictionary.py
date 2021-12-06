# my_dict = {
#     "name": "Gloria",
#     "class": "Python", 
#     "country": "U.S.A"
# }

# my_class = my_dict["class"]

# my_dict["height"] = 100

# my_username = input('Enter your username:\n>')
# print(my_username)
# my_dict['username'] = my_username
# #print(my_dict)



# my_dict = {}
# my_username = input ('Enter your username:\n>')
# my_surname = input('Enter your surname:\n>')
# my_age = input ('Enter your age:\n>')
# my_brother = input ('Enter your brother:\n>')
# my_state = input('Enter your state:\n>')

# my_dict['my_username'] = my_username
# my_dict['my_surname'] = my_surname
# my_dict['age'] = my_age
# my_dict['my_state'] = my_state
# my_dict['my_brother'] = my_brother

#print(my_dict)

# my_firstname = input ('Enter your firstname:\n>')
# my_lastname = input ('Enter your lastname:\n>')
# my_age = int(input ('Enter your age:\n>'))
# dob = str(2021- my_age)
# username = my_firstname[0:3]+my_lastname[0:2]+dob[-2:]

# my_dict = {username: {
#     "firstname": my_firstname,
#     "lastname": my_lastname,
#     "age" : my_age,
#     "dob" : dob
#     } }

# print(my_dict)

# variable = {
#     "name":"Desmond",
#     "ocupation":"Backend Dev",
#     "location":"silicon Valley",
#     "zone":"USA"
# }
# variable['country'] = variable.pop('zone')
# print(variable)

# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
# zipped = zip(first_list, second_list)

# dictionary = dict(zip(first_list, second_list))
# lists = list(zip(first_list, second_list))
# tuples = tuple(zip(first_list, second_list))
# sets = set(zip(first_list, second_list))

# print(zipped)
# print(dictionary)
# print(lists)
# print(tuples)
# print(sets)

# a = [0, 1, 2, 3, 4]
# b = [4, 3, 2, 1, 0]
# dict(zip(a,b))

# names = { 'sarah', 'gloria', 'ife', 'chuka', 'ify'}
# names_count = len(names) 

# print(names_count)

# scores = { 10, 20, 30, 40, 45, 50, 60, 75 }
# scores_count = len(scores)

# print(scores_count)
# print(sum(scores))

# average = sum(scores)/scores_count

# print(average)

# # print(min(scores))

# # print(max(scores))

# range = max(scores) - min(scores)

# print(range)

# print(range(0, 5))
# print(list(range(0,5)))

# my_equation = lambda a, b, c : (-b + (b**2 - (4*a*c))**0.5)/(2*a)

# print(my_equation(1,2,3))

#lamba function
# my_name = lambda word: word.lower()

# print(my_name("GLORIA"))


# my_word = lambda word: list(set(word.upper().split())) 

# sentence = "this is chibuzo and chibuzo is a boy"

# print(my_word(sentence))

# my_func = lambda x: x**2
# my_list = [33, 32, 4, 6, 21, 12]

# mapped = map(my_func, my_list)
# print(mapped)
# print(list(mapped))
# print(my_func(my_list[3]))


# age = {30, 25, 50, 35, 20, 18, 16}


# age_count = len(age)

# average_age = sum(age)/age_count

# print(max(age), min(age), (average_age), sum(age), age_count)


#student_age = lambda numbers: list(set(numbers.str)
# student_age = input ('Enter the ages of students:\n>')
# age = lambda student: student.split()
# numbers = age(student_age)
# lists = lambda age: int(age)
# mapped = list(map(lists, numbers)) 

# age_count = len(mapped)
# average = sum(mapped)/age_count


# print(max(mapped))

# print(min(mapped))

# print(average)

# print(sum(mapped))

# print(age_count)

# students = input('Enter ages of students:\n>')
# ages = list(map(lambda x:int(x), students.split()))
# print("The oldest person is {}years old".format(max(age)))
# print("The youngest person is {}years old".format(min(ages)))
# print("The sum of student's age is {} years old".format(sum(ages)))
# print("The average age is {} years old".format(sum(ages)/len(ages)))
# print("There are {} students in the class".format(len(ages)))

# my_list = lambda scores: list(scores)
# my_scores = {'75', '50', '45', '35', '77', '90'}
# total = list(map(my_list, my_scores))

# print(total)

# #without the lambda
# a_list = ["RED", "BLUE", "GREEN"]

# result = list(map(list, a_list))

# print(result)

#a = list(range(40, 50))

#even_numbers = filter(lambda x: x%2==0, a)
#even_numbers = filter(lambda x: x%2!=0, a)
#print(list(even_numbers))

# from math import pi


# lists = {"3", "4", "5", "girl", "boy", "aunty", "uncle"}

# print(list(filter(lambda x: x.isnumeric(), lists)))


#Q2
# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)

# values = input("Enter some numbers:\n").split(",")
# print(values) #This is the list
# print(tuple(values)) #This is the tuple

#Q2
#list = numbers.split(",")
#tuple = tuple(list)

#print('list:', list)
#print('tuple:', tuple)

#week 3 Assignment

# #QUESTION 1
# import math 
# radius = float(input("The radius of a cirle is:\n>"))
# r = radius
# area = (math.pi) * (r**2)

# print(area)

# # #QUESTION 2

# numbers = input('Enter a set of numbers:\n>')

# print(list(numbers))
# tuple = tuple(numbers)
# print(tuple)


# #QUESTION 3
# variable = input('Enter Users Firt name and Last name:\n>')
# print(variable)
# print(variable[::-1])

#QUESTION 4

# my_details = ['Gloria', 'Amos', 'brother', 'siter', 'car', 'house', '18', '19', '20']

# list = ','.join(my_details)

# print(list)
# print(my_details)

#In-Built-modules and foundationals 22/11/2021
#RANDOM

# import random

# dice = [1,2,3,4,5,6]

# random.shuffle(dice)

# print(dice)

#computer_choice = random.choice(dice)

#pop_sample = random.sample(dice, 3)


#print(pop_sample)

#TIME
# import random
# import time

# dice = [1,2,3,4,5,6]
# print('shuffling.....')
# time.sleep(3)
# random.shuffle(dice)

# print('shuffle complete. Computer selecting......Please wait')

# time.sleep(3)



# computer_choice = random.choice(dice)

# #pop_sample = random.sample(dice, 3)

# print(f'Computer Selected {computer_choice}')

#DATETIME
# import random
# import time
# from datetime import datetime

# date = datetime.now()
# print(date)
# print(date.day)
# print(date.month)
# print(date.year)
# print(date.weekday())
# print(date.isoweekday())

# string_format1 = datetime.strftime(date, '%A, %d of %B, %Y')

# string_format2 = datetime.strftime(date, '%d-%b-%y')

# string_format3 = datetime.strftime(date, '%d/%B/%Y')

# string_format4 = datetime.strftime(date, '%B-%Y')

# string_format5 = datetime.strftime(date, '%a. %d %b., %Y')
# print(string_format1)
# print(string_format2)
# print(string_format3)
# print(string_format4)
# print(string_format5)

#CONDITIONALS
#IF, ELSE, 
#user = int(input('Enter your age:\n>'))
#elif

# user = input('Enter your age:\n>')
# if user.isdigit():
#     user = int(user)
#     if user < 18:
#         print('Not Eligible to vote')
#     elif user <= 50:
#         print('Eligible to vote') 
#     else:
#         print('You are Overaged')
# else:
#     print('invalid input, try again')

# from typing import AsyncGenerator


# students_scores = int(input('Enter Your Grades here:\n>'))
# if students_scores >= 70:
#     print('A Passed')
# elif students_scores >= 60:
#     print('B Passed')
# elif students_scores >= 40:
#     print('C passed')
# else:
#     print('failed')

#Classwork
# import random
# import time

# list_of_unique_words = ["Fast", "Mingle", "Safe", "Univelcity", "Students", "Intelligent", "Nice", "Questions", "Assignments", "Reflection"]
# random.shuffle(list_of_unique_words)
# computer_choice = random.choice(list_of_unique_words)
# print('welcome To Guessing Game!!! If you want to read instructions, Press H')
# user = input().lower()
# if user == 'h':
#    print('The instruction of the game states that when a player guesses a word that was randomly picked by the the computer, the player wins, else the player looses.... ')
# else:
#     print('Invalid command')
# print("Please select from the list below")
# print(list_of_unique_words)
# users_guess = input('Guess a word:\n>')
# if users_guess == computer_choice:
#     print('WINS')
# elif users_guess != computer_choice:
#     print('LOOSE')
# elif users_guess != list_of_unique_words:
#     print('Sorry, word not on the list')
# else:
#     print('Game Over')
# print(f'Computer selected word is {computer_choice}')

#correction
# import random
# print("Welcome to this game")
# print("Enter H for help or any ")
# user_input = input('>').lower()

# help_ = """
# The instruction of the game states that when a player guesses a word that was randomly picked by the the computer, the player wins, else the player looses.... ')
# """
# if user_input == 'h':
#     print(help_)
# my_list = ["Fast", "Mingle", "Safe", "Univelcity", "Students", "Intelligent", "Nice", "Questions", "Assignments", "Reflection"]
# random.shuffle(my_list)
# print(my_list)

# user_choice = input("guess the word:\n>").title()
# computer = random.choice(my_list)

# if user_choice in my_list:
#     if user_choice == computer:
#         print("You Win")
#     else:
#         print(f'computer selected{computer}')
#         print('try again')
# else:
#     print('invalid input. Game over!!!')

#ASSIGNMENT
#A SIMPLE ATM
import random
import time
print('Welcom to City Bank')
time.sleep(1)
print(input('Do you have an accont with us, yes or no? :').lower())
time.sleep(1)
print('Please input your details')
time.sleep(1)

account_number = random.randrange(3000000000, 3999999999)

my_details = {}
user = {}
Fullname = input('\nEnter your fullname :\n> ')
password = input('\nPlease create a password :\n> ')
transaction_pin = input('\nCreate a transaction pin :\n> ')
account_balance = 0

print(f'\nYour current accout balance is {account_balance}')
time.sleep(2)

print('\nYour account have been successfully created')
time.sleep(2)


user['account_number'] = account_number
user['name'] = Fullname
user['password'] = password
user['pin'] = transaction_pin
user['balance'] = account_balance

#print(user)

print(f'\nYour account number is: {account_number}')
time.sleep(2)

print('\nDo you wish to perform any transaction on your account, Yes or No? ')

user_input = input('>').lower()
login_details = account_number
new_password = password
if user_input == 'yes':
    print('\nPlease enter your Account Number and Password to login')

    for i in range(1):
        login_details = print(input('\nEnter your Account Number : '))
        new_password =  print(input('\nEnter your Password : '))
        time.sleep(2)

        if account_number == login_details and password == new_password:
            print('Login Complete')

            for i in range(5):
                print("\nDo you wish to perfom any other transaction like: \nDeposit, Withdraw or Transfer funds, \nor do you wish to Edit your detail?")

                time.sleep(2)
                print("\nT0 Deposit money, Press D, \nTo withdraw, Press W, \nTo Transfer to another Costumer, Press T, \nTo Edit your Details, Press E")

                user_inputs = input('>').lower()

    #for i in range():
                if user_inputs == 'd':
                    deposit_money = int(input('Please deposit funds by inputting deposit amount here :\n>'))
                    deposit = deposit_money
                    account_balance = account_balance + deposit
                    print(f'Your account balance is {account_balance}')
                elif user_inputs == 'w':
                    withdraw_money = int(input('Input the amount you wish to withdraw : \n'))
                    withdrawal_amount = withdraw_money
                    if withdrawal_amount > account_balance :
                        print('insufficient funds.\r\nSorry, your transaction cannot be completed!')
                    else:
                        print(f'Transaction completed \r\nYou have successfully withdrawn the sum of {withdrawal_amount}')
                elif user_inputs == 't':
                    recipent_name = input('Enter the name of recipent :\n')
                    recipent_account_number = int(input('Account number of recipent :\n'))
                    transfer_amount = int(input('Transfer Amount :'))
                    if transfer_amount > account_balance:
                        print('insufficient funds.\r\nSorry, your transaction cannot be completed!')
                    else:
                        print(f'Transaction completed \r\nYou have successfully transfered the sum of {transfer_amount} to {recipent_name}')
                else:
                    edit_details = print('Welcome to First BANK, you can edit your details here!!')
                    Fullname = input('Please enter your fullname :\n> ')
                    password = input('Edit password :\n> ')
                    pin = input('Create new transaction pin :\n> ')
                    Submit = print('To submit your edits, press S :')
                    Submit_input = input('>').lower()
                    Submit_edits = """
                    You have successfully updated your details.
                    """
                    if Submit_input == 's':
                        print(Submit_edits)

                    user['account_number'] = account_number
                    user['name'] = Fullname
                    user['password'] = password
                    user['pin'] = pin
                    user['balance'] = account_balance
        
        else:
            print('Invalid input, Try again')
            time.sleep(1)
            login_details = print(input('\nPlease enter your Account Number : '))
            new_password =  print(input('\nPlease enter your Password : '))
            time.sleep(2)
    if login_details != account_number and password != new_password:
        print('\ninvalid user, please contact the customer care line on 09876784 for help!!!')


else:
    print('\nThank you, Goodbye')



#for loop 24/11/21

# number = int(input('enter your number \n>'))
# prime = True
# if number <= 1:
#     prime = False
# if number == 2:
#     prime = True

# for i in range(2, number):
#     if number%i == 0:
#         prime = False
#         break

# if prime:
#     print("Prime Number")
# else:
#     print("Not Prime")