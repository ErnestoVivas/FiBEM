# This module contains all attributes (sensor/actuators) that can be part
# of the devices of the building energy system

from filip.models.ngsi_v2.iot import DeviceAttribute
from filip.models.base import DataType


temperature_attr = DeviceAttribute(
    name = "temperature",
    type = DataType.NUMBER,
    object_id = "T"
)

power_attr = {
    "name": "power",
    "type": "DataType.NUMBER",
    "object_id": "p"
}

'''
power_attr = DeviceAttribute(
    name = "power",
    type = DataType.NUMBER,
    object_id = "p"
)
'''

heat_flow_attr = DeviceAttribute(
    name = "heatFlow",
    type = DataType.NUMBER,
    object_id = "Q"
)

energy_conversion_efficiency_attr = DeviceAttribute(
    name = "energyConversionEfficiency",
    type = DataType.NUMBER,
    object_id = "ETA"
)
