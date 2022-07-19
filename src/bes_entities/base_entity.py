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


    def add_relationship(self, ref_entity, relationship_type):

        '''
        # one to many relationship not possible using the same key under current
        # architecture of fiware; instead instantiate many to one relationships
        if relationship_type not in self.base_attributes:
            self.base_attributes[relationship_type] = {
                "type": "Relationship",
                "value": ref_entity
            }
        elif type(self.base_attributes[relationship_type]) == list:
            self.base_attributes[relationship_type].append({
                "type": "Relationship",
                "value": ref_entity
            })
        else:
            self.base_attributes[relationship_type] = [self.base_attributes[relationship_type],
                {
                    "type": "Relationship",
                    "value": ref_entity
                }
            ]
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

        # write id and type to ontology
        ttl_file_text = self.print_ontology_base_attributes(ttl_file_text)
        ttl_file_text = self.print_ontology_relationships(ttl_file_text)
        #ttl_file_text = (f'{ttl_file_text}\n\nebc:{self.short_id_ontology} a brick:Site;\n'
        #                 f'    skos:definition "{ontology_strings.site_definition}"')

        # write relationships of the entity to ontology
        '''
        for key in self.base_attributes:
            if ("type" in self.base_attributes[key]) and ("type" == "Relationship"):
                ref_entity_ontology_id = get_ontology_id_from_id(self.base_attributes[key]["value"])
                relationship_type = self.base_attributes[key]["type"]
                ttl_file_text = f'{ttl_file_text};\nbrick:{relationship_type} ebc:{ref_entity_ontology_id}'
        ttl_file_text = f'{ttl_file_text} .'
        '''

        return ttl_file_text
