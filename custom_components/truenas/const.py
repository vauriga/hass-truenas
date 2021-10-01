"""Constants for the FreeNAS integration."""
import voluptuous as vol
from homeassistant.helpers import config_validation as cv

DOMAIN = "truenas"

ATTR_ENCRYPT = "Encrypted"
ATTR_POOL_GUID = "GUID"
ATTR_POOL_NAME = "Pool Name"

ATTR_DATASET_TYPE = "Dataset Type"
ATTR_DATASET_GUID = "GUID"
ATTR_DATASET_POOL = "Pool Name"
ATTR_DATASET_COMMENTS = "Comments"
ATTR_DATASET_USED_BYTTES = "Used Bytes"
ATTR_DATASET_AVAILABLE_BYTES = "Available Bytes"
ATTR_DATASET_TOTAL_BYTES = "Total Bytes"
ATTR_DATASET_COMPRESSION_RATIO = "Compression Ratio"

CONF_AUTH_MODE = "auth_mode"
CONF_AUTH_PASSWORD = "Username + Password"
CONF_AUTH_API_KEY = "API Key"

DEFAULT_SCAN_INTERVAL_SECONDS = 30

SERVICE_JAIL_START = "jail_start"
SCHEMA_SERVICE_JAIL_START = {}
SERVICE_JAIL_STOP = "jail_stop"
SCHEMA_SERVICE_JAIL_STOP = {
    vol.Optional("force"): cv.boolean,
}
SERVICE_JAIL_RESTART = "jail_restart"
SCHEMA_SERVICE_JAIL_RESTART = {}

SERVICE_VM_START = "vm_start"
SCHEMA_SERVICE_VM_START = {
    vol.Optional("overcommit"): cv.boolean,
}
SERVICE_VM_STOP = "vm_stop"
SCHEMA_SERVICE_VM_STOP = {
    vol.Optional("force"): cv.boolean,
}
SERVICE_VM_RESTART = "vm_restart"
SCHEMA_SERVICE_VM_RESTART = {}
