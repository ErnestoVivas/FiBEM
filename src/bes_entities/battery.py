from .base_entity import BaseEntity


class Battery(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        Battery.entity_count += 1

    @staticmethod
    def get_entity_count():
        return Battery.entity_count
