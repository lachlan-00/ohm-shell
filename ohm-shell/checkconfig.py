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
        conffile.write("[conf]\n\n# Shortcut bar: Enter the command the" +
                       "n the icon path\n0fav = xdg-open /home/user\n0f" +
                       "avicon = /usr/share/icons/gnome/48x48/places/fo" +
                       "lder_home.png\n1fav = gnome-terminal\n1favicon " +
                       "= /usr/share/icons/gnome/48x48/apps/terminal.pn" +
                       "g\n2fav = gedit\n2favicon = /usr/share/icons/gn" +
                       "ome/48x48/apps/text-editor.png\n3fav = gksu syn" +
                       "aptic\n3favicon = /usr/share/pixmaps/synaptic.p" +
                       "ng\n4fav = rhythmbox\n4favicon = /usr/share/ico" +
                       "ns/hicolor/48x48/apps/rhythmbox.png\n5fav = tot" +
                       "em\n5favicon = /usr/share/icons/hicolor/48x48/a" +
                       "pps/totem.png\n6fav = \n6favicon = \n7fav = \n7" +
                       "favicon = \n8fav = gnome-control-center\n8favic" +
                       "on = /usr/share/pixmaps/gnome-control-center.xp" +
                       "m\n9fav = \n9favicon =\n10fav = \n10favicon =\n" +
                       "11fav = \n11favicon =\n12fav = \n12favicon =\n1" +
                       "3fav = \n13favicon =\n14fav = \n14favicon =\n15" +
                       "fav = \n15favicon =\n16fav = \n16favicon =\n17f" +
                       "av = \n17favicon =\n18fav = \n18favicon =\n19fa" +
                       "v = \n19favicon =\n\n# autostart allows multipl" +
                       "e commands 4 space separated. ('    ')\nautosta" +
                       "rt = \n# Show open windows on the left or right" +
                       " side of the main window\n# Options (left, righ" +
                       "t or centre)\nappposition = centre\n\n#Show or " +
                       "hide the hot corner label\nshowhotlabel = True\n")
        conffile.close()
        return
