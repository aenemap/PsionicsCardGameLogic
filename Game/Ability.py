class Ability(object):

    def __init__(self, name, abilityDescription, priority, abilityEffectType, abilityArgType, attachedCard):
        self.name = name
        self.abilityDescription =  abilityDescription
        self.priority = priority
        self.abilityEffectType = abilityEffectType
        self.abilityArgType = abilityArgType
        self.attachedCard = attachedCard
        self.canStack = True


    def invoke():
        pass
