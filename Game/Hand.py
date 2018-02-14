from Game.Card import Card

class Hand(object):

    def __init__(self, hand_size, max_hand_size):
        self.hand_size = hand_size
        self.max_hand_size = max_hand_size
        self.hand = []

    def getHand(self):
        return self.hand

    def addCardToHand(self, card):
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
            card.printCard(card)
