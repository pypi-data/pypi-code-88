"""
The AutoCoconut Project - Module 'interpreter'
===============================================================================
The Interpreter module takes the dictionary of events created by the event_handler module
and iterates over particular event to interpret the real actions behind that events.
Then it creates a dictionary of interpreted actions chronologically ordered.

Created by Lukáš Růžička (lruzicka@redhat.com), 2020 and provided under the
General Public License v3.
"""
from math import sqrt, ceil

class Interpreter:
    """ The Interpreter class holds the methods of the interpreter module. """


    def __init__(self, rawreport, stop_key=None):
        """ Initiates the variables. """
        # The input raw json file from the event_handler.py
        self.report = rawreport

        ############### Mouse related attributes #####################################
        # Holds the coordinates of the latest known click to identify doubleclick and drag.
        self.last_click_coords = ()
        # Holds the timestamp of the latest known click to identify doubleclick and drag.
        self.last_click_timestamp = None
        # Holds the horizontal and vertical scrolls to calculate the final scrolling distance.
        self.hscroll = 0
        self.vscroll = 0
        # Holds the position where the scroll started to get the scroll coordinates for the
        # final scroll events.
        self.scroll_coordinates = None
        # And the scroll event
        self.scroll_event = None
        # Holds the move event
        self.move_event = None
        # If it is clicked
        self.clicked = False
        self.last_click = None

        ################ Keyboard related attributes ##################################
        # Holds any alphanumeric keys that have been pressed, until they are resolved
        # and the key buffer cleared -> it can either be resolved as typing, or as
        # key combination.
        self.keybuffer = []
        # Holds any pressed modifiers until one of them is released. In that case,
        # all modifiers are purged from this buffer, since it does not make any sense
        # to keep them. Ex.: ctrl-f4 is not pressed by releasing alt from ctrl-alt-f4.
        self.modified = []
        # Holds the timestamp of the last key pressed.
        self.last_key_timestamp = None
        # Holds the last modifier event and it timestamp.
        self.last_mod_event = None
        self.last_mod_timestamp = None
        # Holds the last special key event and its timestamp.
        self.last_special_event = None
        self.last_alpha_event = None
        # If no stop_key is defined, use the obligatory F10.
        if not stop_key:
            self.stop_key = "f10"
        else:
            self.stop_key = stop_key
        # Mappings for non-existent keys in CZ layout.
        # This is an ugly hack to deal with the Czech keyboard layout I am using, because
        # pynput cannot recognize some of the keys, namely the "right alt" key and the
        # numerical "5" key. This dictionary helps to deal with the "right alt".
        self.altmap = {
            "q":"\\",
            "w":"|",
            "e":"€",
            "r":"¶",
            "t":"ŧ",
            "z":"←",
            "u":"↓",
            "i":"→",
            "o":"ø",
            "p":"þ",
            "a":"~",
            "s":"đ",
            "d":"Đ",
            "f":"[",
            "g":"]",
            "h":"`",
            "j":"'",
            "k":"ł",
            "l":"Ł",
            "ů":"$",
            "§":"'",
            "y":"°",
            "x":"#",
            "c":"&",
            "v":"@",
            "b":"{",
            "n":"}",
            "m":"^",
            ",":"<",
            ".":">",
            "-":"*"
        }


    def press_modifier(self, modifier):
        """ Record the modifier key.

        This method takes the name of the modifier key (str) as argument.
        And stores it in a global variable for further access and evaluation."""
        self.modified.append(modifier)
        return self.modified

    def release_modifier(self):
        """ Delete the buffer of recorded modifiers. """
        # This will instantly delete the whole modifiers buffer, because if one modifier
        # disappears from a combination it becomes not valid anymore.
        self.modified = []
        return self.modified

    def use_buffer(self, addition=None, modifier=False):
        """ Handle various buffer activities.

        The self.keybuffer holds the pressed alphanumeric keys to make this
        sequence ready for resolving when some non-alphanumeric event happens.
        Since some keys may have some function that it is worth implementing,
        for example a backspace should delete one character from the buffer,
        rather than be "just noticed", this method allows better control to
        access the self.keybuffer.

        It takes possibly arguments 'addition' (str) to add the variable
        content into the buffer and 'modifier' (bool) to control the format
        of the buffer output. With modifier being True, the single characters
        are divided by a dash. """
        if addition:
            if addition == "backspace":
                try:
                    string = self.keybuffer.pop(-1)
                except IndexError:
                    string = ""
            else:
                self.keybuffer.append(addition)
                string = addition
        else:
            if modifier:
                string = '-'.join(self.keybuffer)
                self.keybuffer = []
            else:
                string = ''.join(self.keybuffer)
                self.keybuffer = []
        return string

    def calculate_time_delta(self, oldstamp, newstamp):
        """ Calculate the time difference between the time stamps.

        This takes two timestamps as arguments and calculates the
        difference between them."""
        # In order to recognize how fast the single mouse clicks follow
        # each other, let us calculate the difference between the times
        # when they happened. This is mainly used for interpreting the
        # double clicks.
        delta = abs(newstamp - oldstamp)
        return delta

    def calculate_click_distance(self, oldclick, newclick):
        """ Calculates the distance between two click points.

        Takes the click coordinates of the two click and
        calculates the shortest possible distance between
        them on cartesian coordinates, using the Pythagorean
        method."""
        # In order to recognize, how near the single clicks were made
        # we want to calculate the distance between them. This is also 
        # used to identify a double click.
        deltax = abs(newclick[0] - oldclick[0])
        deltay = abs(newclick[1] - oldclick[1])
        distance = sqrt((deltax**2)+(deltay**2))
        return distance

    def order_dict(self, dictionary):
        """ Order the dictionary according to the keys.

        The interpreted events are stored in a new dictionary
        which may end up unordered and the json output is not
        chronologically ordered which is not desired. This method
        orders the dictionary."""
        records = sorted(dictionary.items())
        sdict = {}
        for rec in records:
            sdict[rec[0]] = rec[1]
        return sdict

    def deal_with_mouse_leftovers(self, what):
        """ Deal with unresolved mouse events.

        When the interpret_mouse_action() runs for the first time, it does not evaluate anything,
        it only remembers an event and it decides in later iterations, if the previous is a
        standalone event or if it is connected with the current event somehow (doubleclick, drag).
        If the previous was a standalone event, it has to be dealt with first and then make the
        intepretation (or remembering) of the current event.

        The "what" parameter can be a "scroll", "click", or "move", depending on what we need
        to resolve - different events should be resolved on different places, for example a click can
        resolve some previous scrolling events, but it cannot resolve a previous click, because two
        clicks must be compared for a doubleclick.
        """
        # The events from pynput come as independent single units that might combine into something
        # that we call "superevents", such as mouse drags, double click and key combinations.
        # However, we cannot interpret a superevent, until we will see at least two, each other following
        # events. Then, after we can interpret an event, we might end up having two events at the same time.
        # A current event and a previous (buffered) event. 
        # This is a helper method to clear the buffered event first, before dealing with the current event.
        # It updates the event's fields accordingly and deletes it from the buffer.
        output = {}
        if what == 'scroll' and self.scroll_event:
            sevent = self.scroll_event
            sevent['horizontal'] = self.hscroll
            sevent['vertical'] = self.vscroll
            timestamp = self.last_click_timestamp
            # Zero the scroll events
            self.hscroll = 0
            self.vscroll = 0
            self.scroll_event = None
            self.last_click_timestamp = None
            self.last_click = None
            output[timestamp] = sevent

        elif what == 'drag' and self.move_event:
            mevent = self.move_event
            self.last_click = None
            self.move_event = None
            output[self.last_click_timestamp] = mevent
            self.last_click_timestamp = None

        elif what == 'click' and self.last_click:
            output[self.last_click_timestamp] = self.last_click
            self.last_click_timestamp = None
            self.last_click = None

        return output

    def deal_with_key_leftovers(self, what, reason, combination=None):
        """ Deal with unresolved keyboard events.

        See deal_with_mouse_leftovers() doc string for more info."""
        # See deal_with_mouse_leftovers() for more info, this one has the same purpose
        # just to deal with keyboard stuff.
        output = {}
        if not combination:
            combination = None
        # This will resolve any previously saved typing events.
        if what == 'typing':
            string = self.use_buffer()
            if string and "Ω" not in string:
                timestamp = self.last_key_timestamp
                event = self.last_alpha_event
                event['type'] = "typing"
                event['subtype'] = "text"
                event['action'] = "type"
                event["text"] = string
                event["reason"] = reason
                event["combined"] = combination
                output[timestamp] = event
                self.last_key_timestamp = None
                self.last_alpha_event = None
        # This will resolve shift behaviour, if it was not used to produce text.
        elif what == 'shift':
            if self.keybuffer:
                pass
            else:
                event = self.last_mod_event
                timestamp = self.last_mod_timestamp
                output[timestamp] = event
        # This will resolve any characters pressed under a modifier.
        elif what == 'modifier':
            event = self.last_mod_event
            # If modifier is pressed and held and a special key is pressed, then read the buffer
            # as it was a regular text, because the names of the special key are stored in the
            # keybuffer, too.
            if reason == "special key pressed":
                string = self.use_buffer()
            else:
                # With alphanumeric keys, take them out as a sequence of characters divided by dashes
                # because this is, how they usually are represented.
                string = self.use_buffer(modifier=True)
                # If the string is empty, it means that only modifiers were pressed with no other keys.
                # Although, this is a strange corner case, we think this should be also correclty recognized.
                # Put the names of pressed modifiers into the string instead to be later picked up by the jinja
                # template.
                if not string:
                    string = "-".join(self.modified)
            timestamp = self.last_mod_timestamp
            # The OMEGA sign is a place holder in the keybuffer that helps to correctly identify a situation 
            # when there is a mouse action when the modifiers are pressed. Without this, it would look like
            # if the modifier was pressed and released and then there was a mouse event. We do not need to
            # do anything with it here at this place.
            if string == "Ω":
                pass
            elif string:
                event['type'] = "key combination"
                event['subtype'] = "modifier"
                event['key'] = string.lower()
                event['reason'] = reason
                event['combined'] = combination
                output[timestamp] = event
            else:
                output[timestamp] = event

            self.last_mod_event = None
            self.last_mod_timestamp = None
            self.last_key_timestamp = None
        return output

    def interpret_mouse_action(self, event, timestamp):
        """ Interpret the mouse action.

        This is one of the core methods of the interpreter and it can interpret the single mouse
        events and merge into a one super event, such as a click, a double click, scroll, and
        a drag.

        The method is cumulative, it means that it can only recognize some of the events when it runs
        for the second time. Therefore, it stores its status outside this method in the global class
        variables. """
        output = {}
        # Even if not used, we want always have a "combined" key in the dictionary that saves us from
        # dealing with too many exceptions.
        event['combined'] = None
        # If the current event is a click:
        if event['action'] == 'click':
            # we want to make sure that there are no other previously stored events waiting in the queue.
            # This is typically true for a scroll or for typing. Other events get cleared by other methods.
            # If they are, we will fix them first.
            leftover = self.deal_with_mouse_leftovers('scroll')
            output.update(leftover)
            leftover = self.deal_with_key_leftovers('typing', 'mouse_clicked')
            output.update(leftover)
            # If there wasn't any previous click already, we will just remember this one and 
            # wait for the following event to compare it.
            if not self.last_click:
                if self.modified:
                # If the click happens when a modifier is pressed, we will add a special (omega)
                # placeholder in the keybuffer to make sure the sequence of events (modifier press, click,
                # and modifier released) gets correctly propagated.
                    event['combined'] = self.modified
                    self.use_buffer(addition="Ω")
                self.last_click = event
                self.last_click_timestamp = timestamp
                self.clicked = True
            else:
                # If there has already been a click recorded, calculate the time difference
                # and the distance between the previous and this one click.
                delta = self.calculate_time_delta(self.last_click_timestamp, timestamp)
                distance = self.calculate_click_distance(self.last_click['coordinates'], event['coordinates'])
                # If the time is less than half a second and distance less than 5px, we assume
                # that it was a double click. We merge the two events and update the data in the
                # current event to support it. Also, we update the buffers.
                if delta < 0.5 and distance < 5:
                    event['action'] = 'doubleclick'
                    # When this click also happens under a modifier, we'll repeat the keybuffer hack.
                    if self.modified:
                        event['combined'] = self.modified
                        self.use_buffer(addition="Ω")
                    # To merge the two events properly, we can use the information from the currecnt event
                    # but we need to record the timestamp of the previous events, because this is the real
                    # time when the doubleclick event happened.
                    output[self.last_click_timestamp] = event
                    self.last_click = None
                    self.last_click_timestamp = timestamp
                else:
                    # If this second (current) click do not form a doubleclick with the previous event,
                    # then put the previous click into the output dictionary and replace the buffer 
                    # with the current event to be compared again with the next event.
                    if self.modified:
                        event['combined'] = self.modified
                        self.use_buffer(addition="Ω")
                    output[self.last_click_timestamp] = self.last_click
                    self.last_click = event
                    self.last_click_timestamp = timestamp

        elif event['action'] == 'release':
            # The release of the mouse button is important when we want to interpret a drag later.
            # When the mouse has been released, we will pick up the latest recorded move event,
            # that has actually become a drag
            leftover = self.deal_with_mouse_leftovers('drag')
            output.update(leftover)
            self.clicked = False

        elif event['action'] == 'scroll':
            # If a scroll is recorded, we will look if there is not an unresolved mouse click
            # from the previous run.
            leftover = self.deal_with_mouse_leftovers('click')
            output.update(leftover)
            # If not, we will just record the scroll and make it ready for a pick-up by
            # some other methods, because a scroll cannot pick up a scroll, it must be
            # added to the previous scroll obviously.
            hdir = event['horizontal']
            vdir = event['vertical']
            self.hscroll += hdir
            self.vscroll += vdir
            self.scroll_coordinates = event['coordinates']
            # If the scroll happens under a modifier, let us use the same trick as before
            # with the keybuffer placeholder (see above).
            if self.modified:
                event['combined'] = self.modified
                if not self.keybuffer:
                    self.use_buffer(addition="Ω")
                else:
                    pass
            # Any consecutive scroll is only merged with the previous scroll and the number of
            # steps is increased. However, for the scrolling superevent, we need to record the
            # timestamp of the very first scroll event. Therefore only remember a timestamp
            # when there has not beed one remembered previously.
            if not self.last_click_timestamp:
                self.last_click_timestamp = timestamp
            # However, let us update the event itself.
            self.scroll_event = event

        elif event['action'] == 'move':
            # When the mouse is moving and one of its buttons is clicked, we do not deal with
            # a mouse move anymore, but rather a drag. So, we need to interpret this differently.
            if self.last_click and self.clicked:
                distance = self.calculate_click_distance(self.last_click['coordinates'], event['coordinates'])
                # Some clicks that happened at the end of mouse move were incorrectly identified as mouse drags,
                # therefore we want a drag only be reported if the dragged distance is higher than 10 pixels.
                if distance > 10:
                    # Rename the event to a "drag"
                    self.last_click['action'] = 'drag'
                    # Calculate the duration of the click
                    duration = self.calculate_time_delta(self.last_click_timestamp, timestamp)
                    self.last_click['duration'] = ceil(duration)
                    # Record the coordinates where mouse was released.
                    self.last_click['end_coordinates'] = event['coordinates']
                    # And update the last move event to hold the data of this current drag event.
                    # We only reserve the move events for drag control, so this does not harm anything.
                    self.move_event = self.last_click
            # While moving the mouse, we can resolve any unresolved mouse events in order not to have
            # to wait until some "real" event picks them up and save some repetition in the code.
            # In this case, it can either be a click
            elif self.last_click:
                leftover = self.deal_with_mouse_leftovers('click')
                output.update(leftover)
            # or it can be a scroll.
            elif self.scroll_event:
                leftover = self.deal_with_mouse_leftovers('scroll')
                output.update(leftover)
        return output


    def interpret_key_action(self, event, timestamp):
        """ Interpret key actions.

        This is one of the core methods of the interpreter and it can interpret the single key
        events and merge into a one super event, such as a single press, typing, or a key combo.

        The method is cumulative, it means that it can only recognize some of the events when it runs
        for the second time. Therefore, it stores its status outside this method in the global class
        variables. """
        output = {}
        event["combined"] = None
        #event_class = (event['type'], event['subtype'], event['action'])
        # If the pressed key is a normal "alhphanumeric" key (with certain exceptions)
        if event['type'] == "key" and event['subtype'] == "alphanumeric" and event['action'] == "press":
        #if event_class == ('key', 'alphanumeric', 'press'):
            # All mouse events should have been resolved by themselves when there is some keyboard
            # action except the scrolling. Let us fix it here in case it is necessary.
            leftover = self.deal_with_mouse_leftovers('scroll')
            output.update(leftover)
            # If the current key is a "space" key, we take it as an alphanumeric key. We will add the
            # appropriate whitespace into the keybuffer.
            if event['key'] == "space":
                if not self.keybuffer:
                    self.use_buffer(addition=" ")
                    self.last_alpha_event = event
                    self.last_key_timestamp = timestamp
                else:
                    self.use_buffer(addition=" ")
            # If the key is a tab, we will not record it in the text buffer, but rather handle it as a
            # special key.
            elif event['key'] == "tab":
                # It means we need to collect a previously typed text
                leftover = self.deal_with_key_leftovers("typing", "tab pressed")
                output.update(leftover)
                # and remember this tab event
                output[timestamp] = event
                self.last_alpha_event = event
                self.last_key_timestamp = None
            # Sometimes, the key input is not recognized properly and None is returned instead
            # of the proper key name. On my system, there are two cases that produce this, such as
            # the 'right alt' key and the 'numeric 5'. While we might be able to workaround the
            # numeric 5 by pressing a regular 5 instead, there is no way to workaround the right
            # alt. Therefore, we assume that such situation is when the right alt has been pressed.
            elif event['key'] is None:
                if not self.modified:
                    self.press_modifier("alt_gr")
                else:
                    self.press_modifier("alt")
                    self.use_buffer(addition="alt")
            # Otherwise, we believe that the key is part of a string
            # and will be recorded in the buffer.
            else:
                # However, we need to replace the characters produced while right alt is pressed.
                # Although, correctly interpreted by the operating system, in pynput, they are
                # not correctly interpreted (as result of key combination) so we need to remap
                # them.
                if self.modified and len(self.modified) == 1 and "alt_gr" in self.modified:
                    key = event['key']
                    modkey = self.altmap[key]
                    self.use_buffer(addition=modkey)
                else:
                    # For all other alphanumeric keys, record them in the self.keybuffer.
                    self.use_buffer(addition=event['key'])
                    self.last_alpha_event = event
                    if not self.last_key_timestamp:
                        self.last_key_timestamp = timestamp
        # If the key is one of the special keys.
        elif event['type'] == "key" and event['subtype'] == "special" and event['action'] == "press":
        #elif event_class == ('key', 'special', 'press'):
            # There might be a scroll waiting to be picked up, if so pick it.
            leftover = self.deal_with_mouse_leftovers('scroll')
            output.update(leftover)
            # With backspace, we do not want to record pressing it, but we want it to behave as a means
            # of correction. This makes sure that backspace will remove the last typed character from
            # the keybuffer. 
            if event['key'] == "backspace":
                self.use_buffer(addition="backspace")
            else:
                # All other special keys should be treated normally. A special key might come in
                # the middle of typing, so we need to pick the typing event before we do anything else.
                leftover = self.deal_with_key_leftovers("typing", "special key pressed")
                output.update(leftover)
                event['reason'] = "key released"
                # Also, we need fix a case when the special key is pressed after a modifier key to merge
                # it into a key combination event.
                if self.modified:
                    event['combined'] = self.modified
                    self.last_mod_event = None
                self.last_special_event = event
                output[timestamp] = event
        # If the key is a stop key
        elif event['type'] == "key" and event['subtype'] == "stop" and event['action'] == "press":
        #elif event_class == ('key', 'stop', 'press'):
            # Deal with any leftovers from previous runs to properly close the events.
            leftover = self.deal_with_mouse_leftovers("click")
            output.update(leftover)
            leftover = self.deal_with_mouse_leftovers("scroll")
            output.update(leftover)
            leftover = self.deal_with_key_leftovers("typing", "stop key pressed")
            # Also add the stop key press to the output to get post recording screenshot to check
            # the resulting action later.
            output.update(leftover)
            output[timestamp] = event
        # If the pressed key is the non mapped key (right alt) or if it is interpreted that way.
        elif event['type'] == "key" and event['subtype'] == "non-mapped" and event['action'] == "press":
        #elif event_class == ('key', 'non-mapped', 'press'):
            # For the shift-alt combination that produces a None value, we need to make sure,
            # that the None value is replaced by the correct key names, ergo shift-alt. So, if the last known
            # modifier is a shift, then update this event to be the "alt" key, even if it originally was
            # a None key.
            if self.modified and self.modified[-1] == "shift":
                event['subtype'] = "modifier"
                event['key'] = "alt"
                self.press_modifier(event['key'])
                self.last_mod_event = event
            ## If another modifier has been pressed, handle that as another modifier and add it to the 
            ## list of pressed modifiers.
            #elif self.modified:
            #    self.press_modifier('alt_gr')
            #    event['key'] = 'alt_gr'
            #    self.last_mod_event = event
            # If no modifier has been pressed, we assume that here, the right alt key was pressed. This
            # is not entirely correct, but it lifts the bigger burden we have with None keys.
            else:
                event['subtype'] = "modifier"
                event['key'] = "alt_gr"
                self.press_modifier(event['key'])
                self.last_mod_event = event
                self.last_mod_timestamp = timestamp

        # If the key is one of the modifiers and if it is pressed:
        elif event['type'] == "key" and event['subtype'] == "modifier" and event['action'] == "press":
        #elif event_class == ('key', 'modifier', 'press'):
            # Let us check, if there is a scroll left over from the mouse.
            leftover = self.deal_with_mouse_leftovers("scroll")
            output.update(leftover)
            # Let us handle shift differently. Correctly capitalized output is received already from 
            # pynput, but we still cannot treat shift as normal modifier, as normal modifiers would
            # interrupt any typing process and produce a key combination. With shift, we want to 
            # keep typing going on.
            if not self.modified and event['key'] == "shift":
                # But we still want to add the shift to the list of modifiers, if the following
                # event will also be a modifier.
                self.press_modifier(event['key'])
                self.last_mod_timestamp = timestamp
                self.last_mod_event = event
            elif self.modified:
            # For any consecutive modifier presses, add it to the list of modifiers.
                self.press_modifier(event['key'])
                self.last_mod_event = event
            # If other modifiers than shift are pressed for the same time.
            else:
                # We will interrupt and pick up any typing event.
                leftover = self.deal_with_key_leftovers("typing", "modifier key pressed")
                output.update(leftover)
                # And add the event to the modifying events.
                self.press_modifier(event['key'])
                self.last_mod_timestamp = timestamp
                self.last_mod_event = event
        # If a modifier has been released.
        elif event['type'] == "key" and event['subtype'] == "modifier" and event['action'] == "release":
        #elif event_class == ('key', 'modifier', 'release'):
            # If shift was the only modifier pressed without any alphanumeric key with it, 
            # record that in the output, handle the buffer and release modifiers.
            if self.modified and len(self.modified) == 1 and "shift" in self.modified:
                leftover = self.deal_with_key_leftovers("shift", "shift key pressed")
                output.update(leftover)
                self.release_modifier()
            # If there were more modifiers, then handle the leftovers and resolve the keybuffer
            # for the modifiers.
            elif self.modified:
                # Deal with mouse actions that happened while modified.
                click = self.deal_with_mouse_leftovers("click")
                output.update(click)
                scroll = self.deal_with_mouse_leftovers("scroll")
                output.update(scroll)
                mods = self.modified
                if self.last_special_event:
                    # If the last pressed key was a special key.
                    leftover = self.deal_with_key_leftovers("modifier", "special key pressed", combination=mods)
                    self.last_special_event = None
                else:
                    leftover = self.deal_with_key_leftovers("modifier", "modifier key released", combination=mods)
                output.update(leftover)
                self.release_modifier()
                output[timestamp] = event
            # Nothing else is possible at the moment, but may come in the future.
            else:
                pass
        # If the released key was the non-mapped key.
        elif event['type'] == "key" and event['subtype'] == "non-mapped" and event['action'] == "release":
        #elif event_class == ('key', 'non-mapped', 'release'):
            # This happens when "alt_gr" was the only modifier. In that case, the key buffer is resolved
            # similarly to a shift key, because the correct characters are part of the buffer already.
            if self.modified and len(self.modified) == 1 and "alt_gr" in self.modified:
                leftover = self.deal_with_key_leftovers("shift", "alt_gr")
                output.update(leftover)
                self.release_modifier()
            # with more modifiers pressed
            elif self.modified:
                mods = self.modified
                leftover = self.deal_with_key_leftovers("modifier", "modifier key released", combination=mods)
                output.update(leftover)
                self.release_modifier()
        # There might be some empty records in the dictionary, this will only take a non-empty records.
        final_output = {k: v for k, v in output.items() if v}
        return final_output


    def create_clean_report(self):
        """ Iterate over the event dictionary and interpret the single events.

        This function is a wrapper for the Interpreter class. """
        # Lets create an empty new dictionary to hold the interpreted events.
        clean_report = {}
        # Let us clean the self.keybuffer (just in case)
        self.keybuffer = []
        # Make sure the incoming dictionary entries are chronologically ordered
        records = self.order_dict(self.report)
        # Iterate over the keys and do the interpretation magic.
        for timestamp in records:
            # Let us save each timestamp in a buffer so that we can track back
            # when a sequence of events started and ended.
            event = self.report[timestamp]
            # Interpret the mouse events here
            if event['type'] == "mouse":
                idata = self.interpret_mouse_action(event, timestamp)
                if idata:
                    clean_report.update(idata)
            # And the keyboard events here
            else:
                idata = self.interpret_key_action(event, timestamp)
                if idata:
                    clean_report.update(idata)
        # Order the dictionary to make sure, it is chronologically ordered.
        clean_report = self.order_dict(clean_report)
        return clean_report
