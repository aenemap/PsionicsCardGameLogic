from Game.Ability import Ability
from Game.Enums import *
import math

class GainHealthAtStartOfRound(Ability):

    def __init__(self, attachedCard, amount):
        description = 'Gain {0} health at the start of your turn'.format(amount)
        Ability.__init__(self, 'GainHealthAtStartOfRound',description, 1, AbilityEffectType.StartOfTurn, AbilityArgType.CardOwner, attachedCard)
        self.amount = amount

    def invoke(self, player):
        if player:
            print(self.attachedCard)
            playerArea = player.getPlayerArea(self.attachedCard)
            # print('Player Area => ', playerArea)
            if playerArea:
                # print('Card uniqueCardId => ', self.attachedCard.uniqueCardId)
                playerHasCard = len(list(filter(lambda x: x.uniqueCardId == self.attachedCard.uniqueCardId, playerArea)))
                if playerHasCard > 0:
                    if not self.attachedCard.isFaceDown:
                        player.health += self.amount

class GainEnergyAtStartOfRound(Ability):

    def __init__(self, attachedCard, amount):
        description = 'Gain {0} energy at the start of your turn'.format(amount)
        Ability.__init__(self, 'GainEnergyAtStartOfRound', description, 2, AbilityEffectType.StartOfTurn, AbilityArgType.CardOwner, attachedCard)
        self.amount = amount

    def invoke(self, player):
        if player:
            playerArea = player.getPlayerArea(self.attachedCard)
            # print('Player Area => ', playerArea)
            if playerArea:
                # print('Card uniqueCardId => ', self.attachedCard.uniqueCardId)
                playerHasCard = len(list(filter(lambda x: x.uniqueCardId == self.attachedCard.uniqueCardId, playerArea)))
                if playerHasCard > 0:
                    if not self.attachedCard.isFaceDown:
                        player.energy_pool += self.amount

class DrawCardOnPlay(Ability):

    def __init__(self, attachedCard, howManyCards):
        description = 'When this enters play draw {0} card{1} from the top of your deck'.format(howManyCards, 's' if howManyCards > 1 else '')
        Ability.__init__(self, 'DrawCardOnPlay', description, 1, AbilityEffectType.Immediate, AbilityArgType.CurrentPlayer, attachedCard)
        self.howManyCards = howManyCards

    def invoke(self, player):
        if player:
            for c in range(0, self.howManyCards):
                player.hand.addCardToHand(player.deck.drawCardFromDeck(DrawCard.DrawFromTopOfDeck))

class NightBaneAbility(Ability):

    def __init__(self, attachedCard):
        description = 'When this shield is loaded gains consistency equals to the energy spend (max 5)'
        abilityArgs = [AbilityArgType.Card, AbilityArgType.OpposingPlayer]
        Ability.__init__(self, 'NightBaneAbility', description, 1, AbilityEffectType.AfterLoadShield, abilityArgs, attachedCard)

    def invoke(self, card, player):
        if card:
            energy_amount = int(input('How much energy you want to spent to load the shield?'))
            while energy_amount > 5:
                energy_amount = int(input('How much energy you want to spent to load the shield?'))
            if energy_amount:
                player.removeFromEnergyPool(energy_amount)
                card.energy_cost = energy_amount
                card.consistency_value = energy_amount

class IvoryAbility(Ability):

    def __init__(self, attachedCard):
        description = 'You may reflect half the energy to a minimum of 1 directly to your opponent'
        abilityArgs = [AbilityArgType.CurrentPlayer, AbilityArgType.AttackValue]
        Ability.__init__(self, 'IvoryAbility', description, 1, AbilityEffectType.WhenAttacked, abilityArgs, attachedCard)

    def invoke(self, player, attack_value):
        if player:
            damage_amount = math.floor(attack_value / 2)
            if damage_amount <= 0:
                damage_amount = 1
            print('Damage Reflected from Ivory: ', damage_amount)
            player.health -= damage_amount
