from Game.Card import *
from Game.Enums import *
import uuid , random

cardPool = []
cardPool.append(ShieldCard(
    id=random.randint(1, 100),
    name='Shield1',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost=2,
    consistency_value=3))

cardPool.append(ShieldCard(
    id=random.randint(1, 100),
    name='Shield2',
    type= CardType.Shield,
    sub_type=CardSubType.Absorbing,
    energy_cost=2,
    consistency_value=3))

cardPool.append(ShieldCard(
    id=random.randint(1, 100),
    name='Shield3',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost=2,
    consistency_value=3))

cardPool.append(ShieldCard(
    id=random.randint(1, 100),
    name='Shield4',
    type= CardType.Shield,
    sub_type=CardSubType.Mirror,
    energy_cost=2,
    consistency_value=3))

cardPool.append(TalentCard(
    id=random.randint(1, 100),
    name='Talent4',
    type= CardType.Talent,
    sub_type= '',
    energy_cost=2,
    trash_value=3))

cardPool.append(TalentCard(
    id=random.randint(1, 100),
    name='Talent5',
    type= CardType.Talent,
    sub_type= '',
    energy_cost=2,
    trash_value=3))

cardPool.append(TalentCard(
    id=random.randint(1, 100),
    name='Talent6',
    type= CardType.Talent,
    sub_type= '',
    energy_cost=2,
    trash_value=3))

cardPool.append(TalentCard(
    id=random.randint(1, 100),
    name='Talent7',
    type= CardType.Talent,
    sub_type= '',
    energy_cost=2,
    trash_value=3))
