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

import unittest
from unittest import mock
from alphatype.alphatype import alphatype


class AlphatypeTests(unittest.TestCase):
    """Tests for the Alphatype program."""

    class Timer:
        time = 0
        start = mock.Mock()
        stop = mock.Mock()

        def tick(self, time):
            self.time += time

        def get_time(self):
            return self.time

    def create_getch(self, characters, timer=mock.Mock()):
        first_input = True

        def get_next_character():
            nonlocal characters, first_input

            next_character = characters[0]
            characters = characters[1:]
            if not first_input:
                timer.tick(1)
            first_input = False

            return next_character

        return get_next_character

    def test_handles_correct_sequence_of_characters(self):
        """Returns true for correct sequence of characters."""
        self.assertTrue(alphatype(
                'ab',
                self.create_getch('ab'),
                mock.Mock(),
                silent=True,
        ))

    def test_handles_faulty_sequence_of_characters(self):
        """Returns false for incorrect sequence of characters."""
        self.assertFalse(alphatype(
                'abc',
                self.create_getch('ac'),
                mock.Mock(),
                silent=True,
        ))

    def test_start_and_stop_timer(self):
        """Starts and stops timer."""
        timer = self.Timer()
        alphatype(
                'abcdef',
                self.create_getch('abcdef', timer),
                timer,
                silent=True,
        )
        timer.start.assert_called_once_with()
        timer.stop.assert_called_once_with()
        self.assertEqual(timer.get_time(), 5)


if __name__ == '__main__':
    unittest.main()
