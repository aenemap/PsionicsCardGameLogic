from Game.Enums import *

class DrawCardAction(object):
    def __init__(self):
        pass

    def drawCard(self, player, fromWhere):
        player.hand.addCardToHand(player.deck.drawCardFromDeck(fromWhere))

class PlayCardAction(object):
    def __init__(self):
        pass

    # def playCard(self, table):
    #     logger.info('Player {0} chose the {1} action'.format(table.currentPlayer.name, TurnAction.PlayCard))
    #     cardIdToPlay = input("Select card from Hand(id):")
    #     cardIdToPlay = int(cardIdToPlay)
    #     cardToPlay = table.currentPlayer.hand.getCardFromHand(cardIdToPlay)
    #     logger.info('Player chose the {} card to play'.format(cardToPlay.name))
    #     cardToPlay.logCard(cardToPlay)
    #     if cardToPlay:
    #         if not cardToPlay.isFaceDown:
    #             table.currentPlayer.removeFromEnergyPool(cardToPlay.energy_cost)
    #         table.currentPlayer.playCard(cardToPlay)
    #         if cardToPlay.ability:
    #             #set the reference of the card to the ability. Issue because of copies
    #             cardToPlay.ability.attachedCard = cardToPlay
    #             if not cardToPlay.isFaceDown:
    #                 ActionResolver.handleAbility(table, cardToPlay)
    #     else:
    #         print('Card with id {0} could not be found in Hand', cardIdToPlay)
