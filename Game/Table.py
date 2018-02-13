import random

class Table:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.actionsPerTurn = 4

    def startGame(self):
        startPlayer = random.randint(1,2)
        currentPlayer = None
        print('Starting Player is Player Number {0}'.format(startPlayer))

        if startPlayer == 1:
            currentPlayer = self.player1
        else:
            currentPlayer = self.player2

        while(True):
            for action in range(1, self.actionsPerTurn + 1):
                print('Player {0}, Action {1}'.format(startPlayer, action))
                action = input('Action')

            if startPlayer == 1:
                startPlayer = 2
                currentPlayer = self.player2
            else:
                startPlayer = 1
                currentPlayer = self.player1

            self.player1.health -= 10
            print(self.player1.health)
            if currentPlayer.health <= 0:
                print('GAME OVER')
                break




    def printTable(self):

        print('------------- Player2 play area ---------------')

        print('')
        for card in self.player2.playerArea['DiscardPile']:
            print(card.name)
        print('------------- Discard Pile ---------------- ')

        print('')
        for card in self.player2.playerArea['Talents']:
            print(card.name)
        print('------------- Talents ---------------- ')


        print('')
        for card in self.player2.playerArea['Shields']:
            print(card.name)
        print('------------- Shields ---------------- ')


        print('')
        print('================================================================')
        print('')

        print('------------- Shields ---------------- ')
        for card in self.player1.playerArea['Shields']:
            print(card.name)

        print('')
        print('------------- Talents ---------------- ')
        for card in self.player1.playerArea['Talents']:
            print(card.name)

        print('')
        print('------------- Discard Pile ---------------- ')
        for card in self.player1.playerArea['DiscardPile']:
            print(card.name)

        print('')
        print('------------- Player1 play area ---------------')
