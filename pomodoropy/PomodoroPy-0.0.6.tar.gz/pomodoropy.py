#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# <https://en.wikipedia.org/wiki/Pomodoro_Technique>

import argparse
import subprocess
import sys
import time

from streaminput import streaminput


class Pomodoro(object):

    tag = None
    timestamp = None
    task = None
    interval = None
    rating = None
    comment = None

    def __init__(self, args):
        self.interactive = args.interactive
        self.timeout = args.timeout
        self.work = args.work
        self.rest = args.rest
        self.voice = args.voice

    def session(self):
        try:
            while True:
                self.interval = 0
                # step 1. pick a task
                self.task = input("💡 What's your task for the Pomodoro?\n  ")
                self.tag = streaminput('📌 Would you like to put a tag on it? Press Enter to skip.\n  ', self.timeout)
                # step 2. set a timer for work, focus on work until time is up
                # rate your focus in the end
                if self.interactive:
                    self.work = int(input('⏰ How long (in minutes) would you like to work? Input an integer.\n  '))
                print('🍅 Please focus on work for {} minutes, press Ctrl+C to abort.'.format(self.work))
                self.timer('🍅', self.work, self.voice, "It's time to have a rest.")
                self.interval += self.work
                self.rating = input('🎉 How was your focus (1-10)?\n  ')
                # step 3. make any comments
                self.comment = streaminput('💭 Would you like to make any comments? Press Enter to skip.\n  ', self.timeout)
                # step 4. log the pomodoro
                self.save(self.tag, self.task, self.interval, self.rating, self.comment)
                # step 5. set a timer for rest, have a rest until time is up
                if self.interactive:
                    self.rest = int(input('⏰ How long (in minutes) would you like to rest? Input an integer.\n  '))
                print('🥝 Please have a rest for {} minutes, press Ctrl+C to abort.'.format(self.rest))
                self.timer('🥝', self.rest, self.voice, "It's time to focus on work.")
                # step 6. press Enter to repeat step 1-5
                input('🙈🙉🙊 Press Enter to continue...\n')
        except KeyboardInterrupt:
            print('\n💪 Well done!')

    @staticmethod
    def timer(prog, interval, voice, message):
        secs = interval * 60
        since = time.time()
        while True:
            secs_elapsed = time.time() - since
            secs_left = secs - secs_elapsed
            if secs_left <= 0:
                print('')
                break
            Pomodoro.progressbar(prog, secs_elapsed, secs, extra=Pomodoro.countdown(secs_left))
            time.sleep(1)
        Pomodoro.notify(prog, voice, message)

    @staticmethod
    def countdown(secs_left):
        mins, secs = divmod(round(secs_left), 60)
        return '{:02d}:{:02d} ⏰'.format(mins, secs)

    @staticmethod
    def progressbar(prog, secs_elapsed, secs, extra=''):
        if prog == '🍅':
            length = 25
        elif prog == '🥝':
            length = 5
        frac = secs_elapsed / secs
        loaded = round(frac * length)
        print('\r ', prog * loaded + '--' * (length - loaded), '[{:.0%}]'.format(frac), extra, end='')

    @staticmethod
    def notify(prog, voice, message):
        try:
            # macOS voice notification
            if sys.platform == 'darwin':
                subprocess.run(['terminal-notifier', '-title', prog, '-message', message])
                subprocess.run(['say', '-v', voice, message])
            else:
                # TODO
                pass
        except:
            # TODO
            pass

    @staticmethod
    def save(tag, task, interval, rating, comment, file='./pomodoro.log'):
        timestamp = time.strftime('%a %d %b %Y %H:%M:%S', time.localtime())
        entries = []
        print('😀 {} | ✅ Task: #{} {} | 🍅 Pomodoro: {} minutes | 👉 Self-Rating: {} | 💭 Comment: {}'.format(
            timestamp, tag, task, interval, '⭐' * int(rating), comment)
        )
        entries += [timestamp, tag, task, str(interval), rating, comment]
        with open(file, 'a') as f:
            f.write(' | '.join(entries))
            f.write('\n')

    def add_argparse_args():
        parser = argparse.ArgumentParser(
            prog='🍅',
            description='🍅 Pomodoro timer',
            epilog='Done is Better than Perfect.'
        )
        parser.add_argument(
            '-i',
            '--interactive',
            default=True,
            action='store_false',
            help='whether or not to start session with interactive mode, default: True'
        )
        parser.add_argument(
            '-t',
            '--timeout',
            default=60,
            type=int,
            help='time out (in seconds) for rating, default: 60 seconds'
        )
        parser.add_argument(
            '-w',
            '--work',
            default=25,
            type=int,
            help='time interval (in minutes) for work, default: 25 minutes'
        )
        parser.add_argument(
            '-r',
            '--rest',
            default=5,
            type=int,
            help='time interval (in minutes) for rest, default: 5 minutes'
        )
        parser.add_argument(
            '-v',
            '--voice',
            default='Alex',
            type=str,
            help='voice notification sound, default: Alex'
        )
        return parser

    @classmethod
    def from_argparse_args(cls, args):
        return cls(args)


def parse_args():
    parser = Pomodoro.add_argparse_args()
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    pomodoro = Pomodoro.from_argparse_args(args)
    pomodoro.session()


if __name__ == '__main__':
    main()
