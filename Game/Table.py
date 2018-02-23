import random
import sys
from Game.Enums import *
from Game.Card import Card
from Game.ActionResolver import *
import logging

class Table(object):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.currentPlayer = None
        self.opposingPlayer = None
        self.startOfTurnEffects = []
        self.endOfTurnEffects = []
        self.permanentEffects = []
        self.actionsPerTurn = 4



    def startGame(self):
        # startPlayer = random.randint(1,2)
        startPlayer = 1

        print('Starting Player is Player Number {0}'.format(startPlayer))
        self.currentPlayer = self.player1 if startPlayer == 1 else self.player2
        self.opposingPlayer = self.player2 if startPlayer == 1 else self.player1
        while(True):
            sys.stdout.write(ConsoleColors.Brown.value)
            print('############################### Player {0} TURN ######################'.format(startPlayer))
            sys.stdout.write(ConsoleColors.Reset.value)
            hasShieldsFaceDown = self.currentPlayer.hasCardsInPlayerArea(PlayerArea.Shields, True)
            hasTalentsFaceDown = self.currentPlayer.hasCardsInPlayerArea(PlayerArea.Talents, True)
            print('------------------ Before start of turn actions, only load shield or develop talents')
            if hasShieldsFaceDown or hasTalentsFaceDown:
                preAction = input('Do you want to take an action before the start of turn?(yes/no):')
                while preAction == 'yes':
                    print('1 - Load Shield')
                    print('2 - Develop Talent')
                    preTurnAction = int(input('Choose an action:'))
                    cardType = 'shield' if preTurnAction == 1 else 'talent'
                    whichCard = int(input('Choose the {0} to load (id):'.format(cardType)))
                    cardArea = PlayerArea.Shields if preTurnAction == 1 else PlayerArea.Talents
                    card = self.currentPlayer.getCardFromPlayerArea(whichCard, cardArea)
                    card.isFaceDown = False
                    if card.ability:
                        card.ability.attachedCard = card
                        ActionResolver.handleAbility(self, self.currentPlayer, self.opposingPlayer, card)
                    self.currentPlayer.energy_pool -= card.energy_cost
                    self.printTable()
                    hasShieldsFaceDown = self.currentPlayer.hasCardsInPlayerArea(PlayerArea.Shields, True)
                    hasTalentsFaceDown = self.currentPlayer.hasCardsInPlayerArea(PlayerArea.Talents, True)
                    if hasShieldsFaceDown or hasTalentsFaceDown:
                        preAction = input('Do you want to take an action before the start of turn?(yes/no):')
                    else:
                        preAction = 'no'

            #Start Of Turn Effects
            print('length of startOfTurnEffects => ', len(self.startOfTurnEffects))
            if len(self.startOfTurnEffects) > 0:
                print('------------ Start Of Turn Effects --------------')
                sortedAbilities = sorted(self.startOfTurnEffects, key=lambda k: k.priority)
                for effect in sortedAbilities:
                    print(effect)
                    abilityArgs = effect.getArgsForAbility(self, self.currentPlayer, self.opposingPlayer, effect.attachedCard, None)
                    if isinstance(abilityArgs, list):
                        effect.invoke(*abilityArgs)
                    else:
                        print('i am on else')
                        effect.invoke(abilityArgs)
                print('------------ Start Of Turn Effects Complete --------------')


            #Actions
            for action in range(1, self.currentPlayer.actionsPerTurn + 1):

                sys.stdout.write(ConsoleColors.LightPurple.value)
                print('Player {0}, Action {1}'.format(startPlayer, action))
                print('Health:', self.currentPlayer.health)
                print('Energy:', self.currentPlayer.energy_pool)
                sys.stdout.write(ConsoleColors.Reset.value)

                sys.stdout.write(ConsoleColors.Purple.value)
                print('Opposing Player')
                print('Health:', self.opposingPlayer.health)
                print('Energy:', self.opposingPlayer.energy_pool)
                sys.stdout.write(ConsoleColors.Reset.value)

                sys.stdout.write(ConsoleColors.Cyan.value)
                for action in TurnAction:
                    print('{0} - {1}'.format(action.value, action))
                sys.stdout.write(ConsoleColors.Reset.value)
                print('')
                action = input('Select Action:')
                # Check if the action can be executed , because of any card effect
                ActionResolver.resolveAction(
                    table = self,
                    action = action,
                    currentPlayer=self.currentPlayer,
                    opposingPlayer=self.opposingPlayer,
                    startOfTurnEffects=self.startOfTurnEffects,
                    endOfTurnEffects=self.endOfTurnEffects
                    )
                self.printTable()

            #After each action check if any players health is at zero and end the game
            if self.currentPlayer.health <= 0 or self.opposingPlayer.health <= 0:
                print('GAME OVER')
                print('PLAYER {0} WINS'.format(self.currentPlayer.name if self.currentPlayer.health <= 0 else self.opposingPlayer.name))

            #End Of Turn Effects
            if len(self.endOfTurnEffects) > 0:
                print('------------ End Of Turn Effects --------------')
                sortedAbilities = sorted(self.endOfTurnEffects, key=lambda k: k.priority)
                for effect in sortedAbilities:
                    abilityArgs = effect.getArgsForAbility(self, self.currentPlayer, self.opposingPlayer, effect.attachedCard, None)
                    if isinstance(abilityArgs, list):
                        effect.invoke(*abilityArgs)
                    else:
                        effect.invoke(abilityArgs)
                print('------------ End Of Turn Effects Complete --------------')

            if startPlayer == 1:
                startPlayer = 2
                self.currentPlayer = self.player2
                self.opposingPlayer = self.player1
            else:
                startPlayer = 1
                self.currentPlayer = self.player1
                self.opposingPlayer = self.player2




    def printTable(self):

        print('------------- Player2 play area ---------------')
        print('')
        print('------------- Discard Pile ---------------- ')
        for card in self.player2.playerArea['DiscardPile']:
            card.printCard(card)
        print('----------------------------------- ')
        print('')
        print('------------- Hand ---------------- ')
        sys.stdout.write(ConsoleColors.LightGreen.value)
        self.player2.hand.printHand()
        sys.stdout.write(ConsoleColors.Reset.value)
        print('----------------------------------- ')
        print('')
        print('------------- Talents ---------------- ')
        sys.stdout.write(ConsoleColors.Blue.value)
        for card in self.player2.playerArea['Talents']:
            card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('----------------------------------- ')
        print('')
        print('------------- Shields ---------------- ')
        sys.stdout.write(ConsoleColors.Red.value)
        for card in self.player2.playerArea['Shields']:
            card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('----------------------------------- ')
        print('')
        print('================================================================')
        print('')
        print('----------------------------------- ')
        sys.stdout.write(ConsoleColors.Red.value)
        for card in self.player1.playerArea['Shields']:
            card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Shields ---------------- ')
        print('----------------------------------- ')
        sys.stdout.write(ConsoleColors.Blue.value)
        for card in self.player1.playerArea['Talents']:
            card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Talents ---------------- ')
        print('')
        print('----------------------------------- ')
        sys.stdout.write(ConsoleColors.LightGreen.value)
        self.player1.hand.printHand()
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Hand ---------------- ')
        print('----------------------------------- ')
        for card in self.player1.playerArea['DiscardPile']:
            card.printCard(card)
        print('')
        print('------------- Discard Pile ---------------- ')
        print('')
        print('------------- Player1 play area ---------------')
