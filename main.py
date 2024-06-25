import random

cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal(num_of_cards = 1):
    dealt_cards = []
    for i in range(num_of_cards): 
        dealt_cards.append(cards.pop())

    return dealt_cards

shuffle()
