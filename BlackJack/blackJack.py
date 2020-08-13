import random
import blackJack_helper
from blackJack_helper import Bank
from blackJack_helper import Player
from blackJack_helper import Computer
suit=['Spades','Diamond','Hearts','clubs']
rank=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
cards_used=[]

# RANDOM CARD
def random_card():            
    card=[random.choice(rank),random.choice(suit)]
    while card in cards_used:
        card=[random.choice(rank),random.choice(suit)]
    cards_used.append(card)
    return card


# COMPUTER START
computer_hand=[]
def computer_hand_start():
    computer_hand.append(random_card())
    computer_hand.append(random_card())
    print("~~~~Computer cards~~~~~:")
    for e in computer_hand:
        print(e[0],'of',e[1])
        break
    print('hidden')

# PLAYER START
player_hand=[]
def player_hand_start():
    player_hand.append(random_card())
    player_hand.append(random_card())
    print("**** Player cards ****:")
    for e in player_hand:
        print(e[0],'of',e[1])
# COMPUTER DISPLAY
def computer_hand_display():
    print("~~~~Computer Cards~~~~~:")
    for e in computer_hand:
        print(e[0],'of',e[1])

# PLAYER DISPLAY
def player_hand_display():
    print('**** Player Cards ****:')
    for e in player_hand:
        print(e[0],'of',e[1])
# PLAYER SCORE
player_score=0
def player_value ():
    global player_score
    player_score=0
    for i in player_hand:
        try:
            player_score+=i[0]
        except:
            if i[0]=="King" or i[0]=="Queen" or i[0]=="Jack":
                player_score+=10
            else:
                continue
    for i in player_hand:
        if i[0]=='Ace':
            if 11+player_score>21:
                player_score+=1
            else:
                player_score+=11 

# COMPUTER SCORE
computer_score=0
def computer_value ():
    global computer_score
    computer_score=0
    for i in computer_hand:
        try:
            computer_score+=i[0]
        except:
            if i[0]=="King" or i[0]=="Queen" or i[0]=="Jack":
                computer_score+=10
            else:
                pass
    for i in computer_hand:
        if i[0]=='Ace':
            if 11+computer_score>21:
                computer_score+=1
            else:
                computer_score+=11

# PLAYER CHOICE
def player_choice():
    while True:
        player_input=((input('Hit or Stop: ')).lower())
        if player_input=='hit':
            player_hand.append(random_card())
            break
        if player_input=='stop':
            return 'stop'
# COMPUTER CHOICE
def computer_choice():
    computer_hand.append(random_card())
# PLAYER WIN CON
def player_win_con():
    if player_score==21:
        print("Player WINS!, Player Bank {}".format(Bank.total_amount))
        print("Player Score: {} | Computer score: {}".format(player_score, computer_score))
        Bank.total_amount==Player.player_total_amount
        return True
    if player_score>21:
        print("BUST, Player LOSSES!\nThe Computer wins, Computer Bank: {}".format(Bank.total_amount))
        print("Player Score: {} | Computer score: {}".format(player_score, computer_score))
        Bank.total_amount==Computer.computer_total_amount
        return True
# GAME CLEAR
def game_clear():
    global player_hand
    global computer_hand
    global player_score
    global computer_score
    player_score=0
    computer_score=0
    computer_hand=[]
    player_hand=[]
#  COMPUTER WIN CONDITION
def computer_win_con():
    if computer_score>player_score and computer_score<=21:
        print('Computer WINS!, Computer Bank:{}'.format(Bank.total_amount))
        print("Player Score: {} | Computer score: {}".format(player_score, computer_score))
        Bank.total_amount==Computer.computer_total_amount
        return True
    else:
        print("Player WINS!, Player Bank {}".format(Bank.total_amount))
        print("Player Score: {} | Computer score: {}".format(player_score, computer_score))
        Bank.total_amount==Player.player_total_amount
        return True

# THE GAME

game='ON'
while game=='ON':

    computer_hand_start()
    player_hand_start()
    player_value()

    print('Player total score is {}'.format(player_score))
    while player_score<21:
        if player_choice()=='stop':
            break
        player_hand_display()
        player_value()
        print('Player total score is {}'.format(player_score))
    if player_win_con()==True:
            break

    while computer_score<=player_score and computer_score<21:
        computer_value()
        computer_choice()
        computer_value()
        computer_hand_display()
        print("Computer total score is: {}".format(computer_score))
    if computer_win_con()==True:
        game="OFF"
        game_clear()
        break

