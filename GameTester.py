from Game.Card import *
from Game.Deck import Deck
from Game.CardPool import *
from Game.Player import Player
from Game.Deck import Deck
import uuid


deck1 = Deck(uuid.uuid4(), 'Player1 Deck')

for card in cardPool:
    deck1.addCardToDeck(card)

deck1.shuffleDeck()
deck1.printDeck()

card = deck1.deck.pop()
print(card.name)
