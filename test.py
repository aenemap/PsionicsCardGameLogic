# def grep(pattern):
#     print('Searching for ', pattern)
#     while True:
#         line = (yield)
#         if pattern in line:
#             print(line)
#
# search = grep('coroutine')
# next(search)
# search.send("I love you")
# search.send("Dont you love me?")
# search.send("I love coroutines instead")

# from time import sleep

# def turns(totalTurns):
#     currentTurn = 1
#     while currentTurn <= totalTurns:
#         yield currentTurn
#         currentTurn += 1
#
#
# while True:
#     for action in turns(5):
#         print('Action {0}'.format(action))


# def func1():
#     print('I am func1')
#
# def func2():
#     print('I am func2')
#
# functions = []
# functions.append(func1)
# functions.append(func2)
#
# for func in functions:
#     func()

# from collections import deque
# def func1():
#     print('I am func1')
#
# def func2():
#     print('I am func2')
#
#
# functions = deque([])
# functions.append(func2)
# functions.append(func1)
#
# function = functions.popleft()
# function()
# function = functions.popleft()
# function()

# def ability1():
#     print('Resolving ability 1')
#
# def ability2():
#     print('Resolving ability 2')
#
# def ability3():
#     print('Resolving ability 3')
#
# def ability4():
#     print('Resolving ability 4')
#
# def ability5():
#     print('Resolving ability 5')
#
# abbilitiesList = []
# abbilitiesList.append({'priority': 2, 'ability': ability1})
# abbilitiesList.append({'priority': 5, 'ability': ability2})
# abbilitiesList.append({'priority': 1, 'ability': ability3})
# abbilitiesList.append({'priority': 3, 'ability': ability4})
# abbilitiesList.append({'priority': 4, 'ability': ability5})
#
# sortedAbilities = sorted(abbilitiesList, key=lambda k: k['priority'])
#
# for ab in sortedAbilities:
#     ab['ability']()


# def abilityTest(player, amount):
#     print('the player {0} gains {1} health'.format(player, amount))
#
# startOfTurnEffects = set()
#
#
#
# startOfTurnEffect = abilityTest
#
# startOfTurnEffects.add(startOfTurnEffect)
#
# for startEffect in startOfTurnEffects:
#     startEffect('nick', '1')

# from Game.Player import Player
#
# class Card(object):
#
#     def __init__(self, id, name, type, sub_type, energy_cost):
#         self.id =id
#         self.name = name
#         self.type = type
#         self.sub_type = sub_type,
#         self.energy_cost = energy_cost
#
#         self.startOfTurnEffect = None
#         self.startOfTurnEffectPriority = None
#         self.endOfTurnEffect = None
#         self.endOfTurnEffectPriority = None
#         self.cardAbility = None
#         self.cardAbilityPriority = None
#
#     def printCard(self, card):
#         self.printCard(card)
#
# class TalentCard(Card):
#     def __init__(self, id, name, type, sub_type, energy_cost, trash_value, isFaceDown):
#         Card.__init__(self, id, name, type, sub_type, energy_cost)
#         self.trash_value = trash_value
#         self.isFaceDown = isFaceDown
#
#     def isCardFaceDown(self, value):
#         self.isFaceDown = value
#
#     def printCard(self, card):
#         if self.isFaceDown:
#             print('id:{0} - Talent card face down'.format(card.id))
#         else:
#             print('id:{0} - Name:{1} - EnergyCost:{2} - Trash:{3}'.format(card.id, card.name, card.energy_cost, card.trash_value))
#
#
# class Ability(object):
#
#     def __init__(self, name, priority):
#         self.name = name
#         self.priority = priority
#
#     def invoke(self):
#         pass
#
#
# class GainHealthAtStartOfRound(Ability):
#
#     def __init__(self,name, priority, cardOwner, health_amount):
#         Ability.__init__(self, name, priority)
#         self.cardOwner = cardOwner
#         self.health_amount = health_amount
#
#     def invoke(self, currentPlayer):
#         if currentPlayer.name == cardOwner.name:
#             self.cardOwner.health += self.health_amount
#             print('current player health = ', self.cardOwner.health)
#         else:
#             print('not current player')
#
# newTalentCard = TalentCard(
#     id=random.randint(1, 100),
#     name='Talent5',
#     type= CardType.Talent,
#     sub_type= '',
#     energy_cost=2,
#     trash_value=3,
#     isFaceDown=False)
# newTalentCard.cardAbility =
#
#
# cardOwner = Player(
#     name='John',
#     health=30,
#     deck=[],
#     energy_pool=5
# )
#
# otherPlayer = Player(
#     name='Nick',
#     health=30,
#     deck=[],
#     energy_pool=5
# )
# ability = GainHealthAtStartOfRound('gainHealthAtStartOfRound', 1, cardOwner, 1)
# ability.invoke(cardOwner)
# ability.invoke(otherPlayer)


def actions(currentAction, totalActions):
    while currentAction <= totalActions:
        yield print(currentAction)

currentAction = 1
for action in range(1,5):
    next(actions(currentAction, 5))
    currentAction += 1



class Turn(object):

    def __init__(self, totalActions):
        self.totalActions = totalActions

    def actions(currentAction, totalActions)
