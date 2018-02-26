from Game.Enums import *
from Game.Ability import Ability
from Game.Actions import *
import logging

logger = logging.getLogger(__name__)

class ActionResolver(object):

    @staticmethod
    def resolveAction(table, action):
        drawCardAction = DrawCardAction()
        if action == TurnAction.DrawCard.value:
            #Draw the top card from the deck to players hand
            logger.info('Player {0} chose the {1} action'.format(table.currentPlayer.name, TurnAction.DrawCard))
            print('Player {0} choosed the {1} action'.format(table.currentPlayer.name, TurnAction.DrawCard))
            # table.currentPlayer.hand.addCardToHand(table.currentPlayer.deck.drawCardFromDeck(DrawCard.DrawFromTopOfDeck))
            drawCardAction.drawCard(table.currentPlayer, DrawCard.DrawFromTopOfDeck)
        elif action == TurnAction.PlayCard.value:
            #Play the chosen card from the hand to the players play area (Shields, Talents ....)
            logger.info('Player {0} chose the {1} action'.format(table.currentPlayer.name, TurnAction.PlayCard))
            cardIdToPlay = input("Select card from Hand(id):")
            cardIdToPlay = int(cardIdToPlay)
            cardToPlay = table.currentPlayer.hand.getCardFromHand(cardIdToPlay)
            logger.info('Player chose the {} card to play'.format(cardToPlay.name))
            cardToPlay.logCard(cardToPlay)
            if cardToPlay:
                if not cardToPlay.isFaceDown:
                    table.currentPlayer.removeFromEnergyPool(cardToPlay.energy_cost)
                table.currentPlayer.playCard(cardToPlay)
                if cardToPlay.ability:
                    #set the reference of the card to the ability. Issue because of copies
                    cardToPlay.ability.attachedCard = cardToPlay
                    if not cardToPlay.isFaceDown:
                        ActionResolver.handleAbility(table, cardToPlay)
            else:
                print('Card with id {0} could not be found in Hand', cardIdToPlay)
        elif action == TurnAction.Concentration.value:
            #Player gains 1 energy to his energy pool
            logger.info('Player {0} chose the {1} action'.format(table.currentPlayer.name, TurnAction.Concentration))
            table.currentPlayer.addToEnergyPool(1)
        elif action == TurnAction.InitiateAttack.value:
            #Player Initiates attack and he choses the amount of the attack
            #The amount will be substracted from his energy_pool
            logger.info('Player {0} chose the {1} action'.format(table.currentPlayer.name, TurnAction.InitiateAttack))
            attack_value = input("How much energy to spend for the attack:")
            attack_value = int(attack_value)
            table.currentPlayer.removeFromEnergyPool(attack_value)
            attack_value = ActionResolver.shieldAreaResolution(table, attack_value)
            #if any attack pass the shield can be used to trash talents or attack the players health
            print('Remain Attack after Shield Area:', attack_value)
            if attack_value > 0:
                attack_value = ActionResolver.talentAreaResolution(table, attack_value)

            print('Remain Attack after Talent Area:', attack_value)
            if attack_value > 0:
                # any remain attack goes to player
                print('Damage Opponent by {0}'.format(attack_value))
                table.opposingPlayer.takeDamage(attack_value)


    @staticmethod
    def shieldAreaResolution(table, attack_value):
        #if the opposingPlayer has shields currentPlayer chooses the shield to attack
        if len(table.opposingPlayer.playerArea[PlayerArea.Shields.value]) > 0:
            shieldToAttack = input("Choose a shield to attack (id):")
            shieldToAttack = int(shieldToAttack)
            shield = table.opposingPlayer.getCardFromPlayerArea(shieldToAttack, PlayerArea.Shields)
            # substractFromAttackValue = None
            # if shield.sub_type == CardSubType.
            if shield.isFaceDown:
                # if the shield is face down the opposing players desides to load it or not if he has the energy
                if shield.energy_cost <= table.opposingPlayer.energy_pool:
                    opponentLoadsShield = input('Does opponents loads the shield?(yes/no):')
                    if (opponentLoadsShield == 'yes'):
                        table.opposingPlayer.removeFromEnergyPool(shield.energy_cost)
                        if shield.ability:
                            logger.info('Shield {0} has ability'.format(shield.name))
                            logger.info('Adding ability to reccuringEffects')
                            ActionResolver.handleAbility(shield.ability)
                        table.reccuringEffects.invoke(table, attack_value, AbilityEffectTime.BeforeLoadShield)
                        shield.isCardFaceDown(False)
                        table.reccuringEffects.invoke(table, attack_value, AbilityEffectTime.AfterLoadShield)
                        if attack_value >= shield.defence_value:
                            table.reccuringEffects.invoke(table, attack_value, AbilityEffectTime.BeforeShieldAttack)
                            attack_value -= shield.defence_value
                            table.reccuringEffects.invoke(table, attack_value, AbilityEffectTime.AfterShieldAttack)
                            shield.removeConsistency(1)
                            if shield.consistency_value <=0:
                                table.opposingPlayer.removeCardFromPlayerArea(shield.id, PlayerArea.Shields)
                                table.clearEffect(card)
                        else:
                            attack_value = 0
                    else:
                        print('Opponent does not load the shield. Full attack pass')
                        return attack_value
                else:
                    print('Opponent does not have the energy to load the shield. Full attack pass')
                    return attack_value

            else:
                if attack_value >= shield.defence_value:
                    table.reccuringEffects.invoke(table, attack_value, AbilityEffectTime.BeforeShieldAttack)
                    attack_value -= shield.defence_value
                    table.reccuringEffects.invoke(table, attack_value, AbilityEffectTime.AfterShieldAttack)
                    shield.removeConsistency(1)
                    if shield.consistency_value <=0:
                        table.opposingPlayer.removeCardFromPlayerArea(shield.id, PlayerArea.Shields)
                        table.clearEffect(card)
                else:
                    attack_value = 0

        return attack_value

    @staticmethod
    def talentAreaResolution(table, attack_value):
        # check if opposing player has any talents
        if len(table.opposingPlayer.playerArea[PlayerArea.Talents.value]) > 0:
            # hasFaceDownTalents = len(list(filter(lambda x : x.isFaceDown, opposingPlayer.playerArea[PlayerArea.Talents.value])))
            hasFaceDownTalents = table.opposingPlayer.hasCardsInPlayerArea(PlayerArea.Talents, True)
            if hasFaceDownTalents > 0:
                #if opponent has face down talents choose if  you want to reveal one
                revealTalent = input('Opposing Player has hidden talents do you want to reveal 1?(yes/no):')
                if revealTalent == 'yes':
                    whichTalent = input('Choose a talent to reveal (id):')
                    whichTalent = int(whichTalent)
                    talent = table.opposingPlayer.getCardFromPlayerArea(whichTalent, PlayerArea.Talents)
                    talent.isCardFaceDown(False)
                    if talent.ability:
                        if talent.ability.abilityEffectTime == AbilityEffectTime.Immediate:
                            abilityArgs = shield.ability.getArgsForAbility(table, shield, attack_value)
                            ActionResolver.invokeAbility(shield, abilityArgs)
                        else:
                            table.reccuringEffects.add(talent.ability)
                    # ActionResolver.handleAbility(table, talent)
                    if talent.trash_value <= attack_value:
                        #if you can trash it choose if you want
                        trashTalent = input('The trash cost of the talent card is {0}. Do you want to trash it? (yes/no)'.format(talent.trash_value))
                        if trashTalent == 'yes':
                            table.reccuringEffects.invoke(table, attack_value, AbilityEffectTime.BeforeTrashTalent)
                            attack_value = attack_value - talent.trash_value
                            table.opposingPlayer.removeCardFromPlayerArea(talent.id, PlayerArea.Talents)
                            table.clearEffect(talent)
                            table.reccuringEffects.invoke(table, attack_value, AbilityEffectTime.AfterTrashTalent)
                    else:
                        print('You cannot trash the talent')
            # if the opponent doesnt have any hidden talents check if you can trash any of the revealed
            canTrashTalents = len(list(filter(lambda x : x.trash_value <= attack_value and not x.isFaceDown, table.opposingPlayer.playerArea[PlayerArea.Talents.value])))
            if canTrashTalents > 0:
                trashTalent = input('Do you want to trash a talent ? (yes/no):')
                if trashTalent == 'yes':
                    talentToTrash = int(input('Choose a talent to trash (id):'))
                    talent = table.opposingPlayer.getCardFromPlayerArea(talentToTrash, PlayerArea.Talents)
                    table.reccuringEffects.invoke(table, attack_value, AbilityEffectTime.BeforeTrashTalent)
                    attack_value = attack_value - talent.trash_value
                    table.opposingPlayer.removeCardFromPlayerArea(talent.id, PlayerArea.Talents)
                    table.clearEffect(talent)
                    table.reccuringEffects.invoke(table, attack_value, AbilityEffectTime.AfterTrashTalent)

        return attack_value

    @staticmethod
    def invokeAbility(card, args):
        if isinstance(args, list):
            card.ability.invoke(*args)
        else:
            card.ability.invoke(args)

    @staticmethod
    def handleAbility(table, card):
        logger.info('handleAbility => card.ability.abilityEffectTime =>{0}'.format(card.ability.abilityEffectTime))
        if card.ability.abilityEffectTime == AbilityEffectTime.StartOfTurn:
            logger.info('handleAbility => adding card to startOfTurnEffects')
            table.startOfTurnEffects.add(card.ability)
        elif card.ability.abilityEffectTime == AbilityEffectTime.EndOfTurn:
            logger.info('handleAbility => adding card to endOfTurnEffects')
            table.endOfTurnEffects.add(card.ability)
        elif card.ability.abilityEffectTime == AbilityEffectTime.OnPlay and card.ability.abilityEffectType == AbilityEffectType.Reccuring:
            logger.info('handleAbility => adding card to reccuringEffects')
            table.reccuringEffects.add(card.ability)
        elif card.ability.abilityEffectTime == AbilityEffectTime.OnPlay and card.ability.abilityEffectType == AbilityEffectType.Immediate:
            logger.info('handleAbility => invoking ability')
            abilityArgs = card.ability.getArgsForAbility(table, card, None)
            ActionResolver.invokeAbility(card, abilityArgs)
