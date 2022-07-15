from .base_entity import BaseEntity
import ontology_strings

class Battery(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.base_attributes["definition"]["value"] = ontology_strings.batter_definition
        Battery.entity_count += 1

    @staticmethod
    def get_entity_count():
        return Battery.entity_count
