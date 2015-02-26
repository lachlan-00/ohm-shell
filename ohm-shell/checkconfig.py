#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" checkconfig
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

#import os

#ConfigParser renamed for python3
try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser


def checkconfig(inputpath):
    """ create a default config if not available """
    conf = ConfigParser.RawConfigParser()
    conf.read(inputpath)
    if not conf.has_section('dock'):
        count = 0
        print('CHECKCONFIG: adding dock')
        conffile = open(inputpath, "w")
        conf.add_section('dock')
        while count < 20:
            conf.set('dock', str(count) + 'fav', '')
            conf.set('dock', str(count) + 'icon', '')
            count = count + 1
        conf.write(conffile)
        conffile.close()
    if not conf.has_section('options'):
        conffile = open(inputpath, "w")
        print('CHECKCONFIG: adding options')
        conf.add_section('options')
        conf.set('options', 'autostart', '')
        conf.set('options', 'appposition', 'centre')
        conf.set('options', 'showhotlabel', 'True')
        conf.write(conffile)
        conffile.close()
        return

def checksetting(inputpath, settingid, setting):
    """ try to identify the default icon theme path """
    conf = ConfigParser.RawConfigParser()
    conf.read(inputpath)
    try:
        name = conf.get(settingid, setting)
    except ConfigParser.NoOptionError:
        return None
    return name

def changesetting(inputpath, settingid, setting, value):
    """ set values for settings """
    conf = ConfigParser.RawConfigParser()
    conf.read(inputpath)
    conf.set(settingid, setting, value)
    conffile = open(inputpath, "w")
    conf.write(conffile)
    conffile.close()
    return

def checkdesktopfile(inputfile):
    """ get basic information from the selected desktop file """
    return inputfile
