ontology_prefixes = ("@prefix brick: <https://brickschema.org/schema/Brick#> .\n"
                     "@prefix bsh: <https://brickschema.org/schema/BrickShape#> .\n"
                     "@prefix dcterms: <http://purl.org/dc/terms#> .\n"
                     "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
                     "@prefix qudt: <http://qudt.org/schema/qudt/>.\n"
                     "@prefix qudtqk: <http://qudt.org/vocab/quantitykind/>.\n"
                     "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
                     "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
                     "@prefix sdo: <http://schema.org/>.\n"
                     "@prefix sh: <http://www.w3.org/ns/shacl#> .\n"
                     "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n"
                     "@prefix sosa: <http://www.w3.org/ns/sosa/> .\n"
                     "@prefix tag: <https://brickschema.org/schema/BrickTag#> .\n"
                     "@prefix unit: <http://qudt.org/vocab/unit/>.\n"
                     "@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .\n"
                     "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n"
                     "@prefix ebc: <https://www.ebc.eonerc.rwth-aachen.de/cms/~dmzz/E-ON-ERC-EBC/#> .\n")

heat_pump_type = "ebc:Heat_Pump"
heat_pump_definition = ("A device that transfers heat between spaces with the "
                        "use of electrical energy, based on the refrigeration "
                        "[vapor-compression] cycle.")

electric_boiler_type = "brick:Electric_Boiler"
electric_boiler_definition = ("A closed, pressure vessel that uses electricity"
                              " for heating water or other fluids to supply"
                              " steam or hot water for heating, humidification,"
                              " or other applications.")
natural_gas_boiler_type = "brick:Natural_Gas_Boiler"
natural_gas_boiler_definition = ("A closed, pressure vessel that uses natural "
                                 "gas for heating water or other fluids to "
                                 "supply steam or hot water for heating, "
                                 "humidification, or other applications.")

pump_type = "brick:Pump"
pump_definition = ("Machine for imparting energy to a fluid, causing it to do "
                   "work, drawing a fluid into itself through an entrance port, "
                   "and forcing the fluid out through an exhaust port.")

radiator_type = "brick:Radiator"
radiator_definition = ("Heat exchangers designed to transfer thermal energy "
                       "from one medium to another.")

cogeneration_plant_type = "ebc:Cogeneration_Plant"
cogeneration_plant_definition = ("A Cogeneration or combined heat and power "
                                 "plant is a machine that uses a heat engine "
                                 "to generate both electrical power and useful "
                                 "heat at the same time.")

heat_exchanger_type = "brick:Heat_Exchanger"
heat_exchanger_definition = ("A heat exchanger is a piece of equipment built "
                             "for efficient heat transfer from one medium to "
                             "another. The media may be separated by a solid "
                             "wall to prevent mixing or they may be in direct "
                             "contact [BEDES].")

pv_panel_type = "brick:PV_Panel"
pv_panel_definition = ("An integrated assembly of interconnected photovoltaic "
                       "cells designed to deliver a selected level of working "
                       "voltage and current at its output terminals packaged "
                       "for protection against environment degradation and "
                       "suited for incorporation in photovoltaic power systems.")

pvt_panel_type = "brick:PVT_Panel"
pvt_panel_definition = ("A type of solar panels that convert solar radiation "
                        "into usable thermal and electrical energy.")

solar_thermal_collector_type = "brick:Solar_Thermal_Collector"
solar_thermal_collector_definition = ("A type of solar panels that converts "
                                      "solar radiation into thermal energy.")

water_heater_type = "brick:Water_Heater"
water_heater_definition = ("An apparatus for heating and usually storing hot water.")

water_distribution_type = "brick:Water_Distribution"
water_distribution_definition = ("Utilize a water distribution source to "
                                 "represent how water is distributed across "
                                 "multiple destinations [pipes].")

valve_type = "brick:Valve"
valve_definition = ("A device that regulates, directs or controls the flow of "
                    "a fluid by opening, closing or partially obstructing "
                    "various passageways.")

battery_type = "brick:Battery"
battery_definition = ("A container that stores chemical energy that can be "
                      "converted into electricity and used as a source of power.")

hvac_system_type = "brick:HVAC_System"
hvac_system_definition = ("The equipment, distribution systems and terminals "
                          "that provide, either collectively or individually, "
                          "the processes of heating, ventilating or air "
                          "conditioning to a building or portion of a building.")

electrical_system_type = "brick:Electrical_System"
electrical_system_definition = ("Devices that serve or are part of the "
                                "electrical subsystem in the building.")

water_system_type = "brick:Water_System"
water_system_definition = ("The equipment, devices and conduits that handle the "
                           "production and distribution of water in a building.")

room_type = "brick:Room"
room_definition = "Base class for all more specific room types."

building_type = "brick:Building"
building_definition = ("An independent unit of the built environment with a "
                       "characteristic spatial structure, intended to serve at "
                       "least one function or user activity [ISO 12006-2:2013], "
                       "a structure wholly or partially enclosed within "
                       "exterior walls, or within exterior and party walls, "
                       "and a roof, affording shelter to persons, animals, or "
                       "property.")

outside_type = "brick:Outside"
outside_definition = ("Entity that describes the weather and outside environment "
                      "of the location of the considered site or building.")

site_type = "brick:Site"
site_definition = ("A geographic region containing 0 or more buildings. "
                   "Typically used as the encapsulating location for a "
                   "collection of Brick entities through the hasSite/isSiteOf "
                   "relationships.")

entity_strings_by_value = {
    "0": [heat_pump_type, heat_pump_definition],
    "1": [electric_boiler_type, electric_boiler_definition],
    "2": [natural_gas_boiler_type, natural_gas_boiler_definition],
    "3": [cogeneration_plant_type, cogeneration_plant_definition],
    "4": [heat_exchanger_type, heat_exchanger_definition],
    "5": [pv_panel_type, pv_panel_definition],
    "6": [pvt_panel_type, pvt_panel_definition],
    "7": [solar_thermal_collector_type, solar_thermal_collector_definition],
    "8": [water_heater_type, water_heater_definition],
    "9": [water_distribution_type, water_distribution_definition],
    "10": [valve_type, valve_definition],
    "11": [pump_type, pump_definition],
    "12": [radiator_type, radiator_definition],
    "13": [battery_type, battery_definition],
    "14": [hvac_system_type, hvac_system_definition],
    "15": [electrical_system_type, electrical_system_definition],
    "16": [water_system_type, water_system_definition],
    "17": [room_type, room_definition],
    "18": [building_type, building_definition],
    "19": [outside_type, outside_definition]
}


def get_entity_strings(entity_type):
    if (entity_type >= 0) and (entity_type < 20):
        return entity_strings_by_value[str(entity_type)][0], entity_strings_by_value[str(entity_type)][1]
    else:
        return "No_type_defined", "No definition found"


def strip_prefix(entity_type_str):
    return entity_type_str.split(":")[-1]
