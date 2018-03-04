from Game.Ability import Ability
from Game.Enums import *
from Game.Actions import *
from Game.ActionResolver import *
import math
import logging

logger = logging.getLogger(__name__)

class GainHealthAtStartOfTurn(Ability):

    def __init__(self, attachedCard, amount):
        description = 'Gain {0} health at the start of your turn'.format(amount)
        Ability.__init__(self, 'GainHealthAtStartOfTurn',description, 1, AbilityEffectTime.StartOfTurn, AbilityEffectType.Reccuring, AbilityArgType.CardOwner, attachedCard)
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
                        player.health += self.amount

class GainHealthAtEndOfTurn(Ability):

    def __init__(self, attachedCard, amount):
        description = 'Gain {0} health at the end of your turn'.format(amount)
        Ability.__init__(self, 'GainHealthAtEndOfTurn',description, 1, AbilityEffectTime.EndOfTurn, AbilityEffectType.Reccuring, AbilityArgType.CardOwner, attachedCard)
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
        Ability.__init__(self, 'GainEnergyAtStartOfRound', description, 2, AbilityEffectTime.StartOfTurn, AbilityEffectType.Reccuring, AbilityArgType.CardOwner, attachedCard)
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
        Ability.__init__(self, 'DrawCardOnPlay', description, 1, AbilityEffectTime.OnPlay, AbilityEffectType.Immediate, AbilityArgType.CurrentPlayer, attachedCard)
        self.howManyCards = howManyCards

    def invoke(self, player):
        if player:
            for c in range(0, self.howManyCards):
                player.hand.addCardToHand(player.deck.drawCardFromDeck(DrawCard.DrawFromTopOfDeck))

class NightBaneAbility(Ability):

    def __init__(self, attachedCard):
        description = 'When this shield is loaded gains consistency equals to the energy spend (max 5)'
        abilityArgs = [AbilityArgType.Card, AbilityArgType.OpposingPlayer]
        Ability.__init__(self, 'NightBaneAbility', description, 1, AbilityEffectTime.AfterLoadShield, AbilityEffectType.Reccuring, abilityArgs, attachedCard)

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
        description = 'You reflect half the attack value to your opponent to a minimum of 1'
        abilityArgs = [AbilityArgType.CurrentPlayer, AbilityArgType.AttackValue]
        Ability.__init__(self, 'IvoryAbility', description, 1, AbilityEffectTime.AfterShieldAttack, AbilityEffectType.Reccuring, abilityArgs, attachedCard)

    def invoke(self, player, attack_value):
        if player:
            damage_amount = math.floor(attack_value / 2)
            if damage_amount <= 0:
                damage_amount = 1
            print('Damage Reflected from Ivory: ', damage_amount)
            logger.info('Damage Reflected from Ivory: {0}'.format(damage_amount))
            player.health -= damage_amount

class ImmediateGainEnergy(Ability):

    def __init__(self, attachedCard, amount):
        description = 'Gain {0} energy.'.format(amount)
        Ability.__init__(self, 'ImmediateGainEnergy', description, 1, AbilityEffectTime.OnPlay, AbilityEffectType.Immediate, AbilityArgType.CardOwner, attachedCard)
        self.amount = amount

    def invoke(self, player):
        if player:
            player.energy_pool += self.amount


class ImmediateGainHealth(Ability):

    def __init__(self, attachedCard, amount):
        description = 'Gain {0} health.'.format(amount)
        Ability.__init__(self, 'ImmediateGainHealth', description, 1, AbilityEffectTime.OnPlay, AbilityEffectType.Immediate, AbilityArgType.CardOwner, attachedCard)
        self.amount = amount

    def invoke(self, player):
        if player:
            player.health += self.amount

class WhenLoadsShieldGainEnergy(Ability):

    def __init__(self, attachedCard, amount):
        description = 'When your opponent loads a shield gain {0} energy'.format(amount)
        Ability.__init__(self, 'WhenLoadsShieldGainEnergy', description, 1, AbilityEffectTime.AfterLoadShield, AbilityEffectType.Reccuring, AbilityArgType.CardOwner, attachedCard)
        self.amount = amount

    def invoke(self, player):
        if player:
            playerArea = player.getPlayerArea(self.attachedCard)
            if playerArea:
                playerHasCard = len(list(filter(lambda x: x.uniqueCardId == self.attachedCard.uniqueCardId, playerArea)))
                if playerHasCard > 0:
                    if not self.attachedCard.isFaceDown:
                        player.energy_pool += self.amount

class IcariusAbility(Ability):

    def __init__(self, attachedCard):
        description = 'Initiate an Attack of 3 energy. If the attack passed a loaded absorbing shield then add the load amount to this attack.'
        abilityArgs = [AbilityArgType.Table, AbilityArgType.Card]
        Ability.__init__(self, 'IcariusAbility', description, 1, AbilityEffectTime.OnPlay, AbilityEffectType.Immediate, abilityArgs, attachedCard)

    def invoke(self, table, card):
        if table:
            table.attack_value = 3
            actionResolver = ActionResolver()
            initiateAttackAction = InitiateAttackAction()
            initiateAttackAction.initiateAttack(table, actionResolver.handleAbility)
