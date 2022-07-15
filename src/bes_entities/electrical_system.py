from .base_entity import BaseEntity


class ElectricalSystem(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        ElectricalSystem.entity_count += 1

    @staticmethod
    def get_entity_count():
        return ElectricalSystem.entity_count
