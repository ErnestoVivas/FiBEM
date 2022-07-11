from .base_entity import BaseEntity
from .device_attributes import power_attr


electric_boiler_type = "brick:Electric_Boiler"
electric_boiler_definition = ("A closed, pressure vessel that uses electricity"
                              " for heating water or other fluids to supply"
                              " steam or hot water for heating, humidification,"
                              " or other applications.")

class ElectricBoiler(BaseEntity):

    entity_count = 0

    def __init__(self, new_id, new_type):
        BaseEntity.__init__(self, new_id, new_type)
        self.setup_devices()
        ElectricBoiler.entity_count += 1


    @staticmethod
    def get_entity_count():
        return ElectricBoiler.entity_count


    def setup_devices(self):
        self.devices.append(
            {
                "device_id": "Heating_Coil",
                "entity_name": self.base_attributes["id"] + ":Heating_Coil",
                "entity_type": "brick:Electrical_Power_Sensor",
                "timezone": "Europe/Berlin",     # default value, can be set by user
                "protocol": "IoTA-JSON",
                "transport": "MQTT",
                "attributes": [
                    power_attr
                ],
                "static_attributes": [
                    {
                        "name": "refEntity",
                        "type": "Relationship",
                        "value": self.base_attributes["id"]
                    }
                ]
            }
        )
        # devices of an electric boiler: power in, heat out, efficiency
