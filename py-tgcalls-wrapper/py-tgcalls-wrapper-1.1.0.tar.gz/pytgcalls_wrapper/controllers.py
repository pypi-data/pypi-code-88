from .wrapper_base import WrapperBase
from .exceptions import NotPlaying, NotPaused


class SyncController(WrapperBase):
    def pause(self, chat_id: int):
        self._make_sure_in_call(chat_id)

        if self.pytgcalls.active_calls[chat_id] != "playing":
            raise NotPlaying

        self.pytgcalls.pause_stream(chat_id)

    def resume(self, chat_id: int):
        self._make_sure_in_call(chat_id)

        if self.pytgcalls.active_calls[chat_id] != "paused":
            raise NotPaused

        self.pytgcalls.resume_stream(chat_id)


class AsyncController(SyncController):
    pass
