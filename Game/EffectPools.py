from Game.Enums import *
import logging

logger = logging.getLogger(__name__)

class Effect(object):

    def __init__(self):
        self.effectPool = []

    def getLength(self):
        return len(self.effectPool)

    def add(self, ability):
        self.effectPool.append(ability)

    def removeEffect(self, ability):
        logger.info('Removing effect from effectPool => {0}'.format(ability))
        if len(self.effectPool) > 0:
            if self.effectPool.index(ability):
                abilityIndex = self.effectPool.index(ability)
                if abilityIndex > -1:
                    self.effectPool.pop(abilityIndex)

    def invoke(self):
        pass



class GameEffects(Effect):
    def __init__(self):
        Effect.__init__(self)

    def invoke(self, table, abilityEffectTime, abilityEffectType, targetCard):
        logger.info('Inside GameEffects => invoke()')
        logger.info('Effect Pool => {0}'.format(self.effectPool))
        if abilityEffectTime:
            effectsToInvoke = list(filter(lambda x: x.abilityEffectTime == abilityEffectTime, self.effectPool))
        if abilityEffectType:
            effectsToInvoke = list(filter(lambda x: x.abilityEffectType == abilityEffectType, self.effectPool))
        if abilityEffectTime and abilityEffectType:
            effectsToInvoke = list(filter(lambda x: x.abilityEffectTime == abilityEffectTime and x.abilityEffectType == abilityEffectType, self.effectPool))

        logger.info('effectsToInvoke => {0}'.format(effectsToInvoke))
        if len(effectsToInvoke) > 0:
            sortedEffectsToInvoke = sorted(effectsToInvoke, key=lambda k: k.priority)

            for effect in sortedEffectsToInvoke:
                abilityArgs = effect.getArgsForAbility(table, effect, targetCard)
                logger.info('Invoking Effect => {0}'.format(effect))
                if isinstance(abilityArgs, list):
                    effect.invoke(*abilityArgs)
                else:
                    effect.invoke(abilityArgs)
                if effect.abilityEffectType == AbilityEffectType.Immediate:
                    self.removeEffect(effect)
