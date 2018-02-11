from Game.Card import *
from Game.Deck import Deck
from Game.CardPool import *
from Game.Player import Player
from Game.Deck import Deck
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

# for x in range(0, 2):
#     card = deck1.drawCardFromTopOfDeck()
#     print(card.name)
