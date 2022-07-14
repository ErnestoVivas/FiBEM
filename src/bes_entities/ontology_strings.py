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
                        "(vapor-compression) cycle.")

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

def get_entity_strings(entity_type):
    if entity_type == 0:
        return heat_pump_type, heat_pump_definition
    elif entity_type == 1:
        return electric_boiler_type, electric_boiler_definition
    elif entity_type == 2:
        return natural_gas_boiler_type, natural_gas_boiler_definition
    elif entity_type == 3:
        return pump_type, pump_definition
    elif entity_type == 4:
        return radiator_type, radiator_definition
    else:
        return "No_type_defined", "No definition found"


def strip_prefix(entity_type_str):
    return entity_type_str.split(":")[-1]
