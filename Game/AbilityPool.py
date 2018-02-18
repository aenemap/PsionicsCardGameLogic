from Game.Ability import Ability
from Game.Enums import *

class GainHealthAtStartOfRound(Ability):

    def __init__(self, attachedCard, amount):
        Ability.__init__(self, 'GainHealthAtStartOfRound', 1, AbilityEffectType.StartOfTurn, AbilityArgType.CardOwner)
        self.attachedCard = attachedCard
        self.amount = amount

    def invoke(self, player):
        if player:
            playerArea = None
            if self.attachedCard.type == CardType.Shield:
                playerArea = player.playerArea[PlayerArea.Shields.value]
            elif self.attachedCard.type == CardType.Talent:
                playerArea = player.playerArea[PlayerArea.Talents.value]
            # print('Player Area => ', playerArea)
            if playerArea:
                # print('Card uniqueCardId => ', self.attachedCard.uniqueCardId)
                playerHasCard = len(list(filter(lambda x: x.uniqueCardId == self.attachedCard.uniqueCardId, playerArea)))
                if playerHasCard > 0:
                    player.health += self.amount

class GainEnergyAtStartOfRound(Ability):

    def __init__(self, attachedCard, amount):
        Ability.__init__(self, 'GainEnergyAtStartOfRound', 2, AbilityEffectType.StartOfTurn, AbilityArgType.CardOwner)
        self.attachedCard = attachedCard
        self.amount = amount

    def invoke(self, player):
        if player:
            playerArea = None
            if self.attachedCard.type == CardType.Shield:
                playerArea = player.playerArea[PlayerArea.Shields.value]
            elif self.attachedCard.type == CardType.Talent:
                playerArea = player.playerArea[PlayerArea.Talents.value]
            # print('Player Area => ', playerArea)
            if playerArea:
                # print('Card uniqueCardId => ', self.attachedCard.uniqueCardId)
                playerHasCard = len(list(filter(lambda x: x.uniqueCardId == self.attachedCard.uniqueCardId, playerArea)))
                if playerHasCard > 0:
                    player.energy_pool += self.amount
