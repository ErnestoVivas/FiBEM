'''
    BaseEntity is inherited by all other Entities and contains attributes and
    functions that are part of all entities
'''

from bes_entities import ontology_strings

class BaseEntity():

    def __init__(self, new_id, new_type):
        self.short_id = ""                  # for display purposes
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
                self.short_id = splitted_id[-2] + ":" + splitted_id[-1]
            else:
                self.short_id = splitted_id[-1]
        else:
            self.short_id = new_id


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
