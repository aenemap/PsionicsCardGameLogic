from Game.Enums import *

class Player:

    def __init__(self, name, health, deck):
        self.name = name
        self.health = health
        self.deck = deck
        self.hand = []
        self.playerArea = {
            'Shields':[],
            'Talents':[],
            'DiscardPile': []
        }

    def playCard(self, card):
        if card.type == CardType.Shield:
            self.playerArea['Shields'].append(card)
        elif card.type == CardType.Talent:
            self.playerArea['Talents'].append(card)
