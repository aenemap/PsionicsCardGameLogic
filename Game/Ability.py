class Ability(object):

    def __init__(self, name, priority, abilityEffectType, argType):
        self.name = name
        self.priority = priority
        self.abilityEffectType = abilityEffectType
        self.argType = argType
        self.canStack = True
        self.attachedCard = None


    def invoke():
        pass
