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
    import timer
    import getch
    timer = timer.Timer()
    print('Print the {} alphabet as fast as you can.'.format(alphabet_name))
    was_correct = alphatype(letters, getch.getch, timer)
    if was_correct:
        print('\nFinished in {} seconds.'.format(round(timer.time, 2)))
    else:
        print('\nWrong letter!')


def alphatype(character_sequence, get_next_character, timer, silent=False):
    first_input = True
    while character_sequence:
        next_character = get_next_character()
        if not silent:
            print(next_character, end='')
            sys.stdout.flush()
        if first_input:
            timer.start()
            first_input = False
        if next_character != character_sequence[0]:
            return False
        character_sequence = character_sequence[1:]
    timer.stop()
    return True


if __name__ == '__main__':
    args = parse_args()
    if args.alphabet == 'sv':
        main('abcdefghijklmnopqrstuvwxyzåäö', alphabet_name='Swedish')
    else:
        main('abcdefghijklmnopqrstuvwxyz')
