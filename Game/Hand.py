from Game.Card import Card
import logging

logger = logging.getLogger(__name__)

class Hand(object):

    def __init__(self, hand_size, max_hand_size):
        self.hand_size = hand_size
        self.max_hand_size = max_hand_size
        self.hand = []

    def logHand(self):
        logger.info('Hand Size:{0}'.format(self.hand_size))
        logger.info('HHHHHHHHHHHHHHHHHHHHHHHH Cards in Hand HHHHHHHHHHHHHHHHHHHHHHHH')
        for card in self.hand:
            card.logCard(card)
        logger.info('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')

    def getHand(self):
        return self.hand

    def addCardToHand(self, card):
        if card:
            self.hand.append(card)

    def gethandSize(self):
        return self.hand.length

    def getCardFromHand(self, cardid):
        card = None
        try:
            card = list(filter(lambda x: x.id == int(cardid), self.hand))[0]
        except:
            pass

        if card:
            cardIndex = self.hand.index(card)
            if cardIndex > -1:
                card = self.hand.pop(cardIndex)
        return card

    def printHand(self):
        for card in self.hand:
            if card.isFaceDown:
                card.isFaceDown = False
                card.printCard(card)
                card.isFaceDown = True
            else:
                card.printCard(card)
