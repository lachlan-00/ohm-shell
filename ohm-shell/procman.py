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

import os
import psutil
import subprocess

import logops

LOGFILE = os.getenv('HOME') + '/.ohm-shell.log'

def startprocess(proclist):
    """ start process returning the pid """
    pid = None
    try:
        pid = subprocess.Popen(proclist).pid
    except OSError as e:
        #no file found
        logops.write(LOGFILE, 'PROCMAN: No File Found')
        logops.write(LOGFILE, str(e))
        return False
    except TypeError as e:
        #malformed entry
        logops.write(LOGFILE, 'PROCMAN: Bad file name')
        logops.write(LOGFILE, str(e))
        return False
    #process.wait()
    tmpproc = getprocesses()
    for proc in tmpproc:
        ###debug###print(str(pid) + ' - ' + str(proc))
        if proc[0] == pid:
            return proc
    return False

def getprocesses():
    """ identify process by the pid """
    proclist = []
    for proc in psutil.process_iter():
        xpid = proc.pid
        xname = proc.name
        xproc = proc.cmdline
        proclist.append([xpid, xname, xproc])
    return proclist
