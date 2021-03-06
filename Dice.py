from random import randint
import time

def sixe_side_dice(sides = 6):
          return randint(1,sides)


def name():
    game_on = True
    while game_on == True:

        print("how many dices to u want to roll")
        num_roll = input(':')
        print(num_roll)
        print('exit{y/n}')
        answer = input()
        if answer  ==  'no':
            b = True
        elif answer == 'y' :
            print("system in closing THANK YOU")
            time.sleep(10)
            b = False
