class Ability(object):

    def __init__(self, name, priority, abilityEffectType, argType):
        self.name = name
        self.priority = priority
        self.abilityEffectType = abilityEffectType
        self.argType = argType
        self.abilityIsAttachedToCard = None


    def invoke():
        pass
