class Card(object):

    def __init__(self, id, name, type, sub_type, energy_cost):
        self.id =id
        self.name = name
        self.type = type
        self.sub_type = sub_type,
        self.energy_cost = energy_cost
        self.uniqueCardId = None
        self.ability = None


    def printCard(self, card):
        self.printCard(card)

class ShieldCard(Card):

    def __init__(self, id, name, type, sub_type, energy_cost, defence_value, consistency_value, isFaceDown):
        Card.__init__(self, id, name, type, sub_type, energy_cost)
        self.consistency_value = consistency_value
        self.defence_value = defence_value
        self.isFaceDown = isFaceDown

    def addConsistency(self, amount):
        self.consistency_value += amount

    def removeConsistency(self, amount):
        self.consistency_value -= amount

    def isCardFaceDown(self, value):
        self.isFaceDown = value

    def printCard(self, card):
        if self.isFaceDown:
            print('id:{0} - Shield card face down'.format(card.id))
        else:
            abilityDescription = ''
            if card.ability:
                abilityDescription = card.ability.abilityDescription
            print('id:{0} - Name:{1} - EnergyCost:{2} - Consistency:{3} - Ability:{4}'.format(card.id,card.name, card.energy_cost, card.consistency_value, abilityDescription))


class TalentCard(Card):
    def __init__(self, id, name, type, sub_type, energy_cost, trash_value, isFaceDown):
        Card.__init__(self, id, name, type, sub_type, energy_cost)
        self.trash_value = trash_value
        self.isFaceDown = isFaceDown

    def isCardFaceDown(self, value):
        self.isFaceDown = value

    def printCard(self, card):
        if self.isFaceDown:
            print('id:{0} - Talent card face down'.format(card.id))
        else:
            abilityDescription = ''
            if card.ability:
                abilityDescription = card.ability.abilityDescription
            print('id:{0} - Name:{1} - EnergyCost:{2} - Trash:{3} - Ability:{4}'.format(card.id, card.name, card.energy_cost, card.trash_value, abilityDescription))


class EventCard(Card):
    pass
