import asyncio
import hashlib
import os
import re

from pytgcalls import PyTgCalls

from .exceptions import *

IS_WINDOWS = os.name == "nt"


class Wrapper:
    def __init__(self, pytgcalls: PyTgCalls, raw_dir: str = "./", ffmpeg: str = "ffmpeg", youtube_dl: str = "youtube-dl"):
        self.pytgcalls = pytgcalls
        self.raw_dir = raw_dir
        self.ffmpeg = ffmpeg
        self.youtube_dl = youtube_dl

    def _is_youtube_link(self, s: str) -> bool:
        return bool(re.match(f"^(http|https)://((youtu\.be/.+)|(youtube\.com/watch\?v=.+))$", s))

    def _get_output(self, input: str):
        return os.path.join(self.raw_dir,  hashlib.md5(input.encode()).hexdigest())

    def _get_ffmpeg_cmd(self, input: str):
        return f"{self.ffmpeg} -y -i {input} -f s16le -ac 1 -ar 48000 -acodec pcm_s16le {self._get_output(input)}"

    def _get_youtube_dl_cmd(self, input: str):
        return f"{self.youtube_dl} -x -g \"{input}\""

    async def _solve_input(self, input: str):
        if self._is_youtube_link(input):
            prc = await asyncio.create_subprocess_shell(self._get_youtube_dl_cmd(input), stdout=asyncio.subprocess.PIPE)
            out, _ = await prc.communicate()

            if prc.returncode != 0:
                raise YouTubeDLError(
                    f"Got a non-zero return code: {prc.returncode}")

            return f"\"{out.decode().strip()}\""

        return input

    def _make_sure_in_call(self, chat_id: int):
        if chat_id not in self.pytgcalls.active_calls:
            raise NotInCall

    async def convert(self, input: str) -> str:
        input = await self._solve_input(input)
        output = self._get_output(input)

        if os.path.isfile(output):
            return output

        cmd = self._get_ffmpeg_cmd(input)
        prc = await asyncio.create_subprocess_shell(cmd, stdin=asyncio.subprocess.PIPE, stdout=None, stderr=asyncio.subprocess.PIPE)

        await prc.communicate()

        if prc.returncode != 0:
            raise FFmpegError(f"Got a non-zero return code: {prc.returncode}")

        return output

    async def stream(self, chat_id: int, file: str):
        if chat_id in self.pytgcalls.active_calls:
            self.pytgcalls.change_stream(chat_id, await self.convert(file))
        else:
            self.pytgcalls.join_group_call(chat_id, await self.convert(file))

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


__all__ = ["Wrapper"]
