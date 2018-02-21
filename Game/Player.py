from Game.Enums import *

class Player(object):

    def __init__(self, name, health, energy_pool):
        self.name = name
        self.health = health
        self.decks = {}
        self.deck = None
        self.energy_pool = energy_pool
        self.actionsPerTurn = 4
        self.hand = []
        self.playerArea = {
            PlayerArea.Shields.value:[],
            PlayerArea.Talents.value:[],
            PlayerArea.DiscardPile.value: []
        }

    def addDeckToPlayer(self, deck):
        self.decks[deck.deck_id] = deck

    def selectDeck(self, deck):
        self.deck = self.decks[deck.deck_id]

    def addToEnergyPool(self, amount):
        self.energy_pool += amount

    def removeFromEnergyPool(self, amount):
        self.energy_pool -= amount
        if self.energy_pool <= 0:
            self.energy_pool = 0

    def takeDamage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0

    def heal(self, amount):
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

    def getPlayerArea(self, card):
        if card.type == CardType.Shield:
            return self.playerArea[PlayerArea.Shields.value]
        elif card.type == CardType.Talent:
            return self.playerArea[PlayerArea.Talents.value]

    def removeCardFromPlayerArea(self, cardid, area):
        card = None
        card = self.getCardFromPlayerArea(cardid, area)
        if card:
            cardIndex = self.playerArea[p_area.value].index(card)
            if cardIndex > -1:
                card = self.playerArea[p_area.value].pop(cardIndex)
                self.playerArea[PlayerArea.DiscardPile].append(card)




    def playCard(self, card):
        if card.type == CardType.Shield:
            self.playerArea[PlayerArea.Shields.value].append(card)
        elif card.type == CardType.Talent:
            self.playerArea[PlayerArea.Talents.value].append(card)
        elif card.type == CardType.Event:
            self.playerArea[PlayerArea.DiscardPile.value].append(card)
