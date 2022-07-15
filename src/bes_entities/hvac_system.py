from .base_entity import BaseEntity


class HVACSystem(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        HVACSystem.entity_count += 1

    @staticmethod
    def get_entity_count():
        return HVACSystem.entity_count
