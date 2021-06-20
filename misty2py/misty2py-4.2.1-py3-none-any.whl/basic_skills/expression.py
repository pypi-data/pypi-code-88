"""This module enables setting an expression via a single function.
"""

import time
from typing import Dict, Union

from misty2py.robot import Misty
from misty2py.utils.colours import (construct_transition_dict,
                                    get_rgb_from_unknown)
from misty2py.utils.messages import success_parser_from_list
from misty2py.utils.status import ActionLog


def expression(
    misty: Misty,
    image: Union[str, Dict, None] = None,
    sound: Union[str, Dict, None] = None,
    colour_type: Union[str, None] = None,
    colour: Union[str, Dict, None] = None,
    colours: Union[str, Dict, None] = None,
    image_offset: Union[float, int] = 0,
    sound_offset: Union[float, int] = 0,
    colour_offset: Union[float, int] = 0,
    duration: Union[float, int] = 1.5,
) -> Dict:
    """Performs an audio-visual expression. 

    Args:
        misty (Misty): the Misty that performs the expression.
        image (Union[str, Dict, None], optional): The path to the image to display or `None` if no special image should be displayed. Defaults to `None`.
        sound (Union[str, Dict, None], optional): The path to the sound to play or None if no sound should be played. Defaults to `None`.
        colour_type (Union[str, None], optional): `"trans"` if a colour transition should be lit. Defaults to `None`.
        colour (Union[str, Dict, None], optional): The colour of LED as a dictionary or a data shortcut or `None` if no special colour should be lit. Defaults to `None`.
        colours (Union[str, Dict, None], optional): The LED colours as a dictionary or a data shortcut or `None` if no transitioning colours should be lit. Defaults to `None`.
        image_offset (Union[float, int], optional): The offset between starting the expression and displaying the image in ms. Defaults to `0`.
        sound_offset (Union[float, int], optional): The offset between starting the expression and playing the sound in ms. Defaults to `0`.
        colour_offset (Union[float, int], optional): The offset between starting the expression and lighting the LEDs in ms. Defaults to `0`.
        duration (Union[float, int], optional): The duration of the expression. Defaults to `1.5`.

    Returns:
        Dict: The responses from Misty's REST API for every action and the key `overal_success` (bool) specifying whether all actions were successful.
    """
    assert duration > 0, "Duration must be higher than zero."
    assert (
        colour_offset >= 0 and sound_offset >= 0 and image_offset >= 0
    ), "Offsets must be higher or equal to zero"
    assert (
        image or sound or colour or colours
    ), "At least one audio-visual component \
        (display image, sound or led colour / colours) must be set."

    assert (
        image_offset < duration and
        sound_offset < duration and
        colour_offset < duration
    ), "The offsets cannot be higher than the duration."

    actions = ActionLog()

    reset_img = False
    reset_led = False

    offsets = sorted(set([image_offset, sound_offset, colour_offset]))
    for i, offset in enumerate(offsets):
        time.sleep(offset)

        if offset == image_offset:
            if image:
                img_show_message = misty.perform_action(
                    "image_show",
                    data=image
                )
                actions.append_({"img_show": img_show_message})
                reset_img = True

        if offset == sound_offset:
            if sound:
                audio_play_message = misty.perform_action(
                    "audio_play",
                    data=sound
                )
                actions.append_({"audio_play": audio_play_message})

        if offset == colour_offset:
            if colour_type == "trans":
                json_cols = None
                if colours:
                    json_cols = construct_transition_dict(
                        colours,
                        misty.actions.allowed_data
                    )
                elif colour:
                    json_cols = construct_transition_dict(
                        {"col1": colour, "col2": "led_off"},
                        misty.actions.allowed_data
                    )
                if json_cols:
                    led_trans_message = misty.perform_action(
                        "led_trans",
                        data=json_cols
                    )
                    actions.append_({"led_trans": led_trans_message})
                    reset_led = True
            else:
                if colour:
                    json_col = get_rgb_from_unknown(
                        colour, allowed_data=misty.actions.allowed_data
                    )
                    led_message = misty.perform_action("led", data=json_col)
                    actions.append_({"led": led_message})
                    reset_led = True

        if i == len(offsets) - 1:
            time.sleep(duration - offset)

    if reset_img:
        reset_img_message = misty.perform_action(
            "image_show", data="image_content_default"
        )
        actions.append_({"reset_img": reset_img_message})

    if reset_led:
        reset_led_message = misty.perform_action("led", data="led_off")
        actions.append_({"reset_led": reset_led_message})

    return success_parser_from_list(actions.get_())
