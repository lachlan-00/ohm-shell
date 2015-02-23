#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" procman
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

import subprocess

def startprocess(proclist):
    """ start process returning the pid """
    process = None
    pid = None
    try:
        process = subprocess.Popen(proclist)
        pid = process.pid
    except OSError:
        #no file found
        print('STARTPROCESS: No File Found')
        return False
    except TypeError:
        #malformed entry
        print('STARTPROCESS: Bad file name')
        return False
    #process.wait()
    return pid
