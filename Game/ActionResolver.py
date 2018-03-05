from Game.Enums import *
from Game.Ability import Ability
from Game.Actions import *
from Game.Card import *
import logging

logger = logging.getLogger(__name__)

class ActionResolver(object):

    def __init__(self):
        pass

    def resolveAction(self,table, action):
        drawCardAction = DrawCardAction()
        playCardAction = PlayCardAction()
        concentrationAction = ConcentrationAction()
        initateAttackAction = InitiateAttackAction()
        if action == TurnAction.DrawCard.value:
            #Draw the top card from the deck to players hand
            logger.info('Player {0} chose the {1} action'.format(table.currentPlayer.name, TurnAction.DrawCard))
            print('Player {0} choosed the {1} action'.format(table.currentPlayer.name, TurnAction.DrawCard))
            # table.currentPlayer.hand.addCardToHand(table.currentPlayer.deck.drawCardFromDeck(DrawCard.DrawFromTopOfDeck))
            drawCardAction.drawCard(table.currentPlayer, DrawCard.DrawFromTopOfDeck)
        elif action == TurnAction.PlayCard.value:
            playCardAction.playCard(table, self)
        elif action == TurnAction.Concentration.value:
            #Player gains 1 energy to his energy pool
            concentrationAction.concentration(table.currentPlayer)
        elif action == TurnAction.InitiateAttack.value:
            #Player Initiates attack and he choses the amount of the attack
            initateAttackAction.initiateAttack(table, self.handleAbility)


    # def invokeAbility(self, card, args):
    #     if isinstance(args, list):
    #         card.ability.invoke(*args)
    #     else:
    #         card.ability.invoke(args)


    def handleAbility(self, table, card):
        logger.info('handleAbility => card.abilities =>{0}'.format(card.abilities))
        logger.info('Adding effects to gameEffects pool')
        for ability in card.abilities:
            ability.attachedCard = card
            table.gameEffects.add(ability)
        logger.info('handleAbility => gameEffects => {0}'.format(table.gameEffects))
        logger.info('Calling gameEffects.invoke')
        table.gameEffects.invoke(
            table=table,
            abilityEffectTime = AbilityEffectTime.OnPlay,
            abilityEffectType = AbilityEffectType.Immediate,
            targetCard = None
        )
