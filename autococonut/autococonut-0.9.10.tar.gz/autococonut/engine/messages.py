"""
The AutoCoconut Project - Module 'messages'
========================================================================================

This module returns info messages for the AutoCococunt Interpreter.
"""


class Messagebox:
    """ Provide strings for printing the information."""
    def __init__(self, language):
        self.language = language

    def title(self):
        """ Set the title."""
        title = ""
        if self.language == "md" or self.language == "openqa":
            title = "# AutoCoconut workflow record."
        elif self.language == "html":
            title = "<h1>AutoCoconut workflow record.</h1>\n<ol>"
        return title

    def click(self, button, position, needle):
        """ Provide info about clicks. """
        if self.language == "md" or self.language == "markdown":
            infoline = f"Click with **{button}** button at position *{position}*. See ![{needle}]({needle}) for the recorded click location."
        elif self.language == "html":
            infoline = f'Click with <b>{button}</b> button at position <em>{position}</em>. See <img src="{needle}" width="15%" /> for the suggested needle.</li>'
        elif self.language == "openqa":
            infoline = f'assert_and_click("{needle}", button => {button}, timeout => 30);'
        return infoline

    def double_click(self, button, position, needle):
        """ Provide info about double clicks. """
        if self.language == "md" or self.language == "markdown":
            infoline = f"Double click using **{button}** button at position *{position}*. See ![{needle}]({needle}) for the suggested needle."
        elif self.language == "html":
            infoline = f'<li>DoubleClick using <b>{button}</b> button at position <em>{position}</em>. See <img src="{needle}" width="15%" /> for the suggested needle.</li>'
        elif self.language == "openqa":
            infoline = f"assert_and_click({needle}, button => {button}, dclick => 1, timeout => 30);"
        return infoline

    def combo_prefix(self, key):
        """ Provide info about key combo prefixes, if any. """
        if self.language == "md":
            prefix = f"1. Press and hold the **{key}** key. "
        elif self.language == "html":
            prefix = f"<li>Press and hold the <b>{key}</b> key. "
        elif self.language == "openqa":
            prefix = f'hold_key("{key}");\n'
        return prefix

    def scroll(self, horsteps, versteps, direction):
        """ Provide info about scrolls. """
        if self.language == "md":
            infoline = f"Scroll mouse in **{horsteps}** horizontal steps and in **{versteps}** vertical steps to the **{direction}**."
        elif self.language == "html":
            infoline = f"<li>Scroll mouse in <b>{steps}</b> steps to the <b>{direction}</b>.</li>"
        # In OpenQA, mouse scrolls are not supported, so we change it into pressing the particular
        # arrow key instead
        elif self.language == "openqa":
            if direction == "north":
                key = "up"
            else:
                key = "down"
            command = 'send_key("{}");'.format(key)
            condition = "(my $num = 0; $num == {}; $num++)".format(steps)
            infoline = 'for {} {}'.format(condition, command)
        return infoline

    def drag(self, button, start, position, needle):
        """ Provide info about drags. """
        if self.language == "md":
            infoline = f"Click with **{button}** button at position *{start}*, drag the mouse to position *{position}* and release the button. See ![{needle}]({needle}.png) for the area defined by the action."
        elif self.language == "html":
            infoline = f"Click with <b>{button}</b> button at position <em>{start}</em>, drag the mouse to position <em>{position}</em> and release the button. See <img src='{needle}.png' width='15%' /> for the area defined by the action."
        elif self.language == "openqa":
            infoline = f"# Dragging the mouse is not supported. You are on your own here: Click with **{button}** button at position *{start}*, drag the mouse to position *{position}* and release the button."
        return infoline

    def keypress(self, key, combo=None, needle=None):
        """ Provide info about keypresses. """
        if not combo:
            combo = ""
        else:
            combo = "-".join(combo)
            combo = f"{combo}-"

        if self.language == "md":
            nfix = ""
            if needle:
                nfix = f"See ![{needle}]({needle}.png) for a screen suggested to assert."
            infoline = f"1. Press the **{combo}{key}** key(s). {nfix}"
        elif self.language == "html":
            nfix = ""
            if needle:
                nfix = f"See <img src='{needle}.png' width='15%' /> for a screen suggested to assert."
            infoline = f"<li>Press {ins} the <b>{key}</b> {spec}key. {nfix}"
        elif self.language == "openqa":
            if key == "enter":
                key = "ret"
            if hold:
                infoline = f'hold_key("{key}");\nassert_screen({needle});'
            else:
                infoline = f'send_key("{key}");\nassert_screen({needle});'
        return infoline

    def type(self, text):
        """ Provide info about typing. """
        if self.language == "md":
            infoline = f"1. Type *{text}*."
        elif self.language == "html":
            infoline = f"<li>Type <em>{text}</em>.</li>"
        elif self.language == "openqa":
            infoline = f"type_very_safely('{text}');"
        return infoline

    def modrelease(self, key, needle):
        """ Provide info about modifier release. """
        if self.language == "md":
            infoline = f"1. See a follow-up ![{needle}]({needle}) for the resulting action."
        elif self.language == "html":
            infoline = f"<li>See a follow-up ![{needle}]({needle}) for the resulting action.</li>"
        return infoline
