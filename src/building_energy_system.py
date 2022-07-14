from bes_entities import base_entity
from bes_entities import heat_pump
from bes_entities import electric_boiler
from bes_entities import natural_gas_boiler
from bes_entities import pump
from bes_entities import radiator


class BuildingEnergySystem():

    def __init__(self, bes_id):
        self.id = bes_id
        self.entities = []
        self.entities.append(base_entity.BaseEntity(bes_id, "Site"))


    def add_entity(self, chosen_entity, entity_id):
        if chosen_entity == 0:
            self.entities.append(heat_pump.HeatPump(entity_id, "Heat_Pump"))
        elif chosen_entity == 1:
            self.entities.append(electric_boiler.ElectricBoiler(entity_id, "Electric_Boiler"))
        elif chosen_entity == 2:
            self.entities.append(natural_gas_boiler.NaturalGasBoiler(entity_id, "Natural_Gas_Boiler"))
        elif chosen_entity == 3:
            self.entities.append(pump.Pump(entity_id, "Pump"))
        elif chosen_entity == 4:
            self.entities.append(radiator.Radiator(entity_id, "Radiator"))


    def delete_entity(self, entity_index):
        del self.entities[entity_index]


    def get_entity_count(self, entity_type):
        # this function returns the total amount of entites that have been
        # instantiated; if an entity was deleted, the count does not diminish
        # to avoid conflicts with ambiguous ids
        specific_entity_count = 0
        if entity_type == 0:
            specific_entity_count = heat_pump.HeatPump.get_entity_count()
        elif entity_type == 1:
            specific_entity_count = electric_boiler.ElectricBoiler.get_entity_count()
        elif entity_type == 2:
            specific_entity_count = natural_gas_boiler.NaturalGasBoiler.get_entity_count()
        elif entity_type == 3:
            specific_entity_count = pump.Pump.get_entity_count()
        elif entity_type == 4:
            specific_entity_count = radiator.Radiator.get_entity_count()
        return specific_entity_count
