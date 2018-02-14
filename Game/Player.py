from Game.Enums import *

class Player:

    def __init__(self, name, health, deck, energy):
        self.name = name
        self.health = health
        self.deck = deck
        self.energy = energy
        self.hand = []
        self.playerArea = {
            'Shields':[],
            'Talents':[],
            'DiscardPile': []
        }

    def addEnergy(self, amount):
        self.energy += amount

    def substractEnergy(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def playCard(self, card):
        if card.type == CardType.Shield:
            self.playerArea['Shields'].append(card)
        elif card.type == CardType.Talent:
            self.playerArea['Talents'].append(card)
