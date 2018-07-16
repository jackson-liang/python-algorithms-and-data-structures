# Exercise 14 from
# https://interactivepython.org/runestone/static/pythonds/Introduction/ProgrammingExercises.html
import random

class Card:
    # The ranking of suits is taken from the Game of Poker
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, r, s):
        self.rank = r
        self.suit = s

    def __str__(self):
        return str(Card.ranks[self.rank]) + " of " + str(Card.suits[self.suit])

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        # Checking the suits first
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        # Checking the rank next
        else:
            return self.rank < other.rank


class Deck:
    def __init__(self):
        self.cards = []
        for rank in range(1, 14):
            for suit in range(4):
                card = Card(rank, suit)
                self.cards.append(card)

    def __str__(self):
        printedDeck = []
        for card in self.cards:
            printedDeck.append(str(card))
        return ', '.join(printedDeck)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        return self.cards.sort()

    def move_cards(self, hand, num):
    # This method will deal a number "num" of cards from the deck to the "hand", which is an input argument to the method.
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_hands, num_cards):
        hands = []
        for h in range(1, num_hands+1):
            new_hand = Hand(str(h))
            self.move_cards(new_hand, num_cards)
            hands.append(new_hand)
        return hands


class Hand(Deck):
    def __init__(self, name):
        self.cards = []
        self.name = name



myDeck = Deck()
print(myDeck.deal_hands(4,13)[0])
