import random
import sys
from Game.Enums import *
from Game.Card import Card
from Game.ActionResolver import *

class Table(object):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.actionsPerTurn = 4

    def startGame(self):
        startPlayer = random.randint(1,2)

        print('Starting Player is Player Number {0}'.format(startPlayer))
        currentPlayer = self.player1 if startPlayer == 1 else self.player2
        opposingPlayer = self.player2 if startPlayer == 1 else self.player1
        while(True):
            #Start Of Turn Effects

            #Actions
            for action in range(1, self.actionsPerTurn + 1):
                sys.stdout.write(ConsoleColors.LightPurple.value)
                print('Player {0}, Action {1}'.format(startPlayer, action))
                print('Health:', currentPlayer.health)
                print('Energy:', currentPlayer.energy_pool)
                sys.stdout.write(ConsoleColors.Reset.value)
                sys.stdout.write(ConsoleColors.Cyan.value)
                for action in TurnAction:
                    print('{0} - {1}'.format(action.value, action))
                sys.stdout.write(ConsoleColors.Reset.value)
                print('')
                action = input('Select Action:')
                ActionResolver.resolveAction(action, currentPlayer, opposingPlayer)
                self.printTable()

            #End Of Turn Effects

            if startPlayer == 1:
                startPlayer = 2
                currentPlayer = self.player2
                opposingPlayer = self.player1
            else:
                startPlayer = 1
                currentPlayer = self.player1
                opposingPlayer = self.player2

            self.player1.health -= 10
            print(self.player1.health)
            if currentPlayer.health <= 0:
                print('GAME OVER')
                break





    def printTable(self):

        print('------------- Player2 play area ---------------')
        print('')
        print('------------- Discard Pile ---------------- ')
        for card in self.player2.playerArea['DiscardPile']:
            card.printCard(card)
        print('')
        print('------------- Hand ---------------- ')
        sys.stdout.write(ConsoleColors.LightGreen.value)
        self.player2.hand.printHand()
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Talents ---------------- ')
        sys.stdout.write(ConsoleColors.Blue.value)
        for card in self.player2.playerArea['Talents']:
            card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Shields ---------------- ')
        sys.stdout.write(ConsoleColors.Red.value)
        for card in self.player2.playerArea['Shields']:
            card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('================================================================')
        print('')
        sys.stdout.write(ConsoleColors.Red.value)
        for card in self.player1.playerArea['Shields']:
            card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Shields ---------------- ')
        sys.stdout.write(ConsoleColors.Blue.value)
        for card in self.player1.playerArea['Talents']:
            card.printCard(card)
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Talents ---------------- ')
        print('')
        sys.stdout.write(ConsoleColors.LightGreen.value)
        self.player1.hand.printHand()
        sys.stdout.write(ConsoleColors.Reset.value)
        print('')
        print('------------- Hand ---------------- ')
        for card in self.player1.playerArea['DiscardPile']:
            card.printCard(card)
        print('')
        print('------------- Discard Pile ---------------- ')
        print('')
        print('------------- Player1 play area ---------------')
