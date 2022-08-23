# This module contains all attributes that can be part
# of the devices of the building energy system

from filip.models.ngsi_v2.iot import DeviceAttribute
from filip.models.base import DataType

dynamic_device_attributes = {
    "temperature_attr": {
        "name": "temperature",
        "type": "DataType.Number",
        "object_id": "T"
    },

    "volume_flow_attr": {
        "name": "volume_flow",
        "type": "DataType.Number",
        "object_id": "V_dot"
    },

    "power_attr": {
        "name": "power",
        "type": "DataType.NUMBER",
        "object_id": "P"
    },

    "pressure_attr": {
        "name": "pressure",
        "type": "DataType.Number",
        "object_id": "p"
    },

    "velocity_attr": {
        "name": "velocity",
        "type": "DataType.Number",
        "object_id": "v"
    },

    "angular_velocity_attr": {
        "name": "angular_velocity",
        "type": "DataType.Number",
        "object_id": "omega"
    },

    "percentage_attr": {
        "name": "percentage",
        "type": "DataType.Number",
        "object_id": "%"
    },

    "state_of_charge_attr": {
        "name": "state_of_charge",
        "type": "DataType.Number",
        "object_id": "SOC"
    }
}


'''
power_attr = DeviceAttribute(
    name = "power",
    type = DataType.NUMBER,
    object_id = "p"
)

temperature_attr = DeviceAttribute(
    name = "temperature",
    type = DataType.NUMBER,
    object_id = "T"
)
'''
