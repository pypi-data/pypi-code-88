from enum import Enum
import os
import sys
import pdb


class INTERACTION(Enum):
    """
    Used to give direction back to the console loop for informing next step.

    FRAME_BACK: Given that the console history is stored newest FIRST, going backwards is effectively
    a current index INCREMENT.

    FRAME_FORWARD: As mentioned in FRAME_BACK, with a newest-first history array, we need to DECREMENT
    the current index.
    """

    ITEM_SELECTED = 1
    FRAME_BACK = 2
    FRAME_FORWARD = 3
    UNKNOWN = 4
    EXIT = 5


class InteractionResult:
    def __init__(self, interaction, data=None):
        self.result = interaction
        self.value = data


class HistoryInteractor:
    """
    HV needs to handle two tasks when showing the selected "frame" of data
    from a users history.

    We need to accept written input that:
        a. Reflects the # command in the view pane that we want to keep, an integer followed by an `enter`
        b. Listen for `up`/`left` or `down`/`right` direction commands that change selected frame
        c. Listen for a bare `enter` that takes the currently selected history item.

    Given the fact that we want to handle both the text input AND the keypresses, this will have to be more
    complicated than input() interaction, and as such requires an abstraction layer.
    """

    def __init__(self):
        pass

    def __parse(self, char):
        if char == b"H":
            return InteractionResult(interaction=INTERACTION.FRAME_BACK, data=None)

        if char == b"P":
            return InteractionResult(interaction=INTERACTION.FRAME_FORWARD, data=None)

        ## not having data on an ITEM_SELECTED means that we're selecting the current index
        if char == " ":
            return InteractionResult(interaction=INTERACTION.ITEM_SELECTED, data=None)

        if char == b"\r":
            return InteractionResult(interaction=INTERACTION.ITEM_SELECTED, data=None)

        if char == b"\x1b":
            return InteractionResult(interaction=INTERACTION.EXIT, data=None)

        if char == b"q":
            return InteractionResult(interaction=INTERACTION.EXIT, data=None)

        # see if they selected an index
        try:
            if int(char) in range(0, 10):
                return InteractionResult(
                    interaction=INTERACTION.ITEM_SELECTED, data=int(char)
                )
        except:
            pass

        # everything else we don't understand, just return unknown
        return InteractionResult(interaction=INTERACTION.UKNOWN)

    # a very smart person came up with this methodology https://stackoverflow.com/a/34956791
    def wait_for_input(self):
        result = None
        if os.name == "nt":
            import msvcrt

            result = msvcrt.getch()
            if ord(result) == 224:
                result = msvcrt.getch()
        else:
            # TODO: https://github.com/semick-dev/history-view/issues/8
            raise NotImplementedError("This is completely untested code")

        return self.__parse(result)
