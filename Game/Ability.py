from Game.Enums import *

class Ability(object):

    def __init__(self, name, abilityDescription, priority, abilityEffectType, abilityArgType, attachedCard):
        self.name = name
        self.abilityDescription =  abilityDescription
        self.priority = priority
        self.abilityEffectType = abilityEffectType
        self.abilityArgType = abilityArgType
        self.attachedCard = attachedCard
        self.canStack = True

    def getArgsForAbility(self, table, currentPlayer, opposingPlayer, card):
        args = None
        if isinstance(card.ability.abilityArgType, list):
            abilityArgs = []
            for abilityArg in card.ability.abilityArgType:
                if abilityArg == AbilityArgType.Card:
                    abilityArgs.append(card)
                elif abilityArg == AbilityArgType.CurrentPlayer:
                    abilityArgs.append(currentPlayer)
                elif abilityArg == AbilityArgType.OpposingPlayer:
                    abilityArgs.append(opposingPlayer)
                elif abilityArg == AbilityArgType.CardOwner:
                    abilityArgs.append(currentPlayer)
                elif abilityArg == AbilityArgType.BothPlayers:
                    abilityArgs.append(currentPlayer)
                    abilityArgs.append(opposingPlayer)
                elif abilityArg == AbilityArgType.Table:
                    abilityArgs.append(table)

            args = abilityArgs
        else:
            abilityArgs = None
            if card.ability.abilityArgType == AbilityArgType.Card:
                abilityArgs = card
            elif card.ability.abilityArgType == AbilityArgType.CurrentPlayer:
                abilityArgs = currentPlayer
            elif card.ability.abilityArgType == AbilityArgType.OpposingPlayer:
                abilityArgs = opposingPlayer
            elif card.ability.abilityArgType == AbilityArgType.CardOwner:
                abilityArgs = currentPlayer
            elif card.ability.abilityArgType == AbilityArgType.BothPlayers:
                abilityArgs = []
                abilityArgs.append(currentPlayer)
                abilityArgs.append(opposingPlayer)
            elif card.ability.abilityArgType == AbilityArgType.Table:
                abilityArgs = table

            args = abilityArgs

        return args



    def invoke():
        pass
