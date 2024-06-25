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
        self.value = 0
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

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:        
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number.")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(True)

            for i in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}.")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["s", "stand", "h", "hit"]:
                    choice = input("Please choose 'Hit' or 'Stand' (or H/S) ").lower()
                    print()

                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal())
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(True)

            if self.check_winner(player_hand, dealer_hand):
                continue
            
            print("Final Results")
            print("Your hand", player_hand_value)
            print("Dealer's hand", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over = False):
        player_hand.display()
        if not game_over:
            if player_hand.get_value() > 21:
                print("You lost. Dealer wins!")
                return True
            elif dealer_hand.get_value() > 21:
                print("You win!")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both you and the dealer have blackjack. It's a tie!")
                return True
            elif player_hand.is_blackjack():
                print("You have a blackjack. You win!")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has a blackjack. Dealer wins!")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a tie!")
            else:
                print("Dealer wins!")
            return True
        return False        

game = Game()
game.play()