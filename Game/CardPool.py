from Game.Card import *
from Game.Enums import *
import uuid

cardPool = []
cardPool.append(ShieldCard(
    id=uuid.uuid4(),
    name='Shield1',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost=2,
    consistency_value=3))

cardPool.append(ShieldCard(
    id=uuid.uuid4(),
    name='Shield2',
    type= CardType.Shield,
    sub_type=CardSubType.Absorbing,
    energy_cost=2,
    consistency_value=3))

cardPool.append(ShieldCard(
    id=uuid.uuid4(),
    name='Shield3',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost=2,
    consistency_value=3))

cardPool.append(ShieldCard(
    id=uuid.uuid4(),
    name='Shield4',
    type= CardType.Shield,
    sub_type=CardSubType.Mirror,
    energy_cost=2,
    consistency_value=3))
