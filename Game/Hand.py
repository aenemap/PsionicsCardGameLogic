from Game.Card import Card

class Hand:

    def __init__(self, hand_size, max_hand_size):
        self.hand_size = hand_size
        self.max_hand_size = max_hand_size
        self.hand = []

    def addCardToHand(self, card):
        self.hand.append(card)

    def gethandSize(self):
        return self.hand.length

    def printHand(self):
        for card in self.hand:
            Card.printCard(card)
