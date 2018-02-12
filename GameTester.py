from Game.Card import *
from Game.Deck import Deck
from Game.CardPool import *
from Game.Player import Player
from Game.Deck import Deck
from Game.Hand import Hand
import uuid


deck1 = Deck(uuid.uuid4(), 'Player1 Deck')
deck2 = Deck(uuid.uuid4(), 'Player2 Deck')

for card in cardPool:
    deck1.addCardToDeck(card)
    deck2.addCardToDeck(card)

deck1.shuffleDeck()
deck2.shuffleDeck()

player1 = Player(
    name='John',
    health=30,
    deck=deck1
)

player2 = Player(
    name='Nick',
    health=30,
    deck=deck2
)

print('Player 1 Deck')
player1.deck.printDeck()
print('Player 2 Deck')
player2.deck.printDeck()

allHands = Hand(3,3)
player1Hand = Hand(3,3)
player2Hand = Hand(3,3)
for x in range(0, allHands.hand_size):
    player1Hand.addCardToHand(player1.deck.drawCardFromTopOfDeck())
    player2Hand.addCardToHand(player2.deck.drawCardFromTopOfDeck())

player1.hand = player1Hand
player2.hand = player2Hand

print('Player 1 Hand')
player1.hand.printHand()
print('Player 2 Hand')
player2.hand.printHand()



player1.deck.drawCardFromTopOfDeck()



# for x in range(0, 2):
#     card = deck1.drawCardFromTopOfDeck()
#     print(card.name)
