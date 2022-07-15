'''
    BaseEntity is inherited by all other Entities and contains attributes and
    functions that are part of all entities
'''

from bes_entities import ontology_strings

class BaseEntity():

    def __init__(self, new_id, new_type):
        self.base_attributes = {
            "id": new_id,
            "type": new_type,
            "ontology": "brick",
            "definition": "sample"
        }
        self.devices = []


        #self.id: str = new_id
        #self.type: str = new_type   # if used is root, type is brick:Site
