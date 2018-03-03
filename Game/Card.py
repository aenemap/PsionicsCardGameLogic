import logging

logger = logging.getLogger(__name__)

class Card(object):

    def __init__(self, id, name, type, subType, energy_cost):
        self.id =id
        self.name = name
        self.type = type
        self.subType = subType,
        self.energy_cost = energy_cost
        self.uniqueCardId = None
        self.ability = None


    def printCard(self, card):
        self.printCard(card)

    def logCard(self, card):
        self.logCard(card)

class ShieldCard(Card):

    def __init__(self, id, name, type, subType, energy_cost, consistency_value, isFaceDown):
        Card.__init__(self, id, name, type, subType, energy_cost)
        self.consistency_value = consistency_value
        self.isFaceDown = isFaceDown
        self.defence_value = None
        self.absorbing_value = None
        self.isLoadedWithEnergy = False
        logger.info('Shield Card {0} Created'.format(self.name))

    def logCard(self, card):
        logger.info('---------------------- Card ---------------------')
        logger.info('Id:{0}'.format(self.id))
        logger.info('Name:{0}'.format(self.name))
        logger.info('Type:{0}'.format(self.type))
        logger.info('Sub Type:{0}'.format(self.subType))
        logger.info('Energy Cost:{0}'.format(self.energy_cost))
        logger.info('Consistency Value:{0}'.format(self.consistency_value))
        logger.info('Is Facedown:{0}'.format(self.isFaceDown))
        logger.info('Defence Value:{0}'.format(self.defence_value))
        logger.info('Absorbing Value:{0}'.format(self.absorbing_value))
        logger.info('-------------------------------------------------')


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
            print('id:{0} - Name:{1} - EnergyCost:{2} - DefenceValue:{3} - AbsorbingValue:{4} - Consistency:{5} - Ability:{6}'.format(
                card.id,card.name,
                card.energy_cost,
                card.defence_value,
                card.absorbing_value,
                card.consistency_value,
                abilityDescription
            ))


class TalentCard(Card):
    def __init__(self, id, name, type, subType, energy_cost, trash_value, isFaceDown):
        Card.__init__(self, id, name, type, subType, energy_cost)
        self.trash_value = trash_value
        self.isFaceDown = isFaceDown
        logger.info('Talent Card {0} Created'.format(self.name))

    def isCardFaceDown(self, value):
        self.isFaceDown = value

    def logCard(self, card):
        logger.info('---------------------- Card ---------------------')
        logger.info('Id:{0}'.format(self.id))
        logger.info('Name:{0}'.format(self.name))
        logger.info('Type:{0}'.format(self.type))
        logger.info('Sub Type:{0}'.format(self.subType))
        logger.info('Energy Cost:{0}'.format(self.energy_cost))
        logger.info('Is Facedown:{0}'.format(self.isFaceDown))
        logger.info('Trash Value:{0}'.format(self.trash_value))
        logger.info('-------------------------------------------------')



    def printCard(self, card):
        if self.isFaceDown:
            print('id:{0} - Talent card face down'.format(card.id))
        else:
            abilityDescription = ''
            if card.ability:
                abilityDescription = card.ability.abilityDescription
            print('id:{0} - Name:{1} - EnergyCost:{2} - Trash:{3} - Ability:{4}'.format(card.id, card.name, card.energy_cost, card.trash_value, abilityDescription))


class EventCard(Card):
    def __init__(self, id, name, type, subType, energy_cost):
        Card.__init__(self, id, name, type, subType, energy_cost)
        self.isFaceDown = False

    def logCard(self, card):
        logger.info('---------------------- Card ---------------------')
        logger.info('Id:{0}'.format(self.id))
        logger.info('Name:{0}'.format(self.name))
        logger.info('Type:{0}'.format(self.type))
        logger.info('Sub Type:{0}'.format(self.subType))
        logger.info('Energy Cost:{0}'.format(self.energy_cost))
        logger.info('-------------------------------------------------')

    def printCard(self, card):
        abilityDescription = ''
        if card.ability:
            abilityDescription = card.ability.abilityDescription
        print('id:{0} - Name:{1} - EnergyCost:{2}  - Ability:{3}'.format(card.id,card.name, card.energy_cost, abilityDescription))
