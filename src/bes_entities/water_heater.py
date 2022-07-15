from .base_entity import BaseEntity


class WaterHeater(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        WaterHeater.entity_count += 1

    @staticmethod
    def get_entity_count():
        return WaterHeater.entity_count
