from Game.Enums import *
from Game.Ability import Ability

class ActionResolver(object):

    @staticmethod
    def resolveAction(table, action, currentPlayer, opposingPlayer, startOfTurnEffects, endOfTurnEffects):
        if action == TurnAction.DrawCard.value:
            #Draw the top card from the deck to players hand
            print('Player {0} choosed the {1} action'.format(currentPlayer.name, TurnAction.DrawCard))
            currentPlayer.hand.addCardToHand(currentPlayer.deck.drawCardFromDeck(DrawCard.DrawFromTopOfDeck))
        elif action == TurnAction.PlayCard.value:
            #Play the chosen card from the hand to the players play area (Shields, Talents ....)
            cardIdToPlay = input("Select card from Hand(id):")
            cardIdToPlay = int(cardIdToPlay)
            cardToPlay = currentPlayer.hand.getCardFromHand(cardIdToPlay)
            if cardToPlay:
                if not cardToPlay.isFaceDown:
                    currentPlayer.removeFromEnergyPool(cardToPlay.energy_cost)
                currentPlayer.playCard(cardToPlay)
                if cardToPlay.ability:
                    #set the reference of the card to the ability. Issue because of copies
                    cardToPlay.ability.attachedCard = cardToPlay
                    if not cardToPlay.isFaceDown:
                        ActionResolver.handleAbility(table, currentPlayer, opposingPlayer, cardToPlay)
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
            attack_value = ActionResolver.shieldAreaResolution(table, currentPlayer, opposingPlayer, attack_value)
            #if any attack pass the shield can be used to trash talents or attack the players health
            print('Remain Attack after Shield Area:', attack_value)
            if attack_value > 0:
                attack_value = ActionResolver.talentAreaResolution(table, currentPlayer, opposingPlayer, attack_value)

            print('Remain Attack after Talent Area:', attack_value)
            if attack_value > 0:
                # any remain attack goes to player
                print('Damage Opponent by {0}'.format(attack_value))
                opposingPlayer.takeDamage(attack_value)


    @staticmethod
    def shieldAreaResolution(table, currentPlayer, opposingPlayer, attack_value):
        #if the opposingPlayer has shields currentPlayer chooses the shield to attack
        if len(opposingPlayer.playerArea[PlayerArea.Shields.value]) > 0:
            shieldToAttack = input("Choose a shield to attack (id):")
            shieldToAttack = int(shieldToAttack)
            shield = opposingPlayer.getCardFromPlayerArea(shieldToAttack, PlayerArea.Shields)
            # substractFromAttackValue = None
            # if shield.sub_type == CardSubType.
            if shield.isFaceDown:
                # if the shield is face down the opposing players desides to load it or not if he has the energy
                if shield.energy_cost <= opposingPlayer.energy_pool:
                    opponentLoadsShield = input('Does opponents loads the shield?(yes/no):')
                    if (opponentLoadsShield == 'yes'):
                        opposingPlayer.removeFromEnergyPool(shield.energy_cost)
                        if shield.ability:
                            if shield.ability.abilityEffectType == AbilityEffectType.BeforeLoadShield:
                                abilityArgs = shield.ability.getArgsForAbility(table, currentPlayer, opposingPlayer, shield, attack_value)
                                ActionResolver.invokeAbility(shield, abilityArgs)
                        shield.isCardFaceDown(False)
                        # After Load Shield Abilities
                        if shield.ability:
                            if shield.ability.abilityEffectType == AbilityEffectType.AfterLoadShield:
                                abilityArgs = shield.ability.getArgsForAbility(table, currentPlayer, opposingPlayer, shield, attack_value)
                                ActionResolver.invokeAbility(shield, abilityArgs)
                        if attack_value >= shield.defence_value:
                            # WhenAttacked Abilities
                            if shield.ability:
                                if shield.ability.abilityEffectType == AbilityEffectType.WhenAttacked:
                                    abilityArgs = shield.ability.getArgsForAbility(table, currentPlayer, opposingPlayer, shield, attack_value)
                                    ActionResolver.invokeAbility(shield, abilityArgs)
                            attack_value -= shield.defence_value
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
                if attack_value >= shield.defence_value:
                    attack_value -= shield.defence_value
                    shield.removeConsistency(1)
                else:
                    attack_value = 0

        return attack_value

    @staticmethod
    def talentAreaResolution(table, currentPlayer, opposingPlayer, attack_value):
        # check if opposing player has any talents
        if len(opposingPlayer.playerArea[PlayerArea.Talents.value]) > 0:
            # hasFaceDownTalents = len(list(filter(lambda x : x.isFaceDown, opposingPlayer.playerArea[PlayerArea.Talents.value])))
            hasFaceDownTalents = opposingPlayer.hasCardsInPlayerArea(PlayerArea.Talents, True)
            if hasFaceDownTalents > 0:
                #if opponent has face down talents choose if  you want to reveal one
                revealTalent = input('Opposing Player has hidden talents do you want to reveal 1?:')
                if revealTalent == 'yes':
                    whichTalent = input('Choose a talent to reveal (id):')
                    whichTalent = int(whichTalent)
                    talent = opposingPlayer.getCardFromPlayerArea(whichTalent, PlayerArea.Talents)
                    talent.isCardFaceDown(False)
                    ActionResolver.handleAbility(table, currentPlayer, opposingPlayer, talent)
                    if talent.trash_value <= attack_value:
                        #if you can trash it choose if you want
                        trashTalent = input('The trash cost of the talent card is {0}. Do you want to trash it? (yes/no)'.format(talent.trash_value))
                        if trashTalent == 'yes':
                            attack_value = attack_value - talent.trash_value
                            opposingPlayer.removeCardFromPlayerArea(talent.id, PlayerArea.Talents)
                            ActionResolver.removeReccuringAbility(table, talent)
                    else:
                        print('You cannot trash the talent')
            # if the opponent doesnt have any hidden talents check if you can trash any of the revealed
            canTrashTalents = len(list(filter(lambda x : x.trash_value <= attack_value and not x.isFaceDown, opposingPlayer.playerArea[PlayerArea.Talents.value])))
            if canTrashTalents > 0:
                trashTalent = input('Do you want to trash a talent ? (yes/no):')
                if trashTalent == 'yes':
                    talentToTrash = int(input('Choose a talent to trash (id):'))
                    talent = opposingPlayer.getCardFromPlayerArea(talentToTrash, PlayerArea.Talents)
                    attack_value = attack_value - talent.trash_value
                    opposingPlayer.removeCardFromPlayerArea(talent.id, PlayerArea.Talents)
                    ActionResolver.removeReccuringAbility(table, talent)

        return attack_value

    @staticmethod
    def invokeAbility(card, args):
        if isinstance(args, list):
            card.ability.invoke(*args)
        else:
            card.ability.invoke(args)

    @staticmethod
    def removeReccuringAbility(table, card):
        effectList = []
        if card.ability:
            if card.ability.abilityEffectType == AbilityEffectType.StartOfTurn:
                effectList = table.startOfTurnEffects
            elif card.ability.abilityEffectType == AbilityEffectType.EndOfTurn:
                effectList = table.endOfTurnEffects
            if len(list(filter(lambda x : x.attachedCard.id == card.id, effectList))):
                abilityIndex = table.startOfTurnEffects.index(card.ability)
                if abilityIndex > -1:
                    effectList.pop(abilityIndex)

    @staticmethod
    def handleAbility(table, currentPlayer, opposingPlayer, card):
        print('inside handleAbility')
        if card.ability.abilityEffectType == AbilityEffectType.StartOfTurn:
            table.startOfTurnEffects.append(card.ability)
        elif card.ability.abilityEffectType == AbilityEffectType.EndOfTurn:
            table.endOfTurnEffects.append(card.ability)
        elif card.ability.abilityEffectType == AbilityEffectType.Immediate:
            abilityArgs = card.ability.getArgsForAbility(table, currentPlayer, opposingPlayer, card, None)
            ActionResolver.invokeAbility(card, abilityArgs)
