from .base_entity import BaseEntity


class Room(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        Room.entity_count += 1

    @staticmethod
    def get_entity_count():
        return Room.entity_count