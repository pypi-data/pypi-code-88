from psychopy import core, event, visual

from .stim import StimulusData


class Drawable:
    def __init__(
        self,
        win: visual.Window,
        stimulus_data: StimulusData,
        begin: float,
        dur: float,
    ):
        self.__stimulus_data = stimulus_data
        self.__begin = begin
        self.__end = begin + dur
        kwargs = self.__stimulus_data.kwargs
        self.__attr_funcs = {
            key: kwargs.pop(key)
            for key, val in kwargs.copy().items()
            if callable(val)
        }
        self.stimulus = self.__stimulus_data.stimulus_type(win=win, **kwargs)

    @property
    def end(self):
        return self.__end

    def draw(self, t: float):
        if self.__begin <= t < self.__end:
            for attr, func in self.__attr_funcs.items():
                setattr(self.stimulus, attr, func(t - self.__begin))

            self.stimulus.draw()


class Trial:
    """Trial for showing visual stimuli.

    :param stimuli: Visual stimuli.
    :param win: Psychopy window.
    :param dur: Duration of the trial. Inferred from ``stimuli_properties``
        if not provided.
    """

    def __init__(self, stimuli, win: visual.Window, dur: float = None):
        self.__win = win
        self.__drawables = [Drawable(win, *args) for args in stimuli]
        self.__dur: float = (
            max(map(lambda x: x.end, self.__drawables)) if dur is None else dur
        )
        self.__timer = core.Clock()

    def run(self) -> None:
        """Run trial."""
        self.__timer.reset()

        while (t := self.__timer.getTime()) < self.__dur:
            for drawable in self.__drawables:
                drawable.draw(t)

            self.__win.flip()

            if "escape" in event.getKeys():
                core.quit()
