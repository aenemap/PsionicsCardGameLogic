from enum import Enum

class CardType(Enum):
    Attack = 'Attack'
    Shield = 'Shield'
    Talent = 'Talent'
    Event = 'Event'

class CardSubType(Enum):
    Absorbing = 'Absorbing'
    Basic = 'Basic'
    Mirror = 'Mirror'
    Focus = 'Focus'
    Chaos = 'Chaos'

class TurnAction(Enum):
    Concentration = 'Concentration'
    PlayEvent = 'PlayEvent'
    InitiateAttack = 'InitiateAttack'
    DrawCard = 'DrawCard'
    DevelopTalent = 'DevelopTalent'
    Focus = 'Focus'
    CreateShield = 'CreateShield'
