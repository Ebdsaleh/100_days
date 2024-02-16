# main.py
# Day 11 Capstone Project - Blackjack
"""
############### Blackjack Project ######################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

"""
import random
import os
import sys
import art
logo = art.logo
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []
hands_played = False


def clear_screen():
    OS = sys.platform
    if OS.startswith('linux') or OS == 'darwin':
        os.system('clear')
    else:
        os.system('cls')


def update_screen():
    clear_screen()
    print(logo)
    print("Dealer's hand:")
    show_dealer_hand()
    print("Player's hand:")
    show_hand(player_hand)


def deal(num: int, recipient: str):
    """
    Deals the number of cards to the player and dealer.
    """
    for x in range(num):
        chosen_card = random.choice(deck)
        if recipient == 'player':
            if chosen_card == 11:
                if check_hand_value(player_hand) + chosen_card > 21:
                    chosen_card = 1
            player_hand.append(chosen_card)
        elif recipient == 'dealer':
            if chosen_card == 11:
                if check_hand_value(dealer_hand) + chosen_card > 21:
                    chosen_card = 1
            dealer_hand.append(chosen_card)
        else:
            return
    print(f"Dealer deals {num} cards to the {recipient}.")


def show_hand(hand):
    if not hands_played:
        print(f"{hand}, current score: {check_hand_value(hand)}")


def show_dealer_hand():
    if len(dealer_hand) < 3 and not hands_played:
        print(f"{dealer_hand[0]}")
    else:
        print(f"{dealer_hand}")


def hit():
    deal(1, 'player')


def check_hand_value(hand: list):
    hand_value = sum(hand)
    return hand_value


def check_for_blackjack():
    if len(player_hand) == 2:
        if check_hand_value(player_hand) == 21:
            return True
    else:
        return False


def calculate_score():
    global hands_played
    player_score = check_hand_value(player_hand)
    dealer_score = check_hand_value(dealer_hand)
    player_wins = False
    is_draw = False
    hands_played = True
    clear_screen()
    print(logo)
    print(f"Dealer's final hand: {dealer_hand}, final score: " +
          f"{dealer_score}")
    print(f"Player's final hand: {player_hand}, final score: " +
          f"{player_score}")
    if player_score > 21 or dealer_score == 21:
        player_wins = False
    elif dealer_score > 21 or player_score == 21:
        player_wins = True
    if player_score < 21 and dealer_score < 21:
        if dealer_score > player_score:
            player_wins = False
        elif player_score > dealer_score:
            player_wins = True
        else:
            is_draw = True
    if is_draw:
        print("It's a Draw!")
    else:
        if player_wins:
            print("You Win!")
        else:
            print("You Lose!")
    input("Press 'Enter' to continue.")


def play_another_card():
    while True:
        update_screen()
        another_card = input("Do you want another card? 'y' or 'n': ")
        if another_card[0] == 'y':
            hit()
            if check_hand_value(player_hand) >= 21:
                break
        elif another_card[0] == 'n':
            break


def game():
    global player_hand
    global dealer_hand
    global hands_played
    hands_played = False
    clear_screen()
    print(logo)
    player_hand = []
    dealer_hand = []
    deal(2, 'player')
    deal(2, 'dealer')
    print("Player's hand:")
    show_hand(player_hand)
    print("Dealer's hand:")
    show_dealer_hand()
    if not check_for_blackjack():
        play_another_card()
        while check_hand_value(dealer_hand) < 17:
            deal(1, 'dealer')
    calculate_score()


def start_new_game():
    valid_input = False
    clear_screen()
    print(logo)
    while not valid_input:
        play_game = input(
                "Do you want to play Blackjack? 'y' or 'n': ").lower()
        if play_game[0] == 'y':
            valid_input = True
            return True
        elif play_game[0] == 'n':
            valid_input = True
            return False
        else:
            print("Invalid input")


def main():
    end_game = False
    while not end_game:
        if start_new_game():
            game()
        else:
            end_game = True
    print("Goodbye!")
    exit()


if __name__ == '__main__':
    main()
