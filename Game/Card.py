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
        self.abilities = []


    def printCard(self, card):
        self.printCard(card)

    def logCard(self, card):
        self.logCard(card)

class BasicShield(Card):

    def __init__(self, id, name, type, subType, energy_cost, consistency_value, isFaceDown):
        Card.__init__(self, id, name, type, subType, energy_cost)
        self.consistency_value = consistency_value
        self.isFaceDown = isFaceDown
        self.defence_value = None
        logger.info('Shield Card {0} Created'.format(self.name))

    def logCard(self, card):
        logger.info('---------------------- Card ---------------------')
        logger.info('Id:{0}'.format(self.id))
        logger.info('Name:{0}'.format(self.name))
        logger.info('Type:{0}'.format(self.type))
        logger.info('Sub Type:{0}'.format(self.subType[0]))
        logger.info('Energy Cost:{0}'.format(self.energy_cost))
        logger.info('Consistency Value:{0}'.format(self.consistency_value))
        logger.info('Is Facedown:{0}'.format(self.isFaceDown))
        logger.info('Defence Value:{0}'.format(self.defence_value))
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
            if len(card.abilities) > 0:
                for ab in card.abilities:
                    abilityDescription += ab.abilityDescription
            print('id:{0} - Name:{1} - EnergyCost:{2} - DefenceValue:{3} - AbsorbingValue:{4} - isLoadedWithEnergy:{5} - Consistency:{6} - Ability:{7}'.format(
                card.id,card.name,
                card.energy_cost,
                card.defence_value,
                card.absorbing_value if hasattr(card,'absorbing_value') else None,
                card.isLoadedWithEnergy if hasattr(card, 'isLoadedWithEnergy') else None,
                card.consistency_value,
                abilityDescription
            ))

class AbsorbingShield(BasicShield):

    def __init__(self, id, name, type, subType, energy_cost, consistency_value, isFaceDown):
        BasicShield.__init__(self, id, name, type, subType, energy_cost, consistency_value, isFaceDown)
        self.absorbing_value = None
        self.isLoadedWithEnergy = False



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
            if len(card.abilities) > 0:
                for ab in card.abilities:
                    abilityDescription += ab.abilityDescription
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
        if len(card.abilities) > 0:
            for ab in card.abilities:
                abilityDescription += ab.abilityDescription
        print('id:{0} - Name:{1} - EnergyCost:{2}  - Ability:{3}'.format(card.id,card.name, card.energy_cost, abilityDescription))
