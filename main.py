import random

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, num_of_cards = 1):
        dealt_cards = []
        for i in range(num_of_cards): 
            if len(self.cards) > 0:
                dealt_cards.append(self.cards.pop())

        return dealt_cards

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Hand:
    def __init__(self, is_dealer = False):
        self.cards = []
        self.value = 0
        self.is_dealer = is_dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        for card in self.cards:
            if card.rank["rank"] == "A" and self.value > 10:
                self.value += 1
            else:
                self.value += card.rank["value"]

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards = False):
        print(f'''{"Dealer's" if self.is_dealer else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.is_dealer \
            and not show_all_dealer_cards \
            and not self.is_blackjack():
                print("hidden")
            else:
                print(card)

        if not self.is_dealer:
            print("Value", self.get_value())
        print()

