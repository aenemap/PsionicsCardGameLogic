class Card:

    def __init__(self, id, name, type, sub_type, energy_cost):
        self.id =id
        self.name = name
        self.type = type
        self.sub_type = sub_type,
        self.energy_cost = energy_cost

class ShieldCard(Card):

    def __init__(self, id, name, type, sub_type, energy_cost, consistency_value):
        Card.__init__(self, id, name, type, energy_cost, sub_type)
        self.consistency_value = consistency_value


class TalentCard(Card):
    def __init__(self, id, name, type, sub_type, energy_cost, trash_value):
        Card._init__(self, id, name, type, sub_type, energy_cost)
        self.trash_value = trash_value


class EventCard(Card):
    pass
