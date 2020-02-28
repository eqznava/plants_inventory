import uuid

class Plants:

    def __init__(self, quantity, name, sciname, typeplant, irrigation, season, pui=None):
        self.quantity = quantity
        self.name = name
        self.sciname = sciname
        self.typeplant = typeplant
        self.irrigation = irrigation
        self.season = season
        self.pui = pui or uuid.uuid4()


    def to_dict(self):
        return vars(self)


    @staticmethod
    def schema():
        return ['quantity', 'name', 'sciname', 'typeplant', 'irrigation', 'season', 'pui']
