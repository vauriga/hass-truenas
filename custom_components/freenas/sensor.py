from homeassistant.const import CONF_NAME, TEMP_CELSIUS
from homeassistant.components.sensor import DEVICE_CLASS_TEMPERATURE
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_platform
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.util import slugify

from .pyfreenas.disk import (
    Disk,
    DiskType,
)
from typing import Callable, List

from . import (
    Controller,
    FreeNASSensor,
    FreeNASEntityType,
    FreeNASDiskEntity,
)
from .const import (
    DOMAIN,
)


async def async_setup_entry(
    hass: HomeAssistant, entry: dict, async_add_entities: Callable,
):
    """Set up the FreeNAS switches."""
    entities = _create_entities(hass, entry)
    async_add_entities(entities)

def _get_controller(hass: HomeAssistant, entry: dict) -> Controller:
    controller = hass.data[DOMAIN][entry.entry_id]["controller"]
    assert controller is not None
    return controller


def _create_entities(hass: HomeAssistant, entry: dict) -> List[Entity]:
    entities = []

    controller = _get_controller(hass, entry)
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]
    name = entry.data[CONF_NAME]

    for disk in controller.disks:
        entities.append(DiskTemperatureSensor(
            entry, name, disk, coordinator))

    return entities


class DiskTemperatureSensor(
    FreeNASDiskEntity, FreeNASSensor, Entity
):
    _disk: Disk

    def __init__(self, entry: dict, name: str, disk: Disk, coordinator: DataUpdateCoordinator) -> None:
        self._disk = disk
        super().__init__(entry, name, coordinator)

    @property
    def name(self) -> str:
        """Return the name of the disk."""
        assert self._disk is not None
        return f"{self._disk.name} Disk Temperature"

    @property
    def unique_id(self) -> str:
        assert self._disk is not None
        return slugify(
            f"{self._entry.unique_id}-{FreeNASEntityType.DISK.value}-{self._disk.name}_temperature_sensor",
        )

    @property
    def icon(self) -> str:
        """Return an icon for the disk."""
        return "mdi:thermometer"

    @property
    def device_class(self) -> str:
        return DEVICE_CLASS_TEMPERATURE

    @property
    def unit_of_measurement(self):
        return TEMP_CELSIUS

    def _get_state(self) -> int:
        """Returns the current temperature of the disk."""
        assert self._disk is not None
        return self._disk.temperature