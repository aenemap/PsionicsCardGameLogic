from random import shuffle
from collections import deque

class Deck:

    def __init__(self, deck_id, deck_name):
        self.deck_id = deck_id
        self.deck_name = deck_name
        self.deck = deque([])

    def addCardToDeck(self, card):
        self.deck.append(card)

    def shuffleDeck(self):
        shuffle(self.deck)

    def drawCardFromTopOfDeck(self):
        card = self.deck.popleft()
        return card

    def drawCardFromBottomOfDeck(self):
        card = self.deck.pop()
        return card


    def printDeck(self):
        for card in self.deck:
            print('{0},{1}'.format(card.id, card.name))
