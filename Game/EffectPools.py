import logging

logger = logging.getLogger(__name__)

class Effect(object):

    def __init__(self):
        self.effectPool = []

    def getLength(self):
        return len(self.effectPool)

    def add(self, ability):
        self.effectPool.append(ability)

    def removeEffect(self, card):
        if len(list(filter(lambda x : x.attachedCard.id == card.id, self.effectPool))):
            abilityIndex = self.effectPool.index(card.ability)
            if abilityIndex > -1:
                self.effectPool.pop(abilityIndex)

    def invoke(self, table):

        sortedAbilities = sorted(self.effectPool, key=lambda k: k.priority)
        for effect in sortedAbilities:
            abilityArgs = effect.getArgsForAbility(table, effect.attachedCard, None)
            logger.info('Invoking Effect => {0}'.format(effect))
            if isinstance(abilityArgs, list):
                effect.invoke(*abilityArgs)
            else:
                effect.invoke(abilityArgs)



class StartOfTurn(Effect):
    pass


class EndOfTurn(Effect):
    pass

class ReccurringEffects(Effect):

    def __init__(self):
        Effect.__init__(self)

    def invoke(self, table, attack_value, abilityEffectTime):
        effectsToInvoke = list(filter(lambda x: x.abilityEffectTime == abilityEffectTime, self.effectPool))
        logger.info('Effects to Invoke length:{0} , {1}'.format(len(effectsToInvoke), abilityEffectTime))
        if len(effectsToInvoke) > 0:
            sortedEffectsToInvoke = sorted(effectsToInvoke, key=lambda k: k.priority)
            for effect in sortedEffectsToInvoke:
                abilityArgs = effect.getArgsForAbility(table, effect.attachedCard, attack_value)
                logger.info('Invoking Effect => {0}'.format(effect))
                if isinstance(abilityArgs, list):
                    effect.invoke(*abilityArgs)
                else:
                    effect.invoke(abilityArgs)
