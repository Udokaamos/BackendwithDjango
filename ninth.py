import random

def play_game(trial,scores):

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
                print('Try again')

        else:
            print('Invalid input. Try again.')
        trial -=1
        print(f'\n{trial} trial(s) left\n')

        answer = input("Do you want to play again y/n\n>").lower()
        if answer == 'y':
            new_trial = 3
            new_scores = 0
            return play_game(new_trial, new_scores)  
        else:
            return scores

    