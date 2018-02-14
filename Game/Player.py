from Game.Enums import *

class Player:

    def __init__(self, name, health, deck, energy_pool):
        self.name = name
        self.health = health
        self.deck = deck
        self.energy_pool = energy_pool
        self.hand = []
        self.playerArea = {
            'Shields':[],
            'Talents':[],
            'DiscardPile': []
        }



    def addToEnergyPool(self, amount):
        self.energy_pool += amount

    def substractFromEnergyPool(self, amount):
        self.energy_pool -= amount
        if self.energy_pool < 0:
            self.energy_pool = 0

    def playCard(self, card):
        if card.type == CardType.Shield:
            self.playerArea['Shields'].append(card)
        elif card.type == CardType.Talent:
            self.playerArea['Talents'].append(card)
