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

    def getArgsForAbility(self, table, ability, targetCard):
        args = None
        if isinstance(ability.abilityArgType, list):
            abilityArgs = []
            for abilityArg in ability.abilityArgType:
                if abilityArg == AbilityArgType.Card:
                    abilityArgs.append(ability.attachedCard)
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
                    abilityArgs.append(table.attack_value)
                elif abilityArg == AbilityArgType.TargetCard:
                    abilityArgs.append(targetCard)

            args = abilityArgs
        else:
            abilityArgs = None
            if ability.abilityArgType == AbilityArgType.Card:
                abilityArgs = ability.attachedCard
            elif ability.abilityArgType == AbilityArgType.CurrentPlayer:
                abilityArgs = table.currentPlayer
            elif ability.abilityArgType == AbilityArgType.OpposingPlayer:
                abilityArgs = table.opposingPlayer
            elif ability.abilityArgType == AbilityArgType.CardOwner:
                abilityArgs = table.currentPlayer
            elif ability.abilityArgType == AbilityArgType.BothPlayers:
                abilityArgs = []
                abilityArgs.append(table.currentPlayer)
                abilityArgs.append(table.opposingPlayer)
            elif ability.abilityArgType == AbilityArgType.Table:
                abilityArgs = table
            elif ability.abilityArgType == AbilityArgType.AttackValue:
                abilityArgs = table.attack_value
            elif ability.abilityArgType == AbilityArgType.TargetCard:
                abilityArgs = targetCard

            args = abilityArgs

        return args



    def invoke():
        pass
