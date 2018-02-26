from Game.Enums import *

class Ability(object):

    def __init__(self, name, abilityDescription, priority, abilityEffectTime, abilityEffectType, abilityArgType, attachedCard):
        self.name = name
        self.abilityDescription =  abilityDescription
        self.priority = priority
        self.abilityEffectTime = abilityEffectTime
        self.abilityEffectType = abilityEffectType
        self.abilityArgType = abilityArgType
        self.attachedCard = attachedCard
        self.canStack = True

    def getArgsForAbility(self, table, card, attack_value):
        args = None
        if isinstance(card.ability.abilityArgType, list):
            abilityArgs = []
            for abilityArg in card.ability.abilityArgType:
                if abilityArg == AbilityArgType.Card:
                    abilityArgs.append(card)
                elif abilityArg == AbilityArgType.CurrentPlayer:
                    abilityArgs.append(table.currentPlayer)
                elif abilityArg == AbilityArgType.OpposingPlayer:
                    abilityArgs.append(table.opposingPlayer)
                elif abilityArg == AbilityArgType.CardOwner:
                    abilityArgs.append(table.currentPlayer)
                elif abilityArg == AbilityArgType.BothPlayers:
                    abilityArgs.append(table.currentPlayer)
                    abilityArgs.append(table.opposingPlayer)
                elif abilityArg == AbilityArgType.Table:
                    abilityArgs.append(table)
                elif abilityArg == AbilityArgType.AttackValue:
                    abilityArgs.append(attack_value)

            args = abilityArgs
        else:
            abilityArgs = None
            if card.ability.abilityArgType == AbilityArgType.Card:
                abilityArgs = card
            elif card.ability.abilityArgType == AbilityArgType.CurrentPlayer:
                abilityArgs = table.currentPlayer
            elif card.ability.abilityArgType == AbilityArgType.OpposingPlayer:
                abilityArgs = table.opposingPlayer
            elif card.ability.abilityArgType == AbilityArgType.CardOwner:
                abilityArgs = table.currentPlayer
            elif card.ability.abilityArgType == AbilityArgType.BothPlayers:
                abilityArgs = []
                abilityArgs.append(table.currentPlayer)
                abilityArgs.append(table.opposingPlayer)
            elif card.ability.abilityArgType == AbilityArgType.Table:
                abilityArgs = table
            elif card.ability.abilityArgType == AbilityArgType.AttackValue:
                abilityArg = attack_value

            args = abilityArgs

        return args



    def invoke():
        pass
