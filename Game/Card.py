class Card:

    def __init__(self, id, name, type, sub_type, cost):
        self.id =id
        self.name = name
        self.type = type
        self.sub_type = sub_type,
        self.cost = cost

class ShieldCard(Card):

    def __init__(self, id, name, type, sub_type, cost, constraction_value):
        Card.__init__(self, id, name, type, cost, sub_type)
        self.constraction_value = constraction_value


class TalentCard(Card):
    pass
