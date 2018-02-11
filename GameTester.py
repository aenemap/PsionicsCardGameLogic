from Game.Card import *
from Game.Deck import Deck
from Game.CardPool import *
from Game.Player import Player
from Game.Deck import Deck
import uuid


deck1 = Deck(uuid.uuid4())

for card in cardPool:
    deck1.addCardToDeck(card)

for card in deck1.deck:
    print('{0},{1}'.format(card.id, card.name))

deck1.shuffleDeck()

print('--------------------------------')

for card in deck1.deck:
    print('{0},{1}'.format(card.id, card.name))
