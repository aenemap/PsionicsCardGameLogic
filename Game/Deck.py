from random import shuffle
from collections import deque
from Game.Card import Card
from Game.Enums import DrawCard
import uuid, random
import logging

logger = logging.getLogger(__name__)

class Deck(object):

    def __init__(self, deck_id, deck_name):
        self.deck_id = deck_id
        self.deck_name = deck_name
        self.deck_size = None
        self.deck = deque([])

    def addCardToDeck(self, card):
        card.id = random.randint(1, 1000)
        card.uniqueCardId = uuid.uuid4()
        self.deck.append(card)

    def shuffleDeck(self):
        shuffle(self.deck)

    def drawCardFromDeck(self, from_where):
        if len(self.deck) > 0:
            card = None
            if from_where == DrawCard.DrawFromTopOfDeck:
                card = self.deck.popleft()
            elif from_where == DrawCard.DrawFromBottomOfDeck:
                card = self.deck.pop()
            return card
        else:
            print('Deck is empty')

    # def drawCardFromTopOfDeck(self):
    #     if len(self.deck) > 0:
    #         card = self.deck.popleft()
    #         return card
    #     else:
    #         print('Deck is empty')
    #
    # def drawCardFromBottomOfDeck(self):
    #
    #     card = self.deck.pop()
    #     return card


    def printDeck(self):
        for card in self.deck:
            if card.isFaceDown:
                card.isFaceDown = False
                card.printCard(card)
                card.isFaceDown = True
            else:
                card.printCard(card)
