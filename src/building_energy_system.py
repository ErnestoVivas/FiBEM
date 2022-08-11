from bes_entities import base_entity
from bes_entities.equipment import heat_pump
from bes_entities.equipment import electric_boiler
from bes_entities.equipment import natural_gas_boiler
from bes_entities.equipment import cogeneration
from bes_entities.equipment import heat_exchanger
from bes_entities.equipment import pv_panel
from bes_entities.equipment import pvt_panel
from bes_entities.equipment import solar_thermal_collector
from bes_entities.equipment import water_heater
from bes_entities.equipment import water_distribution
from bes_entities.equipment import valve
from bes_entities.equipment import pump
from bes_entities.equipment import radiator
from bes_entities.equipment import battery
from bes_entities.system import hvac_system
from bes_entities.system import electrical_system
from bes_entities.system import water_system
from bes_entities.location import room
from bes_entities.location import building
from bes_entities.location import outside
from bes_entities import ontology_strings

import json


class BuildingEnergySystem():

    def __init__(self, bes_id):
        self.id = bes_id
        self.entities = []
        self.relationships = []
        self.entities.append(base_entity.BaseEntity(bes_id, "Site"))


    def add_entity(self, chosen_entity, entity_id):
        if chosen_entity == 0:
            self.entities.append(heat_pump.HeatPump(entity_id, "Heat_Pump"))
        elif chosen_entity == 1:
            self.entities.append(electric_boiler.ElectricBoiler(entity_id, "Electric_Boiler"))
        elif chosen_entity == 2:
            self.entities.append(natural_gas_boiler.NaturalGasBoiler(entity_id, "Natural_Gas_Boiler"))
        elif chosen_entity == 3:
            self.entities.append(cogeneration.Cogeneration(entity_id, "Cogeneration_Plant"))
        elif chosen_entity == 4:
            self.entities.append(heat_exchanger.HeatExchanger(entity_id, "Heat_Exchanger"))
        elif chosen_entity == 5:
            self.entities.append(pv_panel.PVPanel(entity_id, "PV_Panel"))
        elif chosen_entity == 6:
            self.entities.append(pvt_panel.PVTPanel(entity_id, "PVT_Panel"))
        elif chosen_entity == 7:
            self.entities.append(solar_thermal_collector.SolarThermalCollector(entity_id, "Solar_Thermal_Collector"))
        elif chosen_entity == 8:
            self.entities.append(water_heater.WaterHeater(entity_id, "Water_Heater"))
        elif chosen_entity == 9:
            self.entities.append(water_distribution.WaterDistribution(entity_id, "Water_Distribution"))
        elif chosen_entity == 10:
            self.entities.append(valve.Valve(entity_id, "Valve"))
        elif chosen_entity == 11:
            self.entities.append(pump.Pump(entity_id, "Pump"))
        elif chosen_entity == 12:
            self.entities.append(radiator.Radiator(entity_id, "Radiator"))
        elif chosen_entity == 13:
            self.entities.append(battery.Battery(entity_id, "Battery"))
        elif chosen_entity == 14:
            self.entities.append(hvac_system.HVACSystem(entity_id, "HVAC_System"))
        elif chosen_entity == 15:
            self.entities.append(electrical_system.ElectricalSystem(entity_id, "Electrical_System"))
        elif chosen_entity == 16:
            self.entities.append(water_system.WaterSystem(entity_id, "Water_System"))
        elif chosen_entity == 17:
            self.entities.append(room.Room(entity_id, "Room"))
        elif chosen_entity == 18:
            self.entities.append(building.Building(entity_id, "Building"))
        elif chosen_entity == 19:
            self.entities.append(outside.Outside(entity_id, "Outside"))


    def delete_entity(self, entity_index):
        deleted_entity_id = self.entities[entity_index].base_attributes["id"]

        # first: all references to the deleted entity must be deleted
        for entity in self.entities:
            key_to_delete = ""
            for key in entity.base_attributes:
                if ("value" in entity.base_attributes[key]) and (entity.base_attributes[key]["value"] == deleted_entity_id):
                    key_to_delete = key
                    break
            if key_to_delete:
                del entity.base_attributes[key_to_delete]

        # Delete all entries in global relationship list that hold the entity
        relationship_indices_to_delete = []
        i = 0
        for relationship in self.relationships:
            first_entity = relationship["first_entity"]
            ref_entity = relationship["ref_entity"]
            if(first_entity == entity_index) or (ref_entity == entity_index):
                relationship_indices_to_delete.append(i)
            i += 1
        for index in reversed(relationship_indices_to_delete):
            del self.relationships[index]

        # entities indices after deleted entity will shrink by 1: adjust relationships list
        for relationship in self.relationships:
            if relationship["first_entity"] > entity_index:
                relationship["first_entity"] -= 1
            if relationship["ref_entity"] > entity_index:
                relationship["ref_entity"] -= 1

        # finally: remove entity
        del self.entities[entity_index]


    def add_device(self, entity_index, device_id, entity_name, entity_type):
        device_definition = ontology_strings.device_definitions[entity_type]
        self.entities[entity_index].add_device(device_id, entity_name, entity_type, device_definition)
        self.entities[entity_index].add_standard_attributes_to_devices()


    def delete_device(self, entity_index, device_index):
        self.entities[entity_index].delete_device(device_index)


    def delete_relationship(self, relationship_index):

        # delete relationship attribute from correspondent entity
        first_entity = self.relationships[relationship_index]["first_entity"]
        relationship_type = self.relationships[relationship_index]["relationship_type"]
        del self.entities[first_entity].base_attributes[relationship_type]

        # remove relationship from global relationship list
        del self.relationships[relationship_index]


    def add_relationship(self, first_entity, ref_entity, relationship_type):
        ref_entity_id = self.entities[ref_entity].base_attributes["id"]
        self.entities[first_entity].add_relationship(ref_entity_id, relationship_type)
        self.relationships.append({
            "first_entity": first_entity,
            "ref_entity": ref_entity,
            "relationship_type": relationship_type
        })


    def print_json(self, json_file_name):
        entities_file_name = f"{json_file_name.rstrip('.json')}_entities.json"
        devices_file_name = f"{json_file_name.rstrip('.json')}_devices.json"
        entities_json_string = ""
        devices_json_string = ""
        for entity in self.entities:
            entities_json_string += f"{json.dumps(entity.base_attributes, indent=4)}\n"
            for device in entity.devices:
                devices_json_string += f"{json.dumps(device, indent=4)}\n"
        with open(entities_file_name, "w") as entities_file:
            entities_file.write(entities_json_string)
        with open(devices_file_name, "w") as devices_file:
            devices_file.write(devices_json_string)


    def print_ontology(self, ontology_file_name):
        ttl_file_text = ontology_strings.ontology_prefixes

        for entity in self.entities:
            ttl_file_text = entity.print_ontology(ttl_file_text)

        with open(ontology_file_name, "w") as ontology_file:
            ontology_file.write(ttl_file_text)


    def reset_bes(self):
        for i, entity in enumerate(self.entities):
            if hasattr(self.entities[i], "entity_count"):
                type(self.entities[i]).entity_count = 0
        self.entities.clear()
        self.relationships.clear()
        self.entities.append(base_entity.BaseEntity(self.id, "Site"))


    def reset_bes_new_id(self, new_bes_id):
        self.id = new_bes_id
        for i, entity in enumerate(self.entities):
            if hasattr(self.entities[i], "entity_count"):
                type(self.entities[i]).entity_count = 0
        self.entities.clear()
        self.relationships.clear()
        self.entities.append(base_entity.BaseEntity(new_bes_id, "Site"))


    def set_relationships_automatically(self):

        # delete all existing relationships
        while len(self.relationships) > 0:
            self.delete_relationship(len(self.relationships)-1)

        # count container and key entities
        hvac_system_count = [0, 0]
        electrical_system_count = [0, 0]
        water_system_count = [0, 0]
        building_count = [0, 0]
        water_heater_count = [0, 0]

        # connect entities to root entity
        for i, entity in enumerate(self.entities):
            if entity.base_attributes["type"] == "Outside":
                self.add_relationship(i, 0, "isPartOf")
            if entity.base_attributes["type"] == "Building":
                self.add_relationship(i, 0, "isPartOf")
                building_count[0] += 1
                building_count[1] = i
            if entity.base_attributes["type"] == "HVAC_System":
                hvac_system_count[0] += 1
                hvac_system_count[1] += i
            if entity.base_attributes["type"] == "Electrical_System":
                electrical_system_count[0] += 1
                electrical_system_count[1] += i
            if entity.base_attributes["type"] == "Water_System":
                water_system_count[0] += 1
                water_system_count[1] += i
            if entity.base_attributes["type"] == "Water_Heater":
                water_heater_count[0] += 1
                water_heater_count[1] += i

        # add rooms and systems to building if possible (not possible if there are multiple buildings)
        if building_count[0] == 1:
            for i, entity in enumerate(self.entities):
                if entity.base_attributes["type"] == "Room":
                    self.add_relationship(i, building_count[1], "hasLocation")
                if (entity.base_attributes["type"] == "HVAC_System") and (hvac_system_count[0] == 1):
                    self.add_relationship(i, building_count[1], "isPartOf")
                if (entity.base_attributes["type"] == "Water_System") and (water_system_count[0] == 1):
                    self.add_relationship(i, building_count[1], "isPartOf")
                if (entity.base_attributes["type"] == "Electrical_System") and (electrical_system_count[0] == 1):
                    self.add_relationship(i, building_count[1], "isPartOf")

        # connect systems directly to site if there is not a unique building
        else:
            for i, entity in enumerate(self.entities):
                if entity.base_attributes["type"] == "HVAC_System":
                    self.add_relationship(i, 0, "isPartOf")
                if entity.base_attributes["type"] == "Water_System":
                    self.add_relationship(i, 0, "isPartOf")
                if entity.base_attributes["type"] == "Electrical_System":
                    self.add_relationship(i, 0, "isPartOf")

        # connect equipment to hvac system (if there is only one...)
        if hvac_system_count[0] == 1:
            for i, entity in enumerate(self.entities):
                if entity.base_attributes["type"] == "Heat_Pump":
                    self.add_relationship(i, hvac_system_count[1], "isPartOf")
                if entity.base_attributes["type"] == "Cogeneration_Plant":
                    self.add_relationship(i, hvac_system_count[1], "isPartOf")
                if entity.base_attributes["type"] == "Electric_Boiler":
                    self.add_relationship(i, hvac_system_count[1], "isPartOf")
                if entity.base_attributes["type"] == "Natural_Gas_Boiler":
                    self.add_relationship(i, hvac_system_count[1], "isPartOf")
                if entity.base_attributes["type"] == "Solar_Thermal_Collector":
                    self.add_relationship(i, hvac_system_count[1], "isPartOf")
                if entity.base_attributes["type"] == "Radiator":
                    self.add_relationship(i, hvac_system_count[1], "isPartOf")
                if entity.base_attributes["type"] == "Water_Heater":
                    self.add_relationship(i, hvac_system_count[1], "isPartOf")

        # connect equipment to electrical system
        if electrical_system_count[0] == 1:
            for i, entity in enumerate(self.entities):
                if entity.base_attributes["type"] == "PV_Panel":
                    self.add_relationship(i, electrical_system_count[1], "isPartOf")
                if entity.base_attributes["type"] == "PVT_Panel":
                    self.add_relationship(i, electrical_system_count[1], "isPartOf")
                if entity.base_attributes["type"] == "Battery":
                    self.add_relationship(i, electrical_system_count[1], "isPartOf")

        # pair rooms with radiators
        for i, first_entity in enumerate(self.entities):
            for j, ref_entity in enumerate(self.entities):
                if (first_entity.base_attributes["type"] == "Radiator") and (ref_entity.base_attributes["type"] == "Room"):
                    first_entity_number = first_entity.base_attributes["id"].split(":")[-1]
                    ref_entity_number = ref_entity.base_attributes["id"].split(":")[-1]
                    if first_entity_number == ref_entity_number:
                        self.add_relationship(i, j, "hasLocation")
                        self.add_relationship(i, j, "feeds")

        # set feeds over water heater if possible
        if water_heater_count[0] == 1:
            for i, entity in enumerate(self.entities):
                if ((entity.base_attributes["type"] == "Heat_Pump") or
                    (entity.base_attributes["type"] == "Cogeneration_Plant") or
                    (entity.base_attributes["type"] == "Solar_Thermal_Collector") or
                    (entity.base_attributes["type"] == "PVT_Panel")):
                    self.add_relationship(i, water_heater_count[1], "feeds")
                if entity.base_attributes["type"] == "Radiator":
                    self.add_relationship(i, water_heater_count[1], "isFedBy")



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
            specific_entity_count = cogeneration.Cogeneration.get_entity_count()
        elif entity_type == 4:
            specific_entity_count = heat_exchanger.HeatExchanger.get_entity_count()
        elif entity_type == 5:
            specific_entity_count = pv_panel.PVPanel.get_entity_count()
        elif entity_type == 6:
            specific_entity_count = pvt_panel.PVTPanel.get_entity_count()
        elif entity_type == 7:
            specific_entity_count = solar_thermal_collector.SolarThermalCollector.get_entity_count()
        elif entity_type == 8:
            specific_entity_count = water_heater.WaterHeater.get_entity_count()
        elif entity_type == 9:
            specific_entity_count = water_distribution.WaterDistribution.get_entity_count()
        elif entity_type == 10:
            specific_entity_count = valve.Valve.get_entity_count()
        elif entity_type == 11:
            specific_entity_count = pump.Pump.get_entity_count()
        elif entity_type == 12:
            specific_entity_count = radiator.Radiator.get_entity_count()
        elif entity_type == 13:
            specific_entity_count = battery.Battery.get_entity_count()
        elif entity_type == 14:
            specific_entity_count = hvac_system.HVACSystem.get_entity_count()
        elif entity_type == 15:
            specific_entity_count = electrical_system.ElectricalSystem.get_entity_count()
        elif entity_type == 16:
            specific_entity_count = water_system.WaterSystem.get_entity_count()
        elif entity_type == 17:
            specific_entity_count = room.Room.get_entity_count()
        elif entity_type == 18:
            specific_entity_count = building.Building.get_entity_count()
        elif entity_type == 19:
            specific_entity_count = outside.Outside.get_entity_count()
        return specific_entity_count
