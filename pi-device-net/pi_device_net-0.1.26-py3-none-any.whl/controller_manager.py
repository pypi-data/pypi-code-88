# Copyright (c) 2021 Edwin Wise
# MIT License
# See LICENSE for details
"""
    PiDeviceNet Controller Manager. High level framework to deal with module
    connection management.
"""
import json
import logging

import pygame
from pi_touch_gui import Page

from pi_device_net import (ControlNetwork, ControllerPingMsg, Command,
                           ControllerDetachMsg)

LOG = logging.getLogger(__name__)


class ControllerManager:
    """ Manage the high-level module interactions.

    Expects pygame.init() to have already been called.
    """

    def __init(self, module_timeout, discovery_delay, network_name,
               known_functions, module_change_func):
        """
        Parameters
        ----------
        module_timeout : Number
            How long we wait for a module message before we disconnect
        discovery_delay : Number
            How many seconds between module discovery attempts
        network_name : String
            Name of the network as a whole
        known_functions : Dictionary
            Registry of known page-support functions
        module_change_func : Callable[]
            Method that is called when a module is added or removed, to reset
            anything that needs adjusting.
        """
        self.module_timeout = module_timeout
        self.discovery_delay = discovery_delay
        self.network_name = network_name
        self.known_functions = known_functions
        self.module_change_func = module_change_func

        self.known_modules = {}
        self.known_pages = {}
        self.module_pages = {}
        self.module_data = {}

        now = pygame.time.get_ticks() // 1000
        self.ping_time = now
        self.last_discovery_time = now
        self.last_refresh_time = now

        self.network = ControlNetwork(self.network_name, self.handle_messages)

    def on_refresh(self, gui, page):
        """ Method tied into the GUI frame refresh
        """
        now = pygame.time.get_ticks() // 1000

        if now == self.last_refresh_time:
            # Limit to only one refresh per second
            return
        self.last_refresh_time = now

        # Find new modules every 10 seconds
        if now - self.last_discovery_time > self.discovery_delay:
            self.network.discover()
            self.last_discovery_time = now

        # Clean stale modules
        stale_module = []
        for module_name, data in self.known_modules.items():
            delta_time = now - data.get('timestamp', 0)
            if delta_time > self.module_timeout:
                stale_module.append((module_name, delta_time))
        for module_name, delta_time in stale_module:
            LOG.warning(f"Module {module_name} has not updated in "
                        f"{int(delta_time)} seconds; detaching.")
            self.remove_module(module_name)

        # Ping known modules every refresh
        for module_name in self.known_modules.keys():
            topic_path = f"{self.network_name}/{module_name}/admin"
            message_data = ControllerPingMsg(module=module_name)
            self.network.publish(topic_path, message_data)

    def handle_messages(self, module, topic, msg):
        if topic == 'admin':
            cmd = msg['command']
            if cmd == Command.ATTACH.value:
                if module not in self.known_modules:
                    self.add_module(module, msg)
            elif cmd == Command.DETACH.value:
                if module in self.known_modules:
                    self.remove_module(module)
            elif cmd == Command.PING.value:
                pass
            else:
                LOG.info(f"Unknown message for {module!r} : {topic!r} "
                         f"=> {json.dumps(msg, sort_keys=True)[:60]}")
        elif topic == 'data':
            cmd = msg['command']
            if cmd == Command.WIDGET.value:
                if module not in self.module_data:
                    self.module_data[module] = {}
                module_data = self.module_data[module]
                module_data.update(msg['data'])
            else:
                LOG.info(f"Unknown message for {module!r} : {topic!r} "
                         f"=> {json.dumps(msg, sort_keys=True)[:60]}")

        else:
            LOG.info(f"Unknown topic for {module!r}: {topic!r}")

        if module in self.known_modules:
            module_data = self.known_modules[module]
            now = pygame.time.get_ticks() // 1000
            module_data['timestamp'] = now

    def add_module(self, name, data):
        if name in self.known_modules:
            LOG.warning(f"Adding already-known module {name!r}")
        module_label = data.get('label') or name
        module_entry_page = data.get('entry_page')
        module_pages = data.get('pages', [])
        LOG.info(f"Attaching new module {module_label!r}")
        pages = [Page.deserialize(page,
                                  registry=self.known_functions)
                 for page in module_pages
                 if page is not None]
        for page in pages:
            self.known_pages.update({page.name: page})
        self.known_modules.update({
            name:
                {'label': module_label,
                 'entry_page': module_entry_page,
                 'pages': pages}})
        self.module_change_func()

    def remove_module(self, name):
        if name not in self.known_modules:
            LOG.warning(f"Removing unknown module {name!r}")
        LOG.info(f"Detaching module {name!r}")
        topic_path = f"{self.network_name}/{name}/admin"
        message_data = ControllerDetachMsg()
        self.network.publish(topic_path, message_data)
        self.known_modules.pop(name)
        self.module_change_func()
