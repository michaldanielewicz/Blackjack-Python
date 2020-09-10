'''
The Blackjack game.
A human player versus computer player which is also a dealer.
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit} of {self.rank}'

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
        print("Deck created.")

    def __str__(self):
        return ', '.join(str(card) for card in self.deck)

    def reset(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card_dealed = self.deck.pop()
        return card_dealed

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace_count = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.ace_count += 1

    def adjust_for_ace(self):
        if self.ace_count > 0 and self.value > 21:
            self.value -= 10
            self.ace_count -= 1

    def reset(self):
        self.cards = []
        self.value = 0
        self.ace_count = 0

    def show_one_card(self):
        print(f'Card in the dealer hand: {self.cards[0]}. Total value: {values[self.cards[0].rank]}.')


    def check_over_21(self):
        if self.value > 21:
            return True
            print("Over 21")
        else:
            return False

    def __str__(self):
        return f"Cards in hand: {[', '.join(str(card) for card in self.cards)]}. Total value: {self.value}."

class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        print("You won this bet!")

    def lose_bet(self):
        self.total -= self.bet
        print("You lose this bet.")

    def draw_bet(self):
        print("It's a draw.")

    def __str__(self):
        return f"You have {self.total} chips"

class Player():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Your name is: {self.name}"

def get_name():
    return input("Please enter your name: ")

def check_bet(player_bet,total_player_cash):
    return player_bet <= total_player_cash

def take_bet(total_player_cash):
    while True:
        try:
            player_bet = int(input(f"------------------------------------------------\nYour total cash is: {total_player_cash}. Please take your bet: "))
        except:
            print("Incorrect value! Please enter a number.")
            continue
        else:
            if check_bet(player_bet,total_player_cash):
                print("Bet taken. Thank you.")
                break
            else:
                print("You have not enough cash. Enter smaller amount.")
                continue
    return player_bet

def replay():
    answer = input("Do you want to play next turn? Y/N: ")
    if answer.upper() == "Y":
        return True
    else:
        return False

def hit_or_stand():
    while True:
        player_answer = input("Do you want to hit or stand? H/S: ")
        if player_answer.upper() == "H" or player_answer.upper() == "S":
            break
        else:
            print("Enter H for hit or S for stand.")
            continue
    return player_answer.upper() == "H"

def check_win(player_hand,dealer_hand):
    result = ''
    if player_hand > 21:
        result = 'Player lose.'
    elif dealer_hand > 21:
        result = 'Player win.'
    else:
        if player_hand > dealer_hand:
            result = 'Player win.'
        elif player_hand < dealer_hand:
            result = 'Player lose.'
        else:
            result = 'Draw'
    return result

def check_gameover(player_chips):
    if player_chips <= 0:
        print("You have no cash left! You lose!")
        return True
    else:
        return False

while True:
    #start the game
    print("Welcome to the game of Blackjack!")
    game_deck = Deck()
    human_player = Player(get_name())
    player_chips = Chips()
    player_hand = Hand()
    dealer_hand = Hand()

    while True:
        #start the turn
        player_chips.bet = take_bet(player_chips.total)
        game_deck.reset()
        game_deck.shuffle()

        player_hand.reset()
        dealer_hand.reset()

        player_hand.add_card(game_deck.deal())
        player_hand.add_card(game_deck.deal())
        dealer_hand.add_card(game_deck.deal())
        dealer_hand.add_card(game_deck.deal())

        print(player_hand)
        dealer_hand.show_one_card()

        while hit_or_stand():
            player_hand.add_card(game_deck.deal())
            print(player_hand)

            player_hand.adjust_for_ace()

            if player_hand.check_over_21():
                break
            else:
                continue

        if dealer_hand.value < 17 and not player_hand.check_over_21():
            print("\nNow goes dealer.")
            while dealer_hand.value < 17:
                #dealer turn

                dealer_hand.add_card(game_deck.deal())
                print(dealer_hand)

                dealer_hand.adjust_for_ace()

                if dealer_hand.check_over_21():
                    break
                else:
                    continue

        print(f'Final hand of dealer: {dealer_hand}')

        if check_win(player_hand.value,dealer_hand.value) == "Player win.":
            player_chips.win_bet()
        elif check_win(player_hand.value,dealer_hand.value) == "Player lose.":
            player_chips.lose_bet()
        else:
            player_chips.draw_bet()

        if check_gameover(player_chips.total):
            break
        else:
            continue

        if replay():
            continue
        else:
            break

















    

