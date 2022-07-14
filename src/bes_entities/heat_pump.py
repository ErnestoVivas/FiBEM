from .base_entity import BaseEntity

class HeatPump(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        HeatPump.entity_count += 1

    @staticmethod
    def get_entity_count():
        return HeatPump.entity_count
