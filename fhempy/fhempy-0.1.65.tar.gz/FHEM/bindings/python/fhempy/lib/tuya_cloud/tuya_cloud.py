#!/usr/bin/env python3
"""Support for Tuya Smart devices."""

from functools import partial
import functools
from ..utils import utils
from .. import fhem
from ..generic import FhemModule

import itertools
from typing import Any

from tuya_iot import (
    ProjectType,
    TuyaDevice,
    TuyaDeviceListener,
    TuyaDeviceManager,
    TuyaHomeManager,
    TuyaOpenAPI,
    TuyaOpenMQ,
)

from .const import (
    CONF_ACCESS_ID,
    CONF_ACCESS_SECRET,
    CONF_APP_TYPE,
    CONF_COUNTRY_CODE,
    CONF_ENDPOINT,
    CONF_PASSWORD,
    CONF_PROJECT_TYPE,
    CONF_USERNAME,
    DOMAIN,
    TUYA_DEVICE_MANAGER,
    TUYA_DISCOVERY_NEW,
    TUYA_HA_DEVICES,
    TUYA_HA_TUYA_MAP,
    TUYA_MQTT_LISTENER,
    TUYA_SUPPORT_HA_TYPE,
    TUYA_SETUP_PLATFORM,
)


class tuya_cloud(FhemModule):
    def __init__(self, logger):
        super().__init__(logger)

    async def Define(self, hash, args, argsh):
        project_type = ProjectType(argsh[CONF_PROJECT_TYPE])
        api = TuyaOpenAPI(
            argsh[CONF_ENDPOINT],
            argsh[CONF_ACCESS_ID],
            argsh[CONF_ACCESS_SECRET],
            project_type,
        )

        api.set_dev_channel("hass")

        response = (
            await utils.run_blocking(
                functools.partial(api.login, argsh[CONF_USERNAME], argsh[CONF_PASSWORD])
            )
            if project_type == ProjectType.INDUSTY_SOLUTIONS
            else await utils.run_blocking(
                functools.partial(
                    api.login,
                    argsh[CONF_USERNAME],
                    argsh[CONF_PASSWORD],
                    argsh[CONF_COUNTRY_CODE],
                    argsh[CONF_APP_TYPE],
                )
            )
        )
        if response.get("success", False) is False:
            self.logger.error(
                "Tuya login error response: %s",
                response,
            )
            return False

        mq = TuyaOpenMQ(api)
        mq.start()

        device_manager = TuyaDeviceManager(api, mq)

        # Get device list
        home_manager = TuyaHomeManager(api, mq, device_manager)
        await utils.run_blocking(functools.partial(home_manager.updateDeviceCache))

        class DeviceListener(TuyaDeviceListener):
            def updateDevice(self, device: TuyaDevice):
                # TODO
                # get all tuya devices from FHEM
                # send update state to device with device.id
                for haDevice in hass.data[DOMAIN][TUYA_HA_DEVICES]:
                    if haDevice.tuya_device.id == device.id:
                        print("_update-->", self, ";->>", haDevice.tuya_device.status)
                        haDevice.schedule_update_ha_state()

            def addDevice(self, device: TuyaDevice):
                print("tuya device add-->", device)

                device_add = False

                print(
                    "add device category->",
                    device.category,
                    "; keys->",
                    hass.data[DOMAIN][TUYA_HA_TUYA_MAP].keys(),
                )
                if device.category in itertools.chain(
                    *hass.data[DOMAIN][TUYA_HA_TUYA_MAP].values()
                ):
                    map = hass.data[DOMAIN][TUYA_HA_TUYA_MAP]

                    remove_device(hass, device.id)

                    for key, list in map.items():
                        if device.category in list:
                            device_add = True
                            async_dispatcher_send(
                                hass, TUYA_DISCOVERY_NEW.format(key), [device.id]
                            )

                if device_add:
                    device_manager = hass.data[DOMAIN][TUYA_DEVICE_MANAGER]
                    device_manager.mq.stop()
                    mq = TuyaOpenMQ(device_manager.api)
                    mq.start()

                    device_manager.mq = mq
                    mq.add_message_listener(device_manager._onMessage)

            def removeDevice(self, id: str):
                print("tuya remove device:", id)
                remove_device(hass, id)

        __listener = DeviceListener()
        hass.data[DOMAIN][TUYA_MQTT_LISTENER] = __listener
        device_manager.addDeviceListener(__listener)
        hass.data[DOMAIN][TUYA_DEVICE_MANAGER] = device_manager

        # Clean up device entities
        await cleanup_device_registry(hass)

        print("domain key->", str(hass.data[DOMAIN][TUYA_HA_TUYA_MAP]))
        print("init support type->", TUYA_SUPPORT_HA_TYPE)

        for platform in TUYA_SUPPORT_HA_TYPE:
            print("tuya async platform-->", platform)
            hass.async_create_task(
                hass.config_entries.async_forward_entry_setup(entry, platform)
            )
            hass.data[DOMAIN][TUYA_SETUP_PLATFORM].add(platform)

        return True


async def cleanup_device_registry(hass: HomeAssistant):
    """Remove deleted device registry entry if there are no remaining entities."""

    device_registry = hass.helpers.device_registry.async_get(hass)
    device_manager = hass.data[DOMAIN][TUYA_DEVICE_MANAGER]

    for dev_id, device_entity in list(device_registry.devices.items()):
        for item in device_entity.identifiers:
            if DOMAIN == item[0] and item[1] not in device_manager.deviceMap.keys():
                device_registry.async_remove_device(dev_id)
                break


def remove_device(hass: HomeAssistant, device_id: str):
    """Remove device from hass cache."""
    device_registry = hass.helpers.device_registry.async_get(hass)
    entity_registry = hass.helpers.entity_registry.async_get(hass)
    for entity in list(entity_registry.entities.values()):
        if entity.unique_id.startswith(f"ty{device_id}"):
            entity_registry.async_remove(entity.entity_id)
            if device_registry.async_get(entity.device_id):
                device_registry.async_remove_device(entity.device_id)


async def async_setup(hass, config):
    """Set up the Tuya integration."""

    conf = config.get(DOMAIN)

    print("Tuya async setup conf %s \n" % conf)
    if conf is not None:

        async def flow_init() -> Any:
            try:
                result = await hass.config_entries.flow.async_init(
                    DOMAIN, context={"source": SOURCE_IMPORT}, data=conf
                )
            except Exception as inst:
                print(inst.args)
            print("Tuya async setup flow_init")
            return result

        hass.async_create_task(flow_init())

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unloading the Tuya platforms."""
    print("integration unload")
    unload = await hass.config_entries.async_unload_platforms(
        entry, hass.data[DOMAIN]["setup_platform"]
    )
    if unload:
        __device_manager = hass.data[DOMAIN][TUYA_DEVICE_MANAGER]
        __device_manager.mq.stop()
        __device_manager.removeDeviceListener(hass.data[DOMAIN][TUYA_MQTT_LISTENER])

        hass.data.pop(DOMAIN)

    return unload


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Async setup hass config entry."""
    print("tuya.__init__.async_setup_entry-->", entry.data)

    hass.data[DOMAIN] = {TUYA_HA_TUYA_MAP: {}, TUYA_HA_DEVICES: []}
    hass.data[DOMAIN][TUYA_SETUP_PLATFORM] = set()

    success = await _init_tuya_sdk(hass, entry)
    if not success:
        return False

    return True
