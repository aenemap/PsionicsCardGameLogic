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
