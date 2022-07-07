from bes_entities import base_entity
from bes_entities import heat_pump
from bes_entities import electric_boiler

class BuildingEnergySystem():

    def __init__(self, bes_id):
        self.id = bes_id
        self.entities = []
        self.entities.append(base_entity.BaseEntity(bes_id, "Site"))


    def add_entity(self, chosen_entity, entity_id):
        if chosen_entity == 0:
            pass
        elif chosen_entity == 1:
            self.entities.append(electric_boiler.ElectricBoiler(entity_id, "Electric_Boiler"))

    def delete_entity(self, entity_index):
        del self.entities[entity_index]
