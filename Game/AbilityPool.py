from Game.Ability import Ability
from Game.Enums import *

class GainHealthAtStartOfRound(Ability):

    def __init__(self):
        Ability.__init__(self, 'GainHealthAtStartOfRound', 1, AbilityEffectType.StartOfTurn, AbilityArgType.CardOwner)

    def invoke(self, player):
        if player:
            playerArea = None
            if self.abilityIsAttachedToCard.type == CardType.Shield:
                playerArea = player.playerArea[PlayerArea.Shields.value]
            elif self.abilityIsAttachedToCard.type == CardType.Talent:
                playerArea = player.playerArea[PlayerArea.Talents.value]
            # print('Player Area => ', playerArea)
            if playerArea:
                # print('Card uniqueCardId => ', self.abilityIsAttachedToCard.uniqueCardId)
                playerHasCard = len(list(filter(lambda x: x.uniqueCardId == self.abilityIsAttachedToCard.uniqueCardId, playerArea)))
                if playerHasCard > 0:
                    player.health += 1
