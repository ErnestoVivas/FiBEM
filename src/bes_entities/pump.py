from .base_entity import BaseEntity

class Pump(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        Pump.entity_count += 1

    @staticmethod
    def get_entity_count():
        return Pump.entity_count
