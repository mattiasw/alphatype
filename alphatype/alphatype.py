#!/usr/bin/env python3
# This file is part of Alphatype.
# http://github.com/mattiasw/alphatype
# Copyright (C) 2018  Mattias Wallander <mattias@wallander.eu>
#
# Alphatype is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Alphatype is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Alphatype. If not, see <https://www.gnu.org/licenses/>.

import sys


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(
            description='Measure how fast you type the alphabet.',
    )
    parser.add_argument(
            '-a',
            '--alphabet',
            default='en',
            help='use alphabet ALPHABET, e.g. sv (default is en)',
    )
    return parser.parse_args()


def main(letters, alphabet_name='English'):
    from timer import Timer
    import getch
    while True:
        timer = Timer()
        print('Print the {} alphabet as fast as you can.'.format(alphabet_name))
        was_correct = alphatype(letters, getch.getch, timer)
        if was_correct:
            print('\nFinished in {} seconds.\n'.format(round(timer.time, 2)))
        else:
            print('\nWrong letter!\n')


def alphatype(character_sequence, get_next_character, timer, echo=True):
    first_input = True
    for correct_character in character_sequence:
        typed_character = get_next_character(echo)
        if first_input:
            timer.start()
            first_input = False
        if typed_character != correct_character:
            return False
    timer.stop()
    return True


if __name__ == '__main__':
    args = parse_args()
    try:
        if args.alphabet == 'sv':
            main('abcdefghijklmnopqrstuvwxyzåäö', alphabet_name='Swedish')
        else:
            main('abcdefghijklmnopqrstuvwxyz')
    except (KeyboardInterrupt, EOFError):
        print('\nExiting...')
