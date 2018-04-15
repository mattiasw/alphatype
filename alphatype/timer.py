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

import time


class Timer:
    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.time = time.perf_counter() - self.start_time
