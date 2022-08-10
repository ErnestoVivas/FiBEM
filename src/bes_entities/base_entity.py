'''
BaseEntity is inherited by all other Entities and contains attributes and
functions that are part of all entities
'''

from bes_entities import ontology_strings


class BaseEntity():

    def __init__(self, new_id, new_type):
        self.short_id = ""                  # for display purposes
        self.short_id_ontology = ""         # for writing to ttl file
        self.base_attributes = {
            "id": new_id,
            "type": new_type,
            "ontology": {
                "value": "Brick",
                "type": "text",
            },
            "definition": {
                "value": ontology_strings.site_definition,
                "type": "text",
            }
        }
        self.devices = []
        self.set_short_id(new_id)
        self.setup_standard_devices()
        self.add_standard_attributes_to_devices()


    def set_short_id(self, new_id):
        splitted_id = new_id.split(":")
        if len(splitted_id) >= 2:
            if splitted_id[-1].isnumeric():
                self.short_id = f"{splitted_id[-2]}:{splitted_id[-1]}"
                self.short_id_ontology = f"{splitted_id[-2]}_{splitted_id[-1]}"
            else:
                self.short_id = splitted_id[-1]
                self.short_id_ontology = splitted_id[-1]
        else:
            self.short_id = new_id
            self.short_id_ontology = new_id


    def get_ontology_id_from_id(self, entity_id):
        ontology_id = ""
        splitted_id = entity_id.split(":")
        if len(splitted_id) >= 2:
            if splitted_id[-1].isnumeric():
                ontology_id = f"{splitted_id[-2]}_{splitted_id[-1]}"
            else:
                ontology_id = splitted_id[-1]
        else:
            ontology_id = entity_id
        return ontology_id


    def setup_standard_devices(self):
        pass


    def add_device(self, device_id, entity_name, entity_type, definition):
        self.devices.append({
                "device_id": device_id,
                "entity_name": entity_name,
                "entity_type": entity_type,
                "definition": {
                    "type": "text",
                    "value": definition
                }
        })


    def delete_device(self, device_index):
        del self.devices[device_index]


    def add_standard_attributes_to_devices(self):
        isPartOf = {
            "type": "Relationship",
            "value": self.base_attributes['id']
        }
        for device in self.devices:
            device["isPartOf"] = isPartOf
            device["timezone"] = "Europe/Berlin"     # default value, can be set by user
            device["protocol"] = "IoTA-JSON"
            device["transport"] = "MQTT"


    def add_relationship(self, ref_entity, relationship_type):

        '''
        one to many relationship not possible using the same key under current
        architecture of fiware; instead instantiate many to one relationships
        '''

        self.base_attributes.update({
            relationship_type: {
                "type": "Relationship",
                "value": ref_entity
            }
        })


    def print_ontology_base_attributes(self, ttl_file_text):
        ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a brick:Site;\n'
                         f'    skos:definition "{ontology_strings.site_definition}"')
        return ttl_file_text


    def print_ontology_relationships(self, ttl_file_text):
        for key in self.base_attributes:
            if ("type" in self.base_attributes[key]) and (self.base_attributes[key]["type"] == "Relationship"):
                ref_entity_ontology_id = self.get_ontology_id_from_id(self.base_attributes[key]["value"])
                relationship_type = key
                ttl_file_text = f'{ttl_file_text};\n    brick:{relationship_type} ebc:{ref_entity_ontology_id}'
        ttl_file_text = f'{ttl_file_text} .'
        return ttl_file_text


    def print_ontology(self, ttl_file_text):
        ttl_file_text = self.print_ontology_base_attributes(ttl_file_text)
        ttl_file_text = self.print_ontology_relationships(ttl_file_text)
        return ttl_file_text
