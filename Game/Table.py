import random
import sys
from collections import deque
from Game.Enums import *
from Game.Card import Card
from Game.ActionResolver import *
from Game.EffectPools import *
import logging

logger = logging.getLogger(__name__)

class Table(object):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.currentPlayer = None
        self.opposingPlayer = None
        self.gameEffects = None
        self.actionsPerTurn = 4
        self.attack_value = 0
        self.turnCounter = 0



    def startGame(self):
        # startPlayer = random.randint(1,2)
        logger.info('#################################################################################')
        logger.info('#################################################################################')
        logger.info('#################################################################################')
        logger.info('STARTING THE GAME')
        actionResolver = ActionResolver()
        startPlayer = 1
        logger.info('Start initiating pools for game effects')
        self.gameEffects = GameEffects()
        # self.startOfTurnEffects = StartOfTurn()
        # self.endOfTurnEffects = EndOfTurn()
        # self.reccuringEffects = ReccurringEffects()
        logger.info('End initiating pools for game effects')

        # print('Starting Player is Player Number {0}'.format(startPlayer))
        self.currentPlayer = self.player1 if startPlayer == 1 else self.player2
        logger.info('Player goes first is {0}'.format(self.currentPlayer.name))
        self.currentPlayer.logPlayer(True)
        self.opposingPlayer = self.player2 if startPlayer == 1 else self.player1
        logger.info('Player goes second is {0}'.format(self.currentPlayer.name))
        self.opposingPlayer.logPlayer(True)
        self.turnCounter = 0
        while(True):
            self.turnCounter += 1
            sys.stdout.write(ConsoleColors.Brown.value)
            print('############################### Player {0} TURN ######################'.format(startPlayer))
            logger.info('####################### TURN {0} #############################'.format(self.turnCounter))
            sys.stdout.write(ConsoleColors.Reset.value)
            self.printTable()

            hasShieldsFaceDown = self.currentPlayer.hasCardsInPlayerArea(PlayerArea.Shields, True)
            logger.info('Current Player has Shields Face Down:{0}'.format(hasShieldsFaceDown))

            hasTalentsFaceDown = self.currentPlayer.hasCardsInPlayerArea(PlayerArea.Talents, True)
            logger.info('Current Player has Talents Face Down:{0}'.format(hasTalentsFaceDown))

            print('------------------ Before start of turn actions, only load shield or develop talents')
            logger.info('------------------ Before start of turn actions, only load shield or develop talents')

            if hasShieldsFaceDown or hasTalentsFaceDown:
                logger.info('Current Player had shield or talents face down')
                preAction = input('Do you want to take an action before the start of turn?(yes/no):')
                while preAction == 'yes':
                    print('1 - Load Shield')
                    print('2 - Develop Talent')
                    preTurnAction = int(input('Choose an action:'))
                    cardType = 'shield' if preTurnAction == 1 else 'talent'
                    whichCard = int(input('Choose the {0} to load (id):'.format(cardType)))
                    cardArea = PlayerArea.Shields if preTurnAction == 1 else PlayerArea.Talents
                    logger.info('Card Area: {0}'.format(cardArea))
                    card = self.currentPlayer.getCardFromPlayerArea(whichCard, cardArea)
                    card.logCard(card)
                    card.isFaceDown = False
                    if len(card.abilites) > 0:
                        for ability in card.abilities:
                            ability.attachedCard = card
                        logger.info('Calling handleAbility from pre actions')
                        actionResolver.handleAbility(self, card)
                    self.currentPlayer.energy_pool -= card.energy_cost
                    logger.info('Current Player energy pool: {0}'.format(self.currentPlayer.energy_pool))
                    self.printTable()
                    hasShieldsFaceDown = self.currentPlayer.hasCardsInPlayerArea(PlayerArea.Shields, True)
                    hasTalentsFaceDown = self.currentPlayer.hasCardsInPlayerArea(PlayerArea.Talents, True)
                    if hasShieldsFaceDown or hasTalentsFaceDown:
                        preAction = input('Do you want to take an action before the start of turn?(yes/no):')
                    else:
                        preAction = 'no'

            #Start Of Turn Effects
            logger.info('----------------------------- START OF TURN EFFECTS -----------------------')
            self.gameEffects.invoke(
                table=self,
                abilityEffectTime = AbilityEffectTime.StartOfTurn,
                abilityEffectType = None,
                targetCard=None
            )
            print('------------ Start Of Turn Effects Complete --------------')
            logger.info('----------------------------- START OF TURN EFFECTS COMPLETE-----------------------')

            #Actions
            for action in range(1, self.currentPlayer.actionsPerTurn + 1):

                sys.stdout.write(ConsoleColors.LightPurple.value)
                print('Player {0}, Action {1}'.format(startPlayer, action))
                print('Health:', self.currentPlayer.health)
                print('Energy:', self.currentPlayer.energy_pool)
                sys.stdout.write(ConsoleColors.Reset.value)
                self.currentPlayer.logPlayer(False)

                sys.stdout.write(ConsoleColors.Purple.value)
                print('Opposing Player')
                print('Health:', self.opposingPlayer.health)
                print('Energy:', self.opposingPlayer.energy_pool)
                sys.stdout.write(ConsoleColors.Reset.value)
                self.opposingPlayer.logPlayer(False)

                sys.stdout.write(ConsoleColors.Cyan.value)
                for action in TurnAction:
                    print('{0} - {1}'.format(action.value, action))
                sys.stdout.write(ConsoleColors.Reset.value)
                print('')
                action = input('Select Action:')
                # TODO Check if the action can be executed , because of any card effect
                actionResolver.resolveAction(
                    table = self,
                    action = action
                    )
                self.printTable()

            #After each action check if any players health is at zero and end the game
            if self.currentPlayer.health <= 0 or self.opposingPlayer.health <= 0:
                print('GAME OVER')
                print('PLAYER {0} WINS'.format(self.currentPlayer.name if self.currentPlayer.health <= 0 else self.opposingPlayer.name))
                break

            #End Of Turn Effects
            logger.info('------------------------------ END OF TURN EFFECTS ---------------------------')
            self.gameEffects.invoke(
                table=self,
                abilityEffectTime = AbilityEffectTime.EndOfTurn,
                abilityEffectType = None,
                targetCard= None
            )
            print('------------ End Of Turn Effects Complete --------------')
            logger.info('------------------------------ END OF TURN EFFECTS COMPLETE---------------------------')

            if startPlayer == 1:
                startPlayer = 2
                self.currentPlayer = self.player2
                self.opposingPlayer = self.player1
            else:
                startPlayer = 1
                self.currentPlayer = self.player1
                self.opposingPlayer = self.player2

    def clearEffect(self, card):
        if len(card.abilities) > 0:
            for ability in card.abilities:
                self.gameEffects.removeEffect(ability)




    def printTable(self):

        print('------------- Player2 play area ---------------')
        print('')
        print('------------- Discard Pile ---------------- ')
        if self.opposingPlayer:
            for card in self.opposingPlayer.playerArea['DiscardPile']:
                card.printCard(card)
        print('----------------------------------- ')
        print('')
        print('------------- Hand ---------------- ')
        sys.stdout.write(ConsoleColors.LightGreen.value)
        if self.opposingPlayer:
            self.opposingPlayer.hand.printHand()
        sys.stdout.write(ConsoleColors.Reset.value)
        print('----------------------------------- ')
        print('')
        print('------------- Talents ---------------- ')
        sys.stdout.write(ConsoleColors.Blue.value)
        if self.opposingPlayer:
            for card in self.opposingPlayer.playerArea['Talents']:
                card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('----------------------------------- ')
        print('')
        print('------------- Shields ---------------- ')
        sys.stdout.write(ConsoleColors.Red.value)
        if self.opposingPlayer:
            for card in self.opposingPlayer.playerArea['Shields']:
                card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('----------------------------------- ')
        print('')
        print('================================================================')
        print('')
        print('----------------------------------- ')
        sys.stdout.write(ConsoleColors.Red.value)
        if self.currentPlayer:
            for card in self.currentPlayer.playerArea['Shields']:
                card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Shields ---------------- ')
        print('----------------------------------- ')
        sys.stdout.write(ConsoleColors.Blue.value)
        if self.currentPlayer:
            for card in self.currentPlayer.playerArea['Talents']:
                card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Talents ---------------- ')
        print('')
        print('----------------------------------- ')
        sys.stdout.write(ConsoleColors.LightGreen.value)
        if self.currentPlayer:
            self.currentPlayer.hand.printHand()
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Hand ---------------- ')
        print('----------------------------------- ')
        if self.currentPlayer:
            for card in self.currentPlayer.playerArea['DiscardPile']:
                card.printCard(card)
        print('')
        print('------------- Discard Pile ---------------- ')
        print('')
        print('------------- Player1 play area ---------------')
