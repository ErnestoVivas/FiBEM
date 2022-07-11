'''
    BaseEntity is inherited by all other Entities and contains attributes and
    functions that are part of all entities
'''

class BaseEntity():

    def __init__(self, new_id, new_type):

        self.base_attributes = {
            "id": new_id,
            "type": new_type,
        }


        #self.id: str = new_id
        #self.type: str = new_type   # if used is root, type is brick:Site