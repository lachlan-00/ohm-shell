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

import os

def checkconfig(inputpath):
    """ create a default config if not available """
    if not os.path.isfile(inputpath):
        conffile = open(inputpath, "w")
        conffile.write("[conf]\n\n# Shortcut bar: Enter the command then the" +
                       " icon path\n0fav = nautilus\n0favicon = /usr/share/i" +
                       "cons/gnome/48x48/places/user-home.png\n1fav = x-term" +
                       "inal-emulator\n1favicon = /usr/share/icons/gnome/48x" +
                       "48/apps/utilities-terminal.png\n2fav = x-www-browser" +
                       "\n2favicon = /usr/share/icons/gnome/48x48/apps/web-b" +
                       "rowser.png\n3fav = \n3favicon = \n4fav = \n4favicon " +
                       "= \n5fav = \n5favicon = \n6fav = \n6favicon = \n7fav" +
                       " = \n7favicon = \n8fav = \n8favicon = \n9fav = \n9fa" +
                       "vicon = \n10fav = \n10favicon = \n11fav = \n11favico" +
                       "n = \n12fav = \n12favicon = \n13fav = \n13favicon = " +
                       "\n14fav = \n14favicon = \n15fav = \n15favicon = \n16" +
                       "fav = \n16favicon = \n17fav = \n17favicon = \n18fav " +
                       "= \n18favicon = \n19fav = \n19favicon = \n\n# autost" +
                       "art allows multiple commands 4 space separated. ('  " +
                       "')\nautostart = \n\n# Show open windows on the left " +
                       "or right side of the main window\n# Options (left, r" +
                       "ight or centre)\nappposition = left\n\n#Show or hide" +
                       " the hot corner label\nshowhotlabel = False\n")
        conffile.close()
        return
