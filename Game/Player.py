from Game.Enums import *

class Player(object):

    def __init__(self, name, health, deck, energy_pool):
        self.name = name
        self.health = health
        self.deck = deck
        self.energy_pool = energy_pool
        self.hand = []
        self.playerArea = {
            PlayerArea.Shields.value:[],
            PlayerArea.Talents.value:[],
            PlayerArea.DiscardPile.value: []
        }

    def addToEnergyPool(self, amount):
        self.energy_pool += amount

    def substractFromEnergyPool(self, amount):
        self.energy_pool -= amount
        if self.energy_pool <= 0:
            self.energy_pool = 0

    def takeDamage(amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0

    def heal(amount):
        self.health += amount

    def getCardFromPlayerArea(self, cardid, area):
        card = None
        for p_area in PlayerArea:
            if p_area == area:
                card = None
                try:
                    card = list(filter(lambda x: x.id == int(cardid), self.playerArea[p_area.value]))[0]
                    break
                except:
                    break
        return card




    def playCard(self, card):
        if card.type == CardType.Shield:
            self.playerArea['Shields'].append(card)
        elif card.type == CardType.Talent:
            self.playerArea['Talents'].append(card)
