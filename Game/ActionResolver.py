from Game.Enums import *

class ActionResolver(object):

    @staticmethod
    def resolveAction(action, currentPlayer, opposingPlayer):
        if action == TurnAction.DrawCard.value:
            #Draw the top card from the deck to players hand
            print('Player {0} choosed the {1} action'.format(currentPlayer.name, TurnAction.DrawCard))
            currentPlayer.hand.addCardToHand(currentPlayer.deck.drawCardFromTopOfDeck())
        elif action == TurnAction.PlayCard.value:
            #Play the chosen card from the hand to the players play area (Shields, Talents ....)
            cardIdToPlay = input("Select card id from Hand:")
            cardIdToPlay = int(cardIdToPlay)
            cardToPlay = currentPlayer.hand.getCardFromHand(cardIdToPlay)
            if cardToPlay:
                currentPlayer.substractFromEnergyPool(cardToPlay.energy_cost)
                currentPlayer.playCard(cardToPlay)
            else:
                print('Card with id {0} could not be found in Hand', cardIdToPlay)
        elif action == TurnAction.Concentration.value:
            #Player gains 1 energy to his energy pool
            currentPlayer.addToEnergyPool(1)
        elif action == TurnAction.InitiateAttack.value:
            #Player Initiates attack and he choses the amount of the attack
            #The amount will be taken from his energy_pool
            attack_value = input("How much energy to spend for the attack:")
            attack_value = int(attack_value)
            currentPlayer.substractFromEnergyPool(attack_value)
            #if the opposingPlayer has shields currentPlayer chooses the shield to attack
            if len(opposingPlayer.playerArea[PlayerArea.Shields]) > 0:
                shieldToAttack = input("Choose a shield to attack (id):")
                shieldToAttack = int(shieldToAttack)
                shield = opposingPlayer.getCardFromPlayerArea(shieldToAttack, PlayerArea.Shields)
                if shield.isFaceDown:
                    if shield.energy_cost <= opposingPlayer.energy_pool:
                        opponentLoadsShield = input('Does opponents loads the shield?:')
                        if (opponentLoadsShield == 'yes'):
                            opposingPlayer.substractFromEnergyPool(shield.energy_cost)
                            shield.isFaceDown = False
                            if attack_value >= shield.energy_cost:
                                attack_value -= shield.energy_cost
                                shield.consistency_value -= 1
                        else:
                            print('Opponent does not load the shield')
                    else:
                        print('Opponent does not have the energy to load the shield')
