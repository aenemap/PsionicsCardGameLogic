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
            cardIdToPlay = input("Select card from Hand(id):")
            cardIdToPlay = int(cardIdToPlay)
            cardToPlay = currentPlayer.hand.getCardFromHand(cardIdToPlay)
            if cardToPlay:
                currentPlayer.removeFromEnergyPool(cardToPlay.energy_cost)
                currentPlayer.playCard(cardToPlay)
            else:
                print('Card with id {0} could not be found in Hand', cardIdToPlay)
        elif action == TurnAction.Concentration.value:
            #Player gains 1 energy to his energy pool
            currentPlayer.addToEnergyPool(1)
        elif action == TurnAction.InitiateAttack.value:
            #Player Initiates attack and he choses the amount of the attack
            #The amount will be substracted from his energy_pool
            attack_value = input("How much energy to spend for the attack:")
            attack_value = int(attack_value)
            currentPlayer.removeFromEnergyPool(attack_value)
            attack_value = shieldAreaResolution(currentPlayer, opposingPlayer, attack_value)
            #if any attack pass the shield can be used to trash talents or attack the players health
            print('Remain Attack after Shield Area:', attack_value)
            if attack_value > 0:
                attack_value = talentAreaResolution(currentPlayer, opposingPlayer, attack_value)

            print('Remain Attack after Talent Area:', attack_value)
            if attack_value > 0:
                # any remain attack goes to player
                print('Damage Opponent by {0}'.format(attack_value))
                opposingPlayer.takeDamage(attack_value)




def shieldAreaResolution(currentPlayer, opposingPlayer, attack_value):
    #if the opposingPlayer has shields currentPlayer chooses the shield to attack
    if len(opposingPlayer.playerArea[PlayerArea.Shields.value]) > 0:
        shieldToAttack = input("Choose a shield to attack (id):")
        shieldToAttack = int(shieldToAttack)
        shield = opposingPlayer.getCardFromPlayerArea(shieldToAttack, PlayerArea.Shields)
        if shield.isFaceDown:
            # if the shield is face down the opposing players desides to load it or not if he has the energy
            if shield.energy_cost <= opposingPlayer.energy_pool:
                opponentLoadsShield = input('Does opponents loads the shield?(yes/no):')
                if (opponentLoadsShield == 'yes'):
                    opposingPlayer.removeFromEnergyPool(shield.energy_cost)
                    shield.isCardFaceDown(False)
                    if attack_value >= shield.energy_cost:
                        attack_value -= shield.energy_cost
                        shield.removeConsistency(1)
                        if shield.consistency_value <=0:
                            opposingPlayer.removeCardFromPlayerArea(shield.id, PlayerArea.Shields.value)
                    else:
                        attack_value = 0
                else:
                    print('Opponent does not load the shield. Full attack pass')
                    return attack_value
            else:
                print('Opponent does not have the energy to load the shield. Full attack pass')
                return attack_value

        else:
            if attack_value >= shield.energy_cost:
                attack_value -= shield.energy_cost
                shield.removeConsistency(1)
            else:
                attack_value = 0

    return attack_value

def talentAreaResolution(currentPlayer, opposingPlayer, attack_value):
    # check if opposing player has any talents
    if len(opposingPlayer.playerArea[PlayerArea.Talents.value]) > 0:
        hasFaceDownTalents = len(list(filter(lambda x : x.isFaceDown, opposingPlayer.playerArea[PlayerArea.Talents.value])))
        if hasFaceDownTalents > 0:
            #if opponent has face down talents choose if  you want to reveal one
            revealTalent = input('Opposing Player has hidden talents do you want to reveal 1?:')
            if revealTalent == 'yes':
                whichTalent = input('Choose a talent to reveal (id):')
                whichTalent = int(whichTalent)
                talent = opposingPlayer.getCardFromPlayerArea(whichTalent, PlayerArea.Talents)
                talent.isCardFaceDown(False)
                if talent.trash_value <= attack_value:
                    #if you can trash it choose if you want
                    trashTalent = input('The trash cost of the talent card is {0}. Do you want to trash it? (yes/no)'.format(talent.trash_value))
                    if trashTalent == 'yes':
                        attack_value = attack_value - talent.trash_value
                        opposingPlayer.removeCardFromPlayerArea(talent.id, PlayerArea.Talents.value)
                else:
                    print('You cannot trash the talent')
        # if the opponent doesnt have any hidden talents check if you can trash any of the revealed
        canTrashTalents = len(list(filter(lambda x : x.trash_value <= attack_value and not x.isFaceDown, opposingPlayer.playerArea[PlayerArea.Talents.value])))
        if canTrashTalents > 0:
            whichTalent = input('Do you want to trash a talent?(id)')
            if len(whichTalent) > 0:
                talent = opposingPlayer.getCardFromPlayerArea(whichTalent, PlayerArea.Talents)
                attack_value = attack_value - talent.trash_value
                opposingPlayer.removeCardFromPlayerArea(talent.id, PlayerArea.Talents.value)

    return attack_value




        # canTrashTalents = len(list(filter(lambda x : x.trash_value <= attack_value, opposingPlayer.playerArea[PlayerArea.Talents.value])))
        # if canTrashTalents> 0:
