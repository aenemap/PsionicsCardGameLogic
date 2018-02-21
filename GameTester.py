from Game.Card import *
from Game.Deck import Deck
from Game.CardPool import *
from Game.Player import Player
from Game.Deck import Deck
from Game.Hand import Hand
from Game.Table import Table
from Game.Enums import *
from Game.Logger import *

import uuid
import sys
import copy


deck1 = Deck(uuid.uuid4(), 'Player1 Deck')
deck2 = Deck(uuid.uuid4(), 'Player2 Deck')

for card in cardPool:
    for x in range(0,3):
        card  = copy.copy(card)
        deck1.addCardToDeck(card)
        deck2.addCardToDeck(card)

deck1.shuffleDeck()
deck2.shuffleDeck()

player1 = Player(
    name='John',
    health=30,
    energy_pool=5
)
player1.addDeckToPlayer(deck1)
player1.selectDeck(deck1)
player2 = Player(
    name='George',
    health=30,
    energy_pool=5
)
player2.addDeckToPlayer(deck2)
player2.selectDeck(deck2)

print('Player 1 Deck')
player1.deck.printDeck()
print('Player 2 Deck')
player2.deck.printDeck()

allHands = Hand(5,5)
player1Hand = Hand(5,5)
player2Hand = Hand(5,5)
for x in range(0, allHands.hand_size):
    player1Hand.addCardToHand(player1.deck.drawCardFromDeck(DrawCard.DrawFromTopOfDeck))
    player2Hand.addCardToHand(player2.deck.drawCardFromDeck(DrawCard.DrawFromTopOfDeck))

player1.hand = player1Hand
player2.hand = player2Hand

# print('Player 1 Hand')
# player1.hand.printHand()
# print('Player 2 Hand')
# player2.hand.printHand()

playTable = Table(player1=player1, player2=player2)
playTable.printTable()
playTable.startGame()
