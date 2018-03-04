from Game.Card import *
from Game.Enums import *
from Game.AbilityPool import *
import uuid , random, logging

logger = logging.getLogger(__name__)

logger.info('Creating the card pool')

cardPool = []

# oblivion = ShieldCard(
#     id=0,
#     name='Oblivion',
#     type= CardType.Shield,
#     subType=CardSubType.Basic,
#     energy_cost= 3,
#     consistency_value= 3,
#     isFaceDown=True)
# oblivion.defence_value = 2
# cardPool.append(oblivion)
#
# barrage = BasicShield(
#     id=0,
#     name='Barrage',
#     type= CardType.Shield,
#     subType=CardSubType.Basic,
#     energy_cost= 2,
#     consistency_value= 2,
#     isFaceDown=True)
# barrage.defence_value=1
# cardPool.append(barrage)
# #
colossus = AbsorbingShield(
    id=0,
    name='Colossus',
    type=CardType.Shield,
    subType=CardSubType.Absorbing,
    energy_cost= 4,
    consistency_value= 3,
    isFaceDown=True)
colossus.absorbing_value=3
cardPool.append(colossus)
#
# doomWall = ShieldCard(
#     id=0,
#     name='Doom Wall',
#     type= CardType.Shield,
#     subType=CardSubType.Basic,
#     energy_cost= 3,
#     consistency_value= 2,
#     isFaceDown=True)
# doomWall.defence_value=3
# cardPool.append(doomWall)
#
# nightbane = ShieldCard(
#     id=0,
#     name='Nightbane',
#     type= CardType.Shield,
#     subType=CardSubType.Basic,
#     energy_cost= 0,
#     consistency_value= 0,
#     isFaceDown=True)
# nightbane.defence_value=3
# nightbane.ability = NightBaneAbility(nightbane)
# cardPool.append(nightbane)
#
# behemoth = ShieldCard(
#     id=0,
#     name='Behemoth',
#     type= CardType.Shield,
#     subType=CardSubType.Absorbing,
#     energy_cost= 4,
#     consistency_value= 0,
#     isFaceDown=True)
# behemoth.absorbing_value = 3
# behemoth.ability = None
# cardPool.append(behemoth)
#
# ivory = ShieldCard(
#     id=0,
#     name='Ivory',
#     type= CardType.Shield,
#     subType=CardSubType.Mirror,
#     energy_cost= 4,
#     consistency_value= 3,
#     isFaceDown=True)
# ivory.defence_value = 2
# ivory.ability = IvoryAbility(ivory)
# cardPool.append(ivory)

echo = TalentCard(
    id=0,
    name='Echo',
    type= CardType.Talent,
    subType=None,
    energy_cost= 2,
    trash_value=2,
    isFaceDown=True
)
echo.ability = GainHealthAtEndOfTurn(echo, 1)
cardPool.append(echo)

# change = EventCard(
#     id=0,
#     name='Change',
#     type= CardType.Event,
#     subType=None,
#     energy_cost= 3
# )
# change.ability = ImmediateGainEnergy(change, 7)
# cardPool.append(change)
#
# lifeSource = EventCard(
#     id=0,
#     name='Life Source',
#     type= CardType.Event,
#     subType=None,
#     energy_cost= 0
# )
# lifeSource.ability = ImmediateGainHealth(lifeSource, 5)
# cardPool.append(lifeSource)

# testCard = TalentCard(
#     id=0,
#     name='testCard',
#     type= CardType.Talent,
#     subType=None,
#     energy_cost= 2,
#     trash_value=2,
#     isFaceDown=True
# )
# testCard.ability = WhenLoadsShieldGainEnergy(testCard, 2)
# cardPool.append(testCard)
Icarius = EventCard(
    id = 0,
    name = 'Icarius',
    type = CardType.Event,
    subType=None,
    energy_cost=3
)
Icarius.ability = IcariusAbility(Icarius)
cardPool.append(Icarius)
