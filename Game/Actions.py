from Game.Enums import *
import logging

logger = logging.getLogger(__name__)

class DrawCardAction(object):
    def __init__(self):
        pass

    def drawCard(self, player, fromWhere):
        player.hand.addCardToHand(player.deck.drawCardFromDeck(fromWhere))

class PlayCardAction(object):
    def __init__(self):
        pass

    def playCard(self, table, actionResolver):
        logger.info('Player {0} chose the {1} action'.format(table.currentPlayer.name, TurnAction.PlayCard))
        cardIdToPlay = input("Select card from Hand(id):")
        cardIdToPlay = int(cardIdToPlay)
        cardToPlay = table.currentPlayer.hand.getCardFromHand(cardIdToPlay)
        print('cardToPlay => ', cardToPlay)
        logger.info('Player chose the {} card to play'.format(cardToPlay.name))
        cardToPlay.logCard(cardToPlay)
        if cardToPlay:
            if not cardToPlay.isFaceDown:
                table.currentPlayer.removeFromEnergyPool(cardToPlay.energy_cost)
            table.currentPlayer.playCard(cardToPlay)
            if len(cardToPlay.abilities) > 0:
                if not cardToPlay.isFaceDown:
                    logger.info('Calling handleAbility from play Card')
                    actionResolver.handleAbility(table, cardToPlay)
        else:
            print('Card with id {0} could not be found in Hand', cardIdToPlay)

class ConcentrationAction(object):
    def __init__(self):
        pass

    def concentration(self, currentPlayer):
        logger.info('Player {0} chose the {1} action'.format(currentPlayer.name, TurnAction.Concentration))
        currentPlayer.addToEnergyPool(1)

class InitiateAttackAction(object):
    def __init__(self):
        pass

    def initiateAttack(self, table, handleAbility):
        #The amount will be substracted from his energy_pool
        logger.info('Player {0} chose the {1} action'.format(table.currentPlayer.name, TurnAction.InitiateAttack))
        if table.attack_value == 0:
            table.attack_value = int(input("How much energy to spend for the attack:"))
            logger.info('Player Initiate Attack with an attack value of {0}'.format(table.attack_value))
        table.currentPlayer.removeFromEnergyPool(table.attack_value)
        table.attack_value = self.shieldAreaResolution(table)
        #if any attack pass the shield can be used to trash talents or attack the players health
        print('Remain Attack after Shield Area:', table.attack_value)
        logger.info('Remain Attack after Shield Area:{0}'.format(table.attack_value))
        if table.attack_value > 0:
            table.attack_value = self.talentAreaResolution(table)

        print('Remain Attack after Talent Area:', table.attack_value)
        logger.info('Remain Attack after Talent Area:{0}'.format(table.attack_value))

        # any remain attack goes to player
        print('Damage Opponent by {0}'.format(table.attack_value))
        logger.info('Damage Opponent by {0}'.format(table.attack_value))
        table.opposingPlayer.takeDamage(table.attack_value)
        table.gameEffects.invoke(
            table=table,
            abilityEffectTime = AbilityEffectTime.OnSuccessfulAttack,
            abilityEffectType = None,
            targetCard = shield
        )

    def shieldAreaResolution(self, table):
        #if the opposingPlayer has shields currentPlayer chooses the shield to attack
        if len(table.opposingPlayer.playerArea[PlayerArea.Shields.value]) > 0:
            shieldToAttack = input("Choose a shield to attack (id):")
            shieldToAttack = int(shieldToAttack)
            shield = table.opposingPlayer.getCardFromPlayerArea(shieldToAttack, PlayerArea.Shields)
            shield.logCard(shield)
            # substractFromAttackValue = None
            # if shield.subType == CardSubType.
            if shield.isFaceDown:
                # if the shield is face down the opposing players desides to load it or not if he has the energy
                if shield.energy_cost <= table.opposingPlayer.energy_pool:
                    opponentLoadsShield = input('Does opponents loads the shield?(yes/no):')
                    if (opponentLoadsShield == 'yes'):
                        table.opposingPlayer.removeFromEnergyPool(shield.energy_cost)
                        if len(shield.abilities) > 0:
                            for ability in shield.abilities:
                                logger.info('Shield {0} has ability'.format(shield.name))
                                logger.info('Adding ability to gameEffects')
                                logger.info('Calling handleAbility from shieldAreaResolution')
                                handleAbility(table, shield)
                        logger.info('Invoking GameEffects for BeforeLoadShield')
                        table.gameEffects.invoke(
                            table=table,
                            abilityEffectTime = AbilityEffectTime.BeforeLoadShield,
                            abilityEffectType = None,
                            targetCard = shield
                        )
                        shield.isCardFaceDown(False)
                        logger.info('Invoking GameEffects for AfterLoadShield')
                        table.gameEffects.invoke(
                            table=table,
                            abilityEffectTime = AbilityEffectTime.AfterLoadShield,
                            abilityEffectType = None,
                            targetCard = shield
                        )
                        spendAttackValue = shield.defence_value if shield.subType[0] == CardSubType.Basic else shield.absorbing_value

                        logger.info('spendAttackValue:{0}'.format(spendAttackValue))
                        if table.attack_value >= spendAttackValue:
                            logger.info('Invoking GameEffects for BeforeShieldAttack')
                            table.gameEffects.invoke(
                                table=table,
                                abilityEffectTime = AbilityEffectTime.BeforeShieldAttack,
                                abilityEffectType = None,
                                targetCard = shield
                            )
                            if shield.subType[0] == CardSubType.Basic:
                                logger.info('Inside basic shield')
                                table.attack_value -= spendAttackValue
                            elif shield.subType[0] == CardSubType.Absorbing:
                                logger.info('Inside absorbing shield')
                                table.attack_value -= spendAttackValue
                                shield.isLoadedWithEnergy = True
                            logger.info('Invoking GameEffects for AfterShieldAttack')
                            table.gameEffects.invoke(
                                table=table,
                                abilityEffectTime = AbilityEffectTime.AfterShieldAttack,
                                abilityEffectType = None,
                                targetCard = shield
                            )
                            shield.removeConsistency(1)
                            if shield.consistency_value <=0:
                                table.opposingPlayer.removeCardFromPlayerArea(shield.id, PlayerArea.Shields)
                                table.clearEffect(shield)
                        else:
                            table.attack_value = 0
                    else:
                        print('Opponent does not load the shield. Full attack pass')
                        return table.attack_value
                else:
                    print('Opponent does not have the energy to load the shield. Full attack pass')
                    return table.attack_value

            else:
                if table.attack_value >= shield.defence_value:
                    logger.info('Invoking GameEffects for BeforeShieldAttack')
                    table.gameEffects.invoke(
                        table=table,
                        abilityEffectTime = AbilityEffectTime.BeforeShieldAttack,
                        abilityEffectType = None,
                        targetCard = shield
                    )
                    table.attack_value -= shield.defence_value
                    logger.info('Invoking GameEffects for AfterShieldAttack')
                    table.gameEffects.invoke(
                        table=table,
                        abilityEffectTime = AbilityEffectTime.AfterShieldAttack,
                        abilityEffectType = None,
                        targetCard = shield
                    )
                    shield.removeConsistency(1)
                    if shield.consistency_value <=0:
                        table.opposingPlayer.removeCardFromPlayerArea(shield.id, PlayerArea.Shields)
                        table.clearEffect(shield)
                else:
                    table.attack_value = 0

        return table.attack_value


    def talentAreaResolution(self, table):
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
                    if talent.trash_value <= table.attack_value:
                        #if you can trash it choose if you want
                        trashTalent = input('The trash cost of the talent card is {0}. Do you want to trash it? (yes/no)'.format(talent.trash_value))
                        if trashTalent == 'yes':
                            logger.info('Invoking GameEffects for BeforeTrashTalent')
                            table.gameEffects.invoke(
                                table=table,
                                abilityEffectTime = AbilityEffectTime.BeforeTrashTalent,
                                abilityEffectType = None,
                                targetCard = talent
                            )
                            table.attack_value = table.attack_value - talent.trash_value
                            table.opposingPlayer.removeCardFromPlayerArea(talent.id, PlayerArea.Talents)
                            table.clearEffect(talent)
                            logger.info('Invoking GameEffects for AfterTrashTalent')
                            table.gameEffects.invoke(
                                table=table,
                                abilityEffectTime = AbilityEffectTime.AfterTrashTalent,
                                abilityEffectType = None,
                                targetCard = talent
                            )
                        else:
                            talent.isCardFaceDown(True)
                    else:
                        print('You cannot trash the talent')
            # if the opponent doesnt have any hidden talents check if you can trash any of the revealed
            canTrashTalents = len(list(filter(lambda x : x.trash_value <= table.attack_value and not x.isFaceDown, table.opposingPlayer.playerArea[PlayerArea.Talents.value])))
            if canTrashTalents > 0:
                trashTalent = input('Do you want to trash a talent ? (yes/no):')
                if trashTalent == 'yes':
                    talentToTrash = int(input('Choose a talent to trash (id):'))
                    talent = table.opposingPlayer.getCardFromPlayerArea(talentToTrash, PlayerArea.Talents)
                    logger.info('Invoking GameEffects for BeforeTrashTalent')
                    table.gameEffects.invoke(
                        table=table,
                        abilityEffectTime = AbilityEffectTime.BeforeTrashTalent,
                        abilityEffectType = None,
                        targetCard = talent
                    )
                    table.attack_value = table.attack_value - talent.trash_value
                    table.opposingPlayer.removeCardFromPlayerArea(talent.id, PlayerArea.Talents)
                    table.clearEffect(talent)
                    logger.info('Invoking GameEffects for AfterTrashTalent')
                    table.gameEffects.invoke(
                        table=table,
                        abilityEffectTime = AbilityEffectTime.BeforeTrashTalent,
                        abilityEffectType = None,
                        targetCard = talent
                    )


        return table.attack_value
