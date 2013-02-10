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
import time
import ConfigParser
import subprocess

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
        self.activitylabel = self.builder.get_object("mainlabel")
        self.mainactivitylabel = self.builder.get_object("mainlabel")
        self.runentry = self.builder.get_object("runentry")
        self.appgrid = self.builder.get_object("app_grid")
        self.fileview = self.builder.get_object("fileview")
        self.contentlist = self.builder.get_object('filestore')
        self.contenttree = self.builder.get_object('fileview')
        self.gobutton = self.builder.get_object("gobutton")
        self.closebutton = self.builder.get_object("closebutton")
        self.current_files = None
        # start
        self.run()

    def run(self, *args):
        """ Connect events and show the main window """
        self.window.connect("destroy", self.quit)
        #self.activitylabel.connect("motion-notify-event", self.motion)
        self.activities.connect("motion-notify-event", self.motion)
        self.mainactivitylabel.connect("motion-notify-event", self.motion)
        self.mainactivitylabel.connect("button-press-event", self.button)
        self.activities.connect("key-release-event", self.keycatch)
        self.window.connect("key-release-event", self.keycatch)
        self.gobutton.connect("clicked", self.execute)
        self.closebutton.connect("clicked", self.quit)
        # set up file and folder lists
        ##cell = Gtk.CellRendererText()
        ##filecolumn = Gtk.TreeViewColumn("Select Files", cell, text=0)
        ##self.fileview.connect("row-activated", self.loadselection)
        ##self.contenttree.append_column(filecolumn)
        ##self.contenttree.set_model(self.contentlist)
        print len(self.loadselection())
        print len(self.loadselection()) / 8.00
        self.loadselection()
        #make windows undecorated and set
        self.window.set_decorated(False)
        #self.window.fullscreen()
        self.activities.move(0,0)
        self.activities.set_keep_above(True)
        self.activities.set_decorated(False)
        self.activities.set_position(Gtk.Align.START)
        #show windows
        self.activities.show()
        self.activities.grab_focus()
        #self.window.show()
        Gtk.main()

    def execute(self, *args):
        subprocess.Popen(str.split(self.runentry.get_text()))
        self.runentry.set_text("")
        self.hide()

    def keycatch(self, actor, event):
        print event.get_keycode()[1]
        test_mask = (event.state & Gdk.ModifierType.SUPER_MASK ==
                       Gdk.ModifierType.SUPER_MASK)
        if event.get_state() and test_mask:
            self.showorhide()
        elif event.get_keycode()[1] == 36:
            self.execute()

    def button(self, actor, event):
        print 'buttonpress'
        test_mask = (event.state & Gdk.ModifierType.SUPER_MASK ==
                       Gdk.ModifierType.SUPER_MASK)
        if event.get_state() and test_mask:
            self.showorhide()

    def motion(self, actor, event):
        #print self.activities.get_pointer()
        if self.activities.get_pointer()[0] == 0 and (
                self.activities.get_pointer()[1] == 0):
            self.showorhide()
        return

    def showorhide(self, *args):
        if self.window.get_visible():
            self.hide()
        elif not self.window.get_visible():
            self.show()
        time.sleep(1)

    def show(self, *args):
        """ fill and show the config window """
        #self.window.fullscreen()
        self.window.maximize()
        self.window.show()
        self.activities.set_keep_above(True)
        self.runentry.grab_focus()
        return

    def hide(self, *args):
        """ hide the config window """
        self.window.set_keep_above(False)
        self.activities.set_keep_above(True)
        self.window.hide()
        return

    def quit(self, *args):
        """ stop the process thread and close the program"""
        self.activities.destroy()
        self.window.destroy()
        Gtk.main_quit(*args)
        return False

    def loadselection(self, *args):
        """ load selected files into the list """
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
