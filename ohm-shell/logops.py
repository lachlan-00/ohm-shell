#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Modified from Rhythmbox Fileorganizer logops.py

    ----------------Authors----------------
    Lachlan de Waard <lachlan.00@gmail.com>
    ----------------Licence----------------
    GNU General Public License version 3

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


import os
import codecs


# Write to log file
def write(path, logmessage):
    """ Perform log operations """
    # Create if missing
    print('Writing to log file: ' + path)
    print(logmessage)
    print()
    if not os.path.exists(path) or (os.path.getsize(path) >= 1076072):
        files = codecs.open(path, "w", "utf8")
        files.close()
    files = codecs.open(path, "a", "utf8")
    logline = []
    logline.append(logmessage)
    files.write(("".join(logline)) + "\n")
    files.close()
    return True
