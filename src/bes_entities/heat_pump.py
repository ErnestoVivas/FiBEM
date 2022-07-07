from .base_entity import BaseEntity

class HeatPump(BaseEntity):

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
