from array import *
from operator import add, sub,mul
from Dice import sixe_side_dice
import time

Goal = 100
player1= 0
player2 = 0
round = 1
score,score2 = 0,0

def pigout():
    global score,player1,player2,score2

    if round % 2 !=0:
        score = 1
        score = score + player1
        player1= score
        #print('test1',score)

    elif round % 2 ==0:
        score2 =1
        score2 = player2 + score2
        player2 = score2
    return player1,player2
def freebacon():
    
    global player1,player2,round,score,score2
    list=[]
    if round % 2 !=0:
        vals =mul(player1,mul(player1,player1))
    elif round %2 == 0:
        vals =mul(player2,mul(player1,player2))

    while vals > 0:
        total = vals % 10
        list.append(int(total))
        vals = vals // 10
    list.reverse()
    output = 1 + abs(sum(list[::2]) - sum(list[1::2]))
    #print(output)
    if round % 2 !=0:
        score = player1 + output
        player1 = score
    else:
        score2= player2 + output
        player2 = score2
    return player1,player2

def num_roll(rolls):
    
    global player1,player2,score2,score
    if rolls == 0:
        freebacon()

    while rolls > 0:
        temp = sixe_side_dice()
        print (temp)
        if temp == 1:
             pigout()
             break

        if round % 2 !=0:
            score=temp+score

        elif round % 2 == 0:
            score2 = temp + score2
        rolls -=1
    player1 = score
    player2 = score2
    #print('test',score,score2)
    return scores()

def swine_swap():
    global player1,player2,score,score2
    value = pow(3,add(score,score2))
    first_digit = int(str(value)[:1])
    last_digit = value % 10
    if last_digit == first_digit:
        temp = score
        score = score2
        score2 = temp
        player1 = score
        player2 = score2
        print('found new score is :\n',player1,player2)

def scores():
    global playe1,player2

    if player1 >= 100:
        print('player1 Win')
        time.sleep(10)
        exit()
    elif player2 >= 100:
        print('plauer2 WIN!')
        time.sleep(10)
        exit()
    if player1 > player2:
        print("player1 toke the lead")
    elif player2 > player1:
        print('player2 took the lead')
    else:
        print("curently its a tie") 
    Overal_Point = print(player1,player2)
    return Overal_Point

def start():
    global round
    gameon = True
    while gameon == True:
        print('how many dice do u wanna to roll')
        dice_input = int(input('user want to roll:'))
        num_roll(dice_input)
        print('checking for swine_swap')
        swine_swap()
        print(' round completed next')
        round += 1


start()
