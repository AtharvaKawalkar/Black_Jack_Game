#BlackJack Game
import Blackjack_G_art
import random
import os

clear = lambda: os.system('cls')

def cards():
    cards_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand_card = random.choice(cards_value)
    return rand_card

def print_msg(user_cards, computer_cards):
    print(f"Your final hand {user_cards}, Current Score {sum(user_cards)}")
    print(f"Computer's final hand {computer_cards}, Current Score {sum(computer_cards)}")

def final_result(diff_user, diff_computer, user_cards, computer_cards):
    if sum(user_cards)>21:
        print_msg(user_cards, computer_cards)
        print("You went over. You Lose")
    elif diff_user<0:
        print_msg(user_cards, computer_cards)
        print("You went over. You Lose")
    elif diff_computer<0:
        print_msg(user_cards, computer_cards)
        print("Computer went over. You Win")
    elif diff_computer>diff_user:
        print_msg(user_cards, computer_cards)
        print("You Win")
    elif diff_user>diff_computer:
        print_msg(user_cards, computer_cards)
        print("You Lose")
    else:
        print_msg(user_cards, computer_cards)
        print("It's a Draw")

def Blackjack():
    user_cards = []
    computer_cards = []
    for _ in range(0,2):
        user_cards.append(cards())
        computer_cards.append(cards())
    print(f"You cards : {user_cards}, Current Score {sum(user_cards)}")
    print(f"Computer's first card : {computer_cards[0]}")
    if sum(computer_cards) == 21:
        print_msg(user_cards, computer_cards)
        print("You Lose. Computer has a BlackJack")
    elif sum(user_cards) == 21:
        print_msg(user_cards, computer_cards)
        print("You Win. You have a BlackJack")
    else:
        play = True
        flag = False
        while(play==True and flag==False):
            player_choice = input("Hit or Hold : ").lower()
            if player_choice == 'hit':
                user_cards.append(cards())
                if user_cards[-1]==11:
                    if sum(user_cards)>21:
                        user_cards[-1] = 1
                print(f"You cards : {user_cards}, Current Score {sum(user_cards)}")
                print(f"Computer's first card : {computer_cards[0]}")
                if(sum(user_cards)>=21):
                    flag=True
            else:
                play = False

        if(flag==False):
            while(sum(computer_cards)<16):
                computer_cards.append(cards())
                if sum(computer_cards)>21:
                    if computer_cards[-1]==11:
                        computer_cards[-1] = 1
                
        diff_user = 21 - sum(user_cards)
        diff_computer = 21 - sum(computer_cards)

        final_result(diff_user, diff_computer, user_cards, computer_cards)

print(Blackjack_G_art.logo)
print("Welcome to BlackJack Game")
start = True
while(start == True):
    choice = input("Do you want to play a game of Blackjack again : Type 'y' or 'n' : ")
    if(choice=='y'):
        clear()
        Blackjack()
    else:
        start = False