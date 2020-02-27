import uuid

class Plants:

    def __init__(self, quantity, name, scientific_name, type_of_plant, irrigation, season, pui=None):
        self.quantity = quantity
        self.name = name
        self.scientific_name = scientific_name
        self.type_of_plant = type_of_plant
        self.irrigation = irrigation
        self.season = season
        self.pui = pui or uuid.uuid4()

    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['quantity', 'name', 'scientific_name', 'type_of_plant', 'irrigation', 'season', 'pui']
