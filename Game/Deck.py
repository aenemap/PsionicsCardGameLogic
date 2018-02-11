from random import shuffle

class Deck:

    def __init__(self, deck_id):
        self.deck_id = deck_id
        self.deck = []

    def addCardToDeck(self, card):
        self.deck.append(card)

    def shuffleDeck(self):
        shuffle(self.deck)
