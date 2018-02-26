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
    DrawCard = "1"
    PlayCard = "2"
    InitiateAttack = "3"
    Concentration = "4"
    Focus = "5"

class PlayerArea(Enum):
    Shields = "Shields"
    Talents = "Talents"
    DiscardPile = "DiscardPile"

class DrawCard(Enum):
    DrawFromTopOfDeck = 'DrawFromTopOfDeck'
    DrawFromBottomOfDeck = 'DrawFromBottomOfDeck'

class AbilityEffectType(Enum):
    Immediate = 'Immediate'
    Reccuring = 'Reccuring'
    Permanent = 'Permanent'

class AbilityEffectTime(Enum):
    OnPlay = 'OnPlay'
    StartOfTurn = 'StartOfTurn'
    EndOfTurn = 'EndOfTurn'
    BeforeLoadShield = 'BeforeLoadShield'
    AfterLoadShield = 'AfterLoadShield'
    BeforeShieldAttack = 'BeforeShieldAttack'
    AfterShieldAttack = 'AfterShieldAttack'
    BeforeLoadTalent = 'BeforeLoadTalent'
    AfterLoadTalent = 'AfterLoadTalent'
    BeforeTrashTalent = 'BeforeTrashTalent'
    AfterTrashTalent = 'AfterTrashTalent'

class AbilityArgType(Enum):
    CardOwner = 'CardOwner'
    CurrentPlayer = 'CurrentPlayer'
    OpposingPlayer = 'OpposingPlayer'
    BothPlayers = 'BothPlayers'
    Table = 'Table'
    Card = 'Card'
    AttackValue = 'AttackValue'

class ConsoleColors(Enum):
    Red   = "\033[1;31m"
    Blue  = "\033[1;34m"
    Cyan  = "\033[1;36m"
    Green = "\033[0;32m"
    Gray = "\033[0;37m]"
    Black = "\033[0;30m"
    Purple = "\033[0;35m"
    Brown = "\033[0;33m"
    DarkGray = "\033[1;30m"
    LightBlue = "\033[1;34m"
    LightGreen ="\033[1;32m"
    LightCyan ="\033[1;36m"
    LightRed = "\033[1;31m"
    LightPurple = "\033[1;35m"
    Yellow = "\033[1;33m"
    White = "\033[1;37m"
    Reset = "\033[0;0m"
    Bold    = "\033[;1m"
    Reverse = "\033[;7m"
