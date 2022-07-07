from .base_entity import BaseEntity


electric_boiler_type = "brick:Electric_Boiler"
electric_boiler_definition = ("A closed, pressure vessel that uses electricity"
                              " for heating water or other fluids to supply"
                              " steam or hot water for heating, humidification,"
                              " or other applications.")

class ElectricBoiler(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        ElectricBoiler.entity_count += 1


    def __del__(self):
        ElectricBoiler.entity_count -= 1


    @staticmethod
    def get_entity_count():
        return ElectricBoiler.entity_count
