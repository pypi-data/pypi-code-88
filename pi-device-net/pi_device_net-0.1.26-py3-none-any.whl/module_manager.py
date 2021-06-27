# Copyright (c) 2021 Edwin Wise
# MIT License
# See LICENSE for details
"""
    PiDeviceNet Module Manager. High level framework to deal with module
    connection management.
"""
import logging
from time import sleep

import pygame

from pi_device_net import (ModuleNetwork, ModuleAttachMsg, ModuleDetachMsg,
                           Command)

LOG = logging.getLogger(__name__)


class ModuleManager:
    """ Manage the high-level module interactions.

    Expects pygame.init() to have already been called.
    """

    def __init(self, controller_timeout, loop_delay, network_name, module_name,
               display_name,
               message_callback, update_callback, pages, subscriptions):
        """
        Parameters
        ----------
        controller_timeout : Number
            How long we wait for a controller message before we disconnect
        loop_delay : Number
            How long to sleep (in seconds) at the end of each cycle.  Not a
            true framerate because we don't account for processing times.
        network_name : String
            Name of the network as a whole
        module_name : String
            Name of this module
        display_name : String
            Name to show in the controller
        message_callback : Callable[String, String, Dict]
            The method that is called for unhandled messages, where the
            parameters are (module_name, topic, message_data)
        update_callback : Callable[]
            This method is called once per frame
        pages : List(Page)
            The pages that this module defines for the controller
        subscriptions : Tuple(String, String)
            Message subscriptions in the form of (module, topic), as per
            ModuleNetwork.subscribe()
        """
        self.controller_timeout = controller_timeout
        self.loop_delay = loop_delay
        self.network_name = network_name
        self.module_name = module_name
        self.display_name = display_name
        self.message_callback = message_callback
        self.update_callback = update_callback
        self.pages = pages
        self.subscriptions = subscriptions

        self.ping_time = pygame.time.get_ticks() // 1000

        self.network = ModuleNetwork(self.network_name,
                                     self.module_name,
                                     self.handle_messages)

    def run(self):
        try:
            # Do nothing forever; all activity is managed in callbacks
            while True:
                # Discover locks up until this module is discovered, then it
                # activates the communication.
                if self.network.discover():
                    self.ping_time = pygame.time.get_ticks() // 1000

                    print("Attach to Controller")
                    message_data = ModuleAttachMsg(
                        label=self.display_name,
                        entry_page=self.pages[0].name,
                        pages=[page.serialize() for page in self.pages]
                    )
                    self.network.publish('admin', message_data)

                    print("Subscribe to messages:")
                    for module, topic in self.subscriptions:
                        print("... {module}: {topic}")
                        self.network.subscribe(module=module, topic=topic)
                else:
                    now = pygame.time.get_ticks() // 1000
                    if now - self.ping_time > self.controller_timeout:
                        print("Timeout, detach controller")
                        message_data = ModuleDetachMsg()
                        self.network.publish('admin', message_data)

                        self.network.restart()
                    else:
                        self.update_callback()

                sleep(self.loop_delay)

        except KeyboardInterrupt:
            LOG.info("Ctrl-C received")
        except Exception as e:
            LOG.error(f"Unmanaged exception {type(e)}: {e}")
        finally:
            self.stop()
            self.network.stop()
            print(f"Exiting {self.display_name} Module")

    def stop(self):
        message_data = ModuleDetachMsg()
        self.network.publish('admin', message_data)

    def handle_messages(self, module, topic, msg):
        if msg.get('module') == self.module_name:
            command = msg.get('command')
            if command == Command.DETACH.value:
                self.network.restart()
            elif command == Command.PING.value:
                self.ping_time = pygame.time.get_ticks() // 1000
            else:
                self.message_callback(module, topic, msg)
