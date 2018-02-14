from Game.Enums import *

class ActionResolver(object):

    @staticmethod
    def resolveAction(action, currentPlayer, opposingPlayer):
        if action == TurnAction.DrawCard.value:
            print('Player {0} choose the {1} action'.format(currentPlayer.name, TurnAction.DrawCard))
            currentPlayer.hand.addCardToHand(currentPlayer.deck.drawCardFromTopOfDeck())
        elif action == TurnAction.CreateShield.value:
            cardIdToPlay = input("Id of Shield card:")
            cardIdToPlay = int(cardIdToPlay)
            cardToPlay = currentPlayer.hand.getCardFromHand(cardIdToPlay)
            if cardToPlay:
                print('cardToPlay => ', cardToPlay)
                currentPlayer.substractEnergy(cardToPlay.energy_cost)
                currentPlayer.playCard(cardToPlay)
            else:
                print('Card with id {0} could not be found in Hand', cardIdToPlay)
        elif action == TurnAction.Concentration.value:
            currentPlayer.addEnergy(1)
