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

HOMEFOLDER = os.getenv('HOME')
CONFIG = xdg_config_dirs[0] + '/pyverlay.conf'
ICON_DIR = '/usr/share/icons/gnome/'


class PYVERLAY(object):
    """ overlay """
    def __init__(self):
        """ Initialise the main window and start """
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/usr/share/pyverlay/pyverlay.ui")
        self.builder.connect_signals(self)
        # Load UI
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
        self.reloadbutton = self.builder.get_object("reloadbutton")
        self.optionbutton = self.builder.get_object("optionbutton")
        self.closebutton = self.builder.get_object("closebutton")
        self.current_files = None
        self.fav0 = self.builder.get_object("favbutton0")
        self.favimage0 = self.builder.get_object("image0")
        self.fav1 = self.builder.get_object("favbutton1")
        self.favimage1 = self.builder.get_object("image1")
        self.fav2 = self.builder.get_object("favbutton2")
        self.favimage2 = self.builder.get_object("image2")
        self.fav3 = self.builder.get_object("favbutton3")
        self.favimage3 = self.builder.get_object("image3")
        self.fav4 = self.builder.get_object("favbutton4")
        self.favimage4 = self.builder.get_object("image4")
        self.fav5 = self.builder.get_object("favbutton5")
        self.favimage5 = self.builder.get_object("image5")
        self.fav6 = self.builder.get_object("favbutton6")
        self.favimage6 = self.builder.get_object("image6")
        self.fav7 = self.builder.get_object("favbutton7")
        self.favimage7 = self.builder.get_object("image7")
        # Connect UI
        self.window.connect("destroy", self.quit)
        #self.activitylabel.connect("motion-notify-event", self.motion)
        self.activities.connect("motion-notify-event", self.motion)
        self.mainactivitylabel.connect("motion-notify-event", self.motion)
        self.mainactivitylabel.connect("button-press-event", self.button)
        self.activities.connect("key-release-event", self.keycatch)
        self.window.connect("key-release-event", self.keycatch)
        self.gobutton.connect("clicked", self.execute)
        self.reloadbutton.connect("clicked", self.reloadme)
        self.optionbutton.connect("clicked", self.openconf)
        self.closebutton.connect("clicked", self.quit)
        #make windows undecorated and set
        self.window.set_decorated(False)
        #self.window.fullscreen()
        self.activities.move(0,0)
        self.activities.set_keep_above(True)
        self.activities.set_decorated(False)
        self.activities.set_position(Gtk.Align.START)
        # start
        self.run()

    def run(self, *args):
        """ configure and show the main window """
        # get config info
        self.checkconfig()
        self.conf = ConfigParser.RawConfigParser()
        self.conf.read(CONFIG)
        self.favcmd0 = self.conf.get('conf', '0fav')
        self.favcmd1 = self.conf.get('conf', '1fav')
        self.favcmd2 = self.conf.get('conf', '2fav')
        self.favcmd3 = self.conf.get('conf', '3fav')
        self.favcmd4 = self.conf.get('conf', '4fav')
        self.favcmd5 = self.conf.get('conf', '5fav')
        self.favcmd6 = self.conf.get('conf', '6fav')
        self.favcmd7 = self.conf.get('conf', '7fav')
        #print dir(self.favimage0)
        if not self.favcmd0 == "":
            self.fav0.set_visible(True)
            self.fav0.connect("clicked", self.favexec)
            self.favimage0.set_from_file(self.conf.get('conf', '0favicon'))
        if not self.favcmd1 == "":
            self.fav1.set_visible(True)
            self.fav1.connect("clicked", self.favexec)
            self.favimage1.set_from_file(self.conf.get('conf', '1favicon'))
        if not self.favcmd2 == "":
            self.fav2.set_visible(True)
            self.fav2.connect("clicked", self.favexec)
            self.favimage2.set_from_file(self.conf.get('conf', '2favicon'))
        if not self.favcmd3 == "":
            self.fav3.set_visible(True)
            self.fav3.connect("clicked", self.favexec)
            self.favimage3.set_from_file(self.conf.get('conf', '3favicon'))
        if not self.favcmd4 == "":
            self.fav4.set_visible(True)
            self.fav4.connect("clicked", self.favexec)
            self.favimage4.set_from_file(self.conf.get('conf', '4favicon'))
        if not self.favcmd5 == "":
            self.fav5.set_visible(True)
            self.fav5.connect("clicked", self.favexec)
            self.favimage5.set_from_file(self.conf.get('conf', '5favicon'))
        if not self.favcmd6 == "":
            self.fav6.set_visible(True)
            self.fav6.connect("clicked", self.favexec)
            self.favimage6.set_from_file(self.conf.get('conf', '6favicon'))
        if not self.favcmd7 == "":
            self.fav7.set_visible(True)
            self.fav7.connect("clicked", self.favexec)
            self.favimage7.set_from_file(self.conf.get('conf', '7favicon'))
        #print len(self.loadselection())
        #print len(self.loadselection()) / 8.00
        #self.loadselection()
        #show windows
        self.activities.show()
        self.activities.grab_focus()
        self.window.hide()
        Gtk.main()

    def favexec(self, actor):
        if actor == self.fav0:
            subprocess.Popen(str.split(self.favcmd0))
            self.hide()
        if actor == self.fav1:
            subprocess.Popen(str.split(self.favcmd1))
            self.hide()
        if actor == self.fav2:
            subprocess.Popen(str.split(self.favcmd2))
            self.hide()
        if actor == self.fav3:
            subprocess.Popen(str.split(self.favcmd3))
            self.hide()
        if actor == self.fav4:
            subprocess.Popen(str.split(self.favcmd4))
            self.hide()
        if actor == self.fav5:
            subprocess.Popen(str.split(self.favcmd5))
            self.hide()
        if actor == self.fav6:
            subprocess.Popen(str.split(self.favcmd6))
            self.hide()
        if actor == self.fav7:
            subprocess.Popen(str.split(self.favcmd7))
            self.hide()

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
        test_mask = (event.state & Gdk.ModifierType.SUPER_MASK ==
                       Gdk.ModifierType.SUPER_MASK)
        if event.get_state() and test_mask:
            self.showorhide()

    def motion(self, actor, event):
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
        """ show overlay window """
        #self.window.fullscreen()
        self.window.maximize()
        self.window.show()
        self.activities.set_keep_above(True)
        self.runentry.grab_focus()
        return

    def hide(self, *args):
        """ hide overlay window """
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

    def checkconfig(self):
        """ create a default config if not available """
        if not os.path.isfile(CONFIG):
            conffile = open(CONFIG, "w")
            conffile.write("[conf]\n0fav = xdg-open " + os.getenv('HOME') +
                           " \n0favicon = /usr/share/icons/gnome/24x24/places" +
                           "/folder_home.png\n1fav = xdg-open xterm\n1favi" +
                           "con = /usr/share/icons/gnome/24x24/apps/termin" +
                           "al.png\n2fav = /usr/bin/gedit\n2favicon = /usr" +
                           "/share/icons/gnome/24x24/apps/text-editor.png\n" +
                           "3fav = \n3favicon = \n4fav = \n4favicon = \n5f" +
                           "av = \n5favicon = \n6fav = \n6favicon = \n7fav" +
                           " = \n7favicon = \n")
            conffile.close()
        return

    def openconf(self, *args):
        self.checkconfig()
        subprocess.Popen(['/usr/bin/xdg-open', CONFIG])
        self.hide()

    def reloadme(self, event):
        self.run()

if __name__ == "__main__":
    PYVERLAY()
