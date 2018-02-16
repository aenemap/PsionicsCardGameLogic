from Game.Card import *
from Game.Enums import *
from Game.AbilityPool import *
import uuid , random

cardPool = []
cardPool.append(ShieldCard(
    id=random.randint(1, 100),
    name='Shield1',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost=random.randint(1, 5),
    consistency_value=random.randint(1, 3),
    isFaceDown=True))

cardPool.append(ShieldCard(
    id=random.randint(1, 100),
    name='Shield2',
    type= CardType.Shield,
    sub_type=CardSubType.Absorbing,
    energy_cost=random.randint(1, 5),
    consistency_value=random.randint(1, 3),
    isFaceDown=True))

cardPool.append(ShieldCard(
    id=random.randint(1, 100),
    name='Shield3',
    type= CardType.Shield,
    sub_type=CardSubType.Basic,
    energy_cost=random.randint(1, 5),
    consistency_value=random.randint(1, 3),
    isFaceDown=True))

cardPool.append(ShieldCard(
    id=random.randint(1, 100),
    name='Shield4',
    type= CardType.Shield,
    sub_type=CardSubType.Mirror,
    energy_cost=random.randint(1, 5),
    consistency_value=random.randint(1, 3),
    isFaceDown=True))

# cardPool.append(TalentCard(
#     id=random.randint(1, 100),
#     name='Talent4',
#     type= CardType.Talent,
#     sub_type= '',
#     energy_cost=random.randint(1, 5),
#     trash_value=3,
#     isFaceDown=False))
#
# cardPool.append(TalentCard(
#     id=random.randint(1, 100),
#     name='Talent5',
#     type= CardType.Talent,
#     sub_type= '',
#     energy_cost=random.randint(1, 5),
#     trash_value=3,
#     isFaceDown=False))
#
# cardPool.append(TalentCard(
#     id=random.randint(1, 100),
#     name='Talent6',
#     type= CardType.Talent,
#     sub_type= '',
#     energy_cost=random.randint(1, 5),
#     trash_value=3,
#     isFaceDown=True))
#
# cardPool.append(TalentCard(
#     id=random.randint(1, 100),
#     name='Talent7',
#     type= CardType.Talent,
#     sub_type= '',
#     energy_cost=random.randint(1, 5),
#     trash_value=3,
#     isFaceDown=True))


newTalentCard = TalentCard(
    id=random.randint(1, 100),
    name='Talent5',
    type= CardType.Talent,
    sub_type= '',
    energy_cost=2,
    trash_value=3,
    isFaceDown=False)
newTalentCard.startOfTurnEffect = gainHealthAtStartOfRound
cardPool.append(newTalentCard)
