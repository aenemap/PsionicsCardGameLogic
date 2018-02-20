from Game.Card import *
from Game.Enums import *
from Game.AbilityPool import *
import uuid , random

cardPool = []
oblivion = ShieldCard(
    id=0,
    name='Oblivion',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost= 3,
    defence_value=2,
    consistency_value= 3,
    isFaceDown=True)
cardPool.append(oblivion)

barrage = ShieldCard(
    id=0,
    name='Barrage',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost= 2,
    defence_value=1,
    consistency_value= 2,
    isFaceDown=True)
cardPool.append(barrage)

colossus = ShieldCard(
    id=0,
    name='Colossus',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost= 4,
    defence_value=3,
    consistency_value= 3,
    isFaceDown=True)
cardPool.append(colossus)

doomWall = ShieldCard(
    id=0,
    name='Doom Wall',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost= 3,
    defence_value=3,
    consistency_value= 2,
    isFaceDown=True)
cardPool.append(doomWall)

nightbane = ShieldCard(
    id=0,
    name='Nightbane',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost= 0,
    defence_value=3,
    consistency_value= 0,
    isFaceDown=True)
nightbane.ability = NightBaneAbility(nightbane)
cardPool.append(nightbane)
