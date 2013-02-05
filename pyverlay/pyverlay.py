#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pyverly
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

import shutil
import os
import random
import mimetypes
import ConfigParser

from gi.repository import Gtk
from gi.repository import Gdk
from xdg.BaseDirectory import xdg_config_dirs


LIBRARYSTYLE = ['Artist', 'Album', 'Track']
HOMEFOLDER = os.getenv('HOME')
DISKFREE = True
TOTALCOUNT = 0
CONFIG = xdg_config_dirs[0] + '/usyncp3.conf'
ICON_DIR = '/usr/share/icons/gnome/'


class PYVERLAY(object):
    """ overlay """
    def __init__(self):
        """ Initialise the main window and start """
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/usr/share/pyverlay/pyverlay.ui")
        self.builder.connect_signals(self)
        # main window
        self.window = self.builder.get_object("main_window")
        self.activities = self.builder.get_object("hot_corner")
        self.fileview = self.builder.get_object("fileview")
        self.contentlist = self.builder.get_object('filestore')
        self.contenttree = self.builder.get_object('fileview')
        self.closebutton = self.builder.get_object("closebutton")
        self.current_files = None
        # start
        self.run()

    def run(self, *args):
        """ Connect events and show the main window """
        self.window.connect("destroy", self.quit)
        self.activities.connect("motion-notify-event", self.motion)
        self.activities.connect("key-release-event", self.keycatch)
        self.window.connect("key-release-event", self.keycatch)
        self.closebutton.connect("clicked", self.quit)
        # set up file and folder lists
        cell = Gtk.CellRendererText()
        filecolumn = Gtk.TreeViewColumn("Select Files", cell, text=0)
        self.fileview.connect("row-activated", self.loadselection)
        self.contenttree.append_column(filecolumn)
        self.contenttree.set_model(self.contentlist)
        print len(self.loadselection())
        self.activities.show()
        self.window.show()
        Gtk.main()

    def keycatch(self, actor, event):
        test_mask = (event.state & Gdk.ModifierType.SUPER_MASK ==
                       Gdk.ModifierType.SUPER_MASK)
        #print dir(Gdk.ModifierType)
        #print event.state & Gdk.ModifierType.SUPER_MASK
        if event.get_state() and test_mask:
            if self.window.get_visible():
                self.hide()
            elif self.window.get_visible():
                self.show()

    def motion(self, actor, event):
        #print dir(event.state)
        #print dir(Gdk.ModifierType)
        test_mask = (event.state & Gdk.ModifierType.META_MASK ==
                       Gdk.ModifierType.META_MASK)
        print event.get_state()
        return

    def show(self, *args):
        """ fill and show the config window """
        self.window.show()
        return

    def hide(self, *args):
        """ hide the config window """
        self.window.hide()
        return

    def quit(self, *args):
        """ stop the process thread and close the program"""
        self.window.destroy()
        Gtk.main_quit(*args)
        return False

    def loadselection(self, *args):
        """ load selected files into tag editor """
        self.current_files = []
        if args:
            if os.path.isdir(args[0]):
                current_dir = args[0]
        else:
            current_dir = ['/usr/share/applications']
        for items in current_dir:
            filelist = os.listdir(items)
            filelist.sort(key=lambda y: y.lower())
            for files in filelist:
                if files[(files.rfind('.')):] == '.desktop':
                    self.current_files.append(items + '/' + files)
        #model, fileiter = self.contenttree.get_selection().get_selected_rows()
        #for files in fileiter:
        #    tmp_file = current_dir + '/' + model[files][0]
        #    self.current_files.append(tmp_file)
        return self.current_files

if __name__ == "__main__":
    PYVERLAY()
