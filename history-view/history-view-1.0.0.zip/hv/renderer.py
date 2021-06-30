from jinja2 import Template
import shutil
import pdb
import random
import textwrap
import re

from .globals import *

# fmt: off
# template expects data dictionary with arguments of
#  data list[str]
#  terminal_size int
#  history_length int
DISPLAY_TEMPLATE = Template(
"""🐐🐐 Command History:
There are {{ history_length }} items(s) to observe. Rendering tWidth at {{ terminal_size }}. 

Select an option either by the selector (space|enter) or by typing an index digit.
Enter "q" or "ctrl-c" to exit without selecting a command.

{{ top_line }}
     idx    cmd   

{% for cmd in data -%}   {{ cmd }}
{% endfor %}
{{ bottom_line }}
""")

DOWN_ARROW="\\/"
UP_ARROW="/\\"

EMPTY_DATA_TEMPLATE = Template(
"""
{{ ("-" * terminal_size ) }}
Well that's unfortunate.

I can't find your seach history. I looked here:

I'd `ctrl-c` to exit if I were you. 
{{ ("-" * terminal_size ) }}
""")
# fmt: on


class InvalidConfigurationException(BaseException):
    pass


class HistoryRenderer:
    def __init__(self, data, **kwargs):
        self.data = [cmd.strip() for cmd in data]
        self.frame_size = kwargs.get("frame_size", DEFAULT_FRAME_SIZE)
        self.template = kwargs.get("template", DISPLAY_TEMPLATE)
        self.party_parrot = kwargs.get("parrot_mode", False)
        self.current_frame = kwargs.get("start_frame", 0)
        self.previous_frame = None

        # we start at max because the the render happens top down
        # that means selected starts at
        self.selected_index = self.frame_size - 1

        if not data:
            raise InvalidConfigurationException(
                "The data passed to the renderer needs to be populated. Renderer saw {} items in data array.".format(
                    len(self.data)
                )
            )

        if self.frame_size > len(data):
            raise InvalidConfigurationException(
                "Frame size of {} is bigger than the size of the data array {}!".format(
                    self.frame_size, len(self.data)
                )
            )

    def t_size(self):
        return shutil.get_terminal_size()

    def __is_selected_frame(self, frame_index):
        """
        Takes an index from a frame and returns a boolean to indicate whether or not to show the "selector" on that line.
        """
        return frame_index == self.selected_index

    def __get_frame_index_prefix(self, frame_index):
        return "---> " if self.__is_selected_frame(frame_index) else "     "

    def __render_idx_prefix(self, frame_idx):
        return "{line:{fill}{align}{width}}".format(
            line=" " + str(frame_idx), fill=" ", align="<", width=7
        )

    def __rows_preceeding(self, index=None):
        return (index or self.current_frame) > 0

    def __rows_proceeding(self, index=None):
        begin_idx = index or self.current_frame
        end_idx = begin_idx + self.frame_size

        return any(self.data[end_idx:])

    def __calculate_line(self, direction):
        terminal_size = self.t_size().columns

        if direction == UP_ARROW:
            if not self.__rows_proceeding():
                direction = "=="

        if direction == DOWN_ARROW:
            if not self.__rows_preceeding():
                direction = "=="

        result = "--" + direction + ("-" * (terminal_size - 13)) + direction + "--"
        return result

    def __calculate_prefix(self, r_string):
        if r_string:
            return "\033[{}F".format(len(r_string.split("\n")) - 1)
        else:
            return r_string

    def render_current_frame(self, enable_overwrite=True):
        return self.render_frame(reversed(self.get_frame()), enable_overwrite)

    def __minimize_pad_frame(self, frame):
        minimized_frame = [
            self.__get_frame_index_prefix(index)
            + self.__render_idx_prefix(index)
            + textwrap.shorten(
                history_item, width=self.t_size().columns - 8, placeholder="..."
            )
            for index, history_item in enumerate(frame)
        ]
        padded_frame = [
            "{line:{fill}{align}{width}}".format(
                line=shorted_frame, fill=" ", align="<", width=self.t_size().columns
            )
            for shorted_frame in minimized_frame
        ]
        return padded_frame

    def parrotfy(self, rendered_str):
        result = ""
        code = random.randrange(3, 16) * 16

        if self.party_parrot:
            result += u"\u001b[38;5;{0}m".format(code)

        result += rendered_str

        if self.party_parrot:
            result += u"\u001b[38;5;"

        return result

    def get_command(self, idx):
        frame = self.get_frame()
        return frame[self.frame_size - 1 - idx]

    def render_blank_frame(self):
        replace_regex = r"[^\s]"

        return re.sub(replace_regex, " ", self.previous_frame)

    def render_frame(self, frame, enable_overwrite=True):
        """
        Renders a frame to text. Leaves the value output set in class variable
        `previous_frame`. This will allow the next render to overwrite the previous output
        appropriately.

        """

        rendered_frame = self.parrotfy(
            self.template.render(
                data=self.__minimize_pad_frame(frame),
                terminal_size=self.t_size().columns,
                bottom_line=self.__calculate_line(DOWN_ARROW),
                top_line=self.__calculate_line(UP_ARROW),
                history_length=len(self.data),
            )
        )
        prefix = ""
        if enable_overwrite and self.previous_frame:
            prefix = self.__calculate_prefix(self.previous_frame)

        self.previous_frame = rendered_frame
        return prefix + rendered_frame

    def get_frame(self):
        """
        Gets a frame at current index.

        See get_frame_at_index for details.
        """
        return self.get_frame_at_index(self.current_frame)

    def get_frame_at_index(self, index):
        """
        Gets a frame at current index.

        Array Slice Access method:
            [<--->---------]
             i + f

            i: target index
            f: target index + frame_size

            [i:i+frame_size]
        """
        begin = index
        end = begin + self.frame_size

        return self.data[begin:end]

    def __process_selected_change(self, positive):
        """
        Processes the selected index change of a "go up" or "go down" command.

        Returns whether or not the selected index actually changes
        """
        if positive:
            if self.selected_index < (self.frame_size - 1):
                self.selected_index = self.selected_index + 1
                return True
        else:
            if self.selected_index > (self.frame_size - 4):
                self.selected_index = self.selected_index - 1
                return True
        return False

    def increment_frame(self):
        """
        Advances the frame in the positive direction. Moving first element of viewable frame towards the end.
        Never moves beyond safe bound.

        Given a basic array of data, it would looks like...

        < in frame >
        [<--->---------] --> [-<--->--------]
         0                    01
        """
        if not self.current_frame >= (len(self.data) - self.frame_size):
            self.current_frame += 1

            # we only need to move our frame if the selected index updates (otherwise we'll get a double move)
            self.current_frame -= self.__process_selected_change(False)

    def decrement_frame(self):
        """
        Retreats the frame in the negative direction, bringing the first element in frame closer to 0.
        Never moves beyond safe bound.

        Given a basic array of data, it would looks like...

        < in frame >
        [-<--->--------] --> [<--->---------]
         01                   0
        """
        if self.current_frame > 0 or self.selected_index < self.frame_size - 1:
            self.current_frame -= 1

            self.current_frame += self.__process_selected_change(True)
