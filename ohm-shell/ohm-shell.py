#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" OHM-shell
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
import time
import ConfigParser
import subprocess

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Wnck
from xdg.BaseDirectory import xdg_config_dirs

HOMEFOLDER = os.getenv('HOME')
CONFIG = xdg_config_dirs[0] + '/ohm-shell.conf'
HIDELIST = ['ohm-shell.py', 'Desktop', 'xfce4-panel', 'xfce4-notifyd']


class OHMSHELL(object):
    """ OHM-shell overlay """
    def __init__(self):
        """ Initialise the main window and start the program """
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/usr/share/ohm-shell/ohm-shell.ui")
        self.builder.connect_signals(self)
        self.conf = ConfigParser.RawConfigParser()
        # Load primary windows, labels and button objects
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
        self.timelabel = self.builder.get_object("timelabel")
        self.reloadbutton = self.builder.get_object("reloadbutton")
        self.optionbutton = self.builder.get_object("optionbutton")
        self.restartbutton = self.builder.get_object("restartbutton")
        self.haltbutton = self.builder.get_object("haltbutton")
        self.closebutton = self.builder.get_object("closebutton")
        # Load dock icon and button objects
        self.window0 = self.builder.get_object("windowimage0")
        self.window1 = self.builder.get_object("windowimage1")
        self.window2 = self.builder.get_object("windowimage2")
        self.window3 = self.builder.get_object("windowimage3")
        self.window4 = self.builder.get_object("windowimage4")
        self.window5 = self.builder.get_object("windowimage5")
        self.window6 = self.builder.get_object("windowimage6")
        self.window7 = self.builder.get_object("windowimage7")
        self.window8 = self.builder.get_object("windowimage8")
        self.window9 = self.builder.get_object("windowimage9")
        self.window10 = self.builder.get_object("windowimage10")
        self.window11 = self.builder.get_object("windowimage11")
        self.window12 = self.builder.get_object("windowimage12")
        self.window13 = self.builder.get_object("windowimage13")
        self.window14 = self.builder.get_object("windowimage14")
        self.window15 = self.builder.get_object("windowimage15")
        self.window16 = self.builder.get_object("windowimage16")
        self.window17 = self.builder.get_object("windowimage17")
        self.window18 = self.builder.get_object("windowimage18")
        self.window19 = self.builder.get_object("windowimage19")
        self.dockbutton0 = self.builder.get_object("dockbutton0")
        self.dockbutton1 = self.builder.get_object("dockbutton1")
        self.dockbutton2 = self.builder.get_object("dockbutton2")
        self.dockbutton3 = self.builder.get_object("dockbutton3")
        self.dockbutton4 = self.builder.get_object("dockbutton4")
        self.dockbutton5 = self.builder.get_object("dockbutton5")
        self.dockbutton6 = self.builder.get_object("dockbutton6")
        self.dockbutton7 = self.builder.get_object("dockbutton7")
        self.dockbutton8 = self.builder.get_object("dockbutton8")
        self.dockbutton9 = self.builder.get_object("dockbutton9")
        self.dockbutton10 = self.builder.get_object("dockbutton10")
        self.dockbutton11 = self.builder.get_object("dockbutton11")
        self.dockbutton12 = self.builder.get_object("dockbutton12")
        self.dockbutton13 = self.builder.get_object("dockbutton13")
        self.dockbutton14 = self.builder.get_object("dockbutton14")
        self.dockbutton15 = self.builder.get_object("dockbutton15")
        self.dockbutton16 = self.builder.get_object("dockbutton16")
        self.dockbutton17 = self.builder.get_object("dockbutton17")
        self.dockbutton18 = self.builder.get_object("dockbutton18")
        self.dockbutton19 = self.builder.get_object("dockbutton19")
        self.docklabel0 = self.builder.get_object("docklabel0")
        self.docklabel1 = self.builder.get_object("docklabel1")
        self.docklabel2 = self.builder.get_object("docklabel2")
        self.docklabel3 = self.builder.get_object("docklabel3")
        self.docklabel4 = self.builder.get_object("docklabel4")
        self.docklabel5 = self.builder.get_object("docklabel5")
        self.docklabel6 = self.builder.get_object("docklabel6")
        self.docklabel7 = self.builder.get_object("docklabel7")
        self.docklabel8 = self.builder.get_object("docklabel8")
        self.docklabel9 = self.builder.get_object("docklabel9")
        self.docklabel10 = self.builder.get_object("docklabel10")
        self.docklabel11 = self.builder.get_object("docklabel11")
        self.docklabel12 = self.builder.get_object("docklabel12")
        self.docklabel13 = self.builder.get_object("docklabel13")
        self.docklabel14 = self.builder.get_object("docklabel14")
        self.docklabel15 = self.builder.get_object("docklabel15")
        self.docklabel16 = self.builder.get_object("docklabel16")
        self.docklabel17 = self.builder.get_object("docklabel17")
        self.docklabel18 = self.builder.get_object("docklabel18")
        self.docklabel19 = self.builder.get_object("docklabel19")
        # Dock lists to update buttons and images together
        self.screen = Wnck.Screen.get_default()
        self.screen.force_update()
        self.windowlist = self.screen.get_windows()
        self.dock = [[self.window0, self.dockbutton0, self.docklabel0],
                     [self.window1, self.dockbutton1, self.docklabel1],
                     [self.window2, self.dockbutton2, self.docklabel2],
                     [self.window3, self.dockbutton3, self.docklabel3],
                     [self.window4, self.dockbutton4, self.docklabel4],
                     [self.window5, self.dockbutton5, self.docklabel5],
                     [self.window6, self.dockbutton6, self.docklabel6],
                     [self.window7, self.dockbutton7, self.docklabel7],
                     [self.window8, self.dockbutton8, self.docklabel8],
                     [self.window9, self.dockbutton9, self.docklabel9],
                     [self.window10, self.dockbutton10, self.docklabel10],
                     [self.window11, self.dockbutton11, self.docklabel11],
                     [self.window12, self.dockbutton12, self.docklabel12],
                     [self.window13, self.dockbutton13, self.docklabel13],
                     [self.window14, self.dockbutton14, self.docklabel14],
                     [self.window15, self.dockbutton15, self.docklabel15],
                     [self.window16, self.dockbutton16, self.docklabel16],
                     [self.window17, self.dockbutton17, self.docklabel17],
                     [self.window18, self.dockbutton18, self.docklabel18],
                     [self.window19, self.dockbutton19, self.docklabel19]]
        # Shortcuts, buttons and images to connect from config
        self.fav0 = self.builder.get_object("favbutton0")
        self.fav1 = self.builder.get_object("favbutton1")
        self.fav2 = self.builder.get_object("favbutton2")
        self.fav3 = self.builder.get_object("favbutton3")
        self.fav4 = self.builder.get_object("favbutton4")
        self.fav5 = self.builder.get_object("favbutton5")
        self.fav6 = self.builder.get_object("favbutton6")
        self.fav7 = self.builder.get_object("favbutton7")
        self.fav8 = self.builder.get_object("favbutton8")
        self.fav9 = self.builder.get_object("favbutton9")
        self.favimage0 = self.builder.get_object("image0")
        self.favimage1 = self.builder.get_object("image1")
        self.favimage2 = self.builder.get_object("image2")
        self.favimage3 = self.builder.get_object("image3")
        self.favimage4 = self.builder.get_object("image4")
        self.favimage5 = self.builder.get_object("image5")
        self.favimage6 = self.builder.get_object("image6")
        self.favimage7 = self.builder.get_object("image7")
        self.favimage8 = self.builder.get_object("image8")
        self.favimage9 = self.builder.get_object("image9")
        self.favcmd0 = None
        self.favcmd1 = None
        self.favcmd2 = None
        self.favcmd3 = None
        self.favcmd4 = None
        self.favcmd5 = None
        self.favcmd6 = None
        self.favcmd7 = None
        self.favcmd8 = None
        self.favcmd9 = None
        self.autostart = None
        # Connect UI
        self.window.connect("destroy", self.quit)
        self.window.connect("key-release-event", self.keycatch)
        self.window.connect("motion-notify-event", self.motion)
        self.activities.connect("motion-notify-event", self.motion)
        self.activities.connect("key-release-event", self.keycatch)
        #self.activities.connect("button-release-event", self.button)
        #self.mainactivitylabel.connect("button-release-event", self.button)
        self.mainactivitylabel.connect("motion-notify-event", self.motion)
        self.gobutton.connect("clicked", self.execute)
        self.reloadbutton.connect("clicked", self.reloadme)
        self.optionbutton.connect("clicked", self.openconf)
        self.restartbutton.connect("clicked", self.execute)
        self.haltbutton.connect("clicked", self.execute)
        self.closebutton.connect("clicked", self.quit)
        # make windows undecorated and set options
        self.window.set_decorated(False)
        self.activities.set_decorated(False)
        self.activities.set_skip_taskbar_hint(True)
        self.activities.set_skip_pager_hint(True)
        self.activities.set_keep_above(True)
        self.activities.move(0, 0)
        self.activities.set_position(Gtk.Align.START)
        # start
        self.run()
        # run autostart commands
        self.execute("autostart")
        Gtk.main()

    def run(self, *args):
        """ configure and show the main window """
        # get config info
        self.checkconfig()
        self.conf.read(CONFIG)
        self.favcmd0 = self.conf.get('conf', '0fav')
        self.favcmd1 = self.conf.get('conf', '1fav')
        self.favcmd2 = self.conf.get('conf', '2fav')
        self.favcmd3 = self.conf.get('conf', '3fav')
        self.favcmd4 = self.conf.get('conf', '4fav')
        self.favcmd5 = self.conf.get('conf', '5fav')
        self.favcmd6 = self.conf.get('conf', '6fav')
        self.favcmd7 = self.conf.get('conf', '7fav')
        self.favcmd8 = self.conf.get('conf', '8fav')
        self.favcmd9 = self.conf.get('conf', '9fav')
        try:
            self.autostart = self.conf.get('conf', 'autostart')
        except ConfigParser.NoOptionError:
            self.autostart = None
        if self.autostart:
            self.autostart = self.autostart.split("    ")
        if not self.favcmd0 == "":
            self.fav0.set_visible(True)
            self.fav0.set_tooltip_text(self.favcmd0)
            self.fav0.connect("clicked", self.execute)
            self.favimage0.set_from_file(self.conf.get('conf', '0favicon'))
        else:
            self.fav0.set_visible(False)
        if not self.favcmd1 == "":
            self.fav1.set_visible(True)
            self.fav1.set_tooltip_text(self.favcmd1)
            self.fav1.connect("clicked", self.execute)
            self.favimage1.set_from_file(self.conf.get('conf', '1favicon'))
        else:
            self.fav1.set_visible(False)
            self.fav1.set_tooltip_text("")
        if not self.favcmd2 == "":
            self.fav2.set_visible(True)
            self.fav2.set_tooltip_text(self.favcmd2)
            self.fav2.connect("clicked", self.execute)
            self.favimage2.set_from_file(self.conf.get('conf', '2favicon'))
        else:
            self.fav2.set_visible(False)
            self.fav2.set_tooltip_text("")
        if not self.favcmd3 == "":
            self.fav3.set_visible(True)
            self.fav3.set_tooltip_text(self.favcmd3)
            self.fav3.connect("clicked", self.execute)
            self.favimage3.set_from_file(self.conf.get('conf', '3favicon'))
        else:
            self.fav3.set_visible(False)
            self.fav3.set_tooltip_text("")
        if not self.favcmd4 == "":
            self.fav4.set_visible(True)
            self.fav4.set_tooltip_text(self.favcmd4)
            self.fav4.connect("clicked", self.execute)
            self.favimage4.set_from_file(self.conf.get('conf', '4favicon'))
        else:
            self.fav4.set_visible(False)
            self.fav4.set_tooltip_text("")
        if not self.favcmd5 == "":
            self.fav5.set_visible(True)
            self.fav5.set_tooltip_text(self.favcmd5)
            self.fav5.connect("clicked", self.execute)
            self.favimage5.set_from_file(self.conf.get('conf', '5favicon'))
        else:
            self.fav5.set_visible(False)
            self.fav5.set_tooltip_text("")
        if not self.favcmd6 == "":
            self.fav6.set_visible(True)
            self.fav6.set_tooltip_text(self.favcmd6)
            self.fav6.connect("clicked", self.execute)
            self.favimage6.set_from_file(self.conf.get('conf', '6favicon'))
        else:
            self.fav6.set_visible(False)
            self.fav6.set_tooltip_text("")
        if not self.favcmd7 == "":
            self.fav7.set_visible(True)
            self.fav7.set_tooltip_text(self.favcmd7)
            self.fav7.connect("clicked", self.execute)
            self.favimage7.set_from_file(self.conf.get('conf', '7favicon'))
        else:
            self.fav7.set_visible(False)
            self.fav7.set_tooltip_text("")
        if not self.favcmd8 == "":
            self.fav8.set_visible(True)
            self.fav8.set_tooltip_text(self.favcmd8)
            self.fav8.connect("clicked", self.execute)
            self.favimage8.set_from_file(self.conf.get('conf', '8favicon'))
        else:
            self.fav8.set_visible(False)
            self.fav8.set_tooltip_text("")
        if not self.favcmd9 == "":
            self.fav9.set_visible(True)
            self.fav9.set_tooltip_text(self.favcmd9)
            self.fav9.connect("clicked", self.execute)
            self.favimage9.set_from_file(self.conf.get('conf', '9favicon'))
        else:
            self.fav9.set_visible(False)
            self.fav9.set_tooltip_text("")
        self.activities.show()
        self.activities.grab_focus()
        self.window.hide()
        return

    def execute(self, actor):
        """ Execute commands in a subprocess """
        if actor == self.fav0:
            subprocess.Popen(self.favcmd0.split(' '))
            self.hide()
        elif actor == self.fav1:
            subprocess.Popen(self.favcmd1.split(' '))
            self.hide()
        elif actor == self.fav2:
            subprocess.Popen(self.favcmd2.split(' '))
            self.hide()
        elif actor == self.fav3:
            subprocess.Popen(self.favcmd3.split(' '))
            self.hide()
        elif actor == self.fav4:
            subprocess.Popen(self.favcmd4.split(' '))
            self.hide()
        elif actor == self.fav5:
            subprocess.Popen(self.favcmd5.split(' '))
            self.hide()
        elif actor == self.fav6:
            subprocess.Popen(self.favcmd6.split(' '))
            self.hide()
        elif actor == self.fav7:
            subprocess.Popen(self.favcmd7.split(' '))
            self.hide()
        elif actor == self.fav8:
            subprocess.Popen(self.favcmd8.split(' '))
            self.hide()
        elif actor == self.fav9:
            subprocess.Popen(self.favcmd9.split(' '))
            self.hide()
        elif actor == "enter" or actor == self.gobutton:
            subprocess.Popen(str.split(self.runentry.get_text()))
            self.runentry.set_text("")
        elif actor == "autostart":
            if self.autostart:
                for items in self.autostart:
                    subprocess.Popen(items.split(' '))
        elif actor == self.restartbutton:
            subprocess.Popen(['gksu', 'reboot'])
        elif actor == self.haltbutton:
            subprocess.Popen(['gksu', 'halt'])
        self.hide()

    def keycatch(self, actor, event):
        """ Capture keys for execute or minimise """
        test_mask = (event.state & Gdk.ModifierType.SUPER_MASK ==
                       Gdk.ModifierType.SUPER_MASK)
        if event.get_state() and test_mask:
            self.showorhide()
        elif event.get_keycode()[1] == 36:
            self.execute("enter")

    def button(self, actor, event):
        """ Catch mouse clicks """
        # NOT IMPLEMENTED YET test_mask = ...
        print event.state()
        print Gdk.ModifierType()
        #if event.get_state() and test_mask:
        #    self.showorhide()
        return

    def motion(self, actor, event):
        """ Hot Corner functionality """
        if self.activities.get_pointer()[0] == 0 and (
                self.activities.get_pointer()[1] == 0):
            self.showorhide()
        return

    def showorhide(self, *args):
        """ Show or hide the overlay depending on visibility """
        if self.window.get_visible():
            self.hide()
        elif not self.window.get_visible():
            self.show()
        time.sleep(1)

    def show(self, *args):
        """ show overlay window """
        self.updatedock()
        mytime = time.strftime('%H') + ':' + time.strftime('%M')
        self.timelabel.set_text(mytime)
        self.window.fullscreen()
        self.window.maximize()
        self.window.show()
        self.activities.set_keep_above(True)
        self.runentry.grab_focus()
        return

    def hide(self, *args):
        """ hide overlay window """
        self.timelabel.set_text("")
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

    def updatedock(self):
        """ Update the list of open windows on the overlay """
        self.screen = Wnck.Screen.get_default()
        self.screen.force_update()
        if self.windowlist == self.screen.get_windows():
            return
        self.windowlist = self.screen.get_windows()
        openwindows = []
        if not len(self.windowlist) == 0:
            count = 0
            for windows in self.windowlist:
                if not windows.get_name() in HIDELIST:
                    openwindows.append([windows.get_name(), windows.get_icon(),
                                           windows.is_minimized()])
            # blank before filling dock
            for items in self.dock:
                items[0].set_tooltip_text("")
                items[2].set_text("")
                items[0].set_visible(False)
                items[1].set_visible(False)
                items[2].set_visible(False)
            # fill dock with open windows
            for items in openwindows:
                if len(items[0]) > 13:
                    text = items[0][:9] + '...'
                else:
                    text = items[0]
                self.dock[count][0].set_from_pixbuf(items[1])
                self.dock[count][1].connect("clicked", self.changewindow)
                self.dock[count][1].set_tooltip_text(items[0])
                self.dock[count][2].set_line_wrap(True)
                self.dock[count][2].set_text(text)
                self.dock[count][0].set_visible(True)
                self.dock[count][1].set_visible(True)
                self.dock[count][2].set_visible(True)
                count = count + 1
            return

    def changewindow(self, actor):
        """ Activate windows that you select from the dock """
        self.screen.force_update()
        self.windowlist = self.screen.get_windows()
        for windows in self.windowlist:
            # activate window that has the same name
            if windows.get_name() == actor.get_tooltip_text():
                self.window.hide()
                windows.activate(0)
                return
        # couldn't open window
        return

    def checkconfig(self):
        """ create a default config if not available """
        if not os.path.isfile(CONFIG):
            conffile = open(CONFIG, "w")
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
                           "m\n9fav = \n9favicon =\n\n# autostart allows mu" +
                           "ltiple commands 4 space separated. ('    ')\nau" +
                           "tostart = gnome-settings-daemon\n")
            conffile.close()
        return

    def openconf(self, *args):
        """ Open config file in default text editor """
        self.checkconfig()
        subprocess.Popen(['/usr/bin/xdg-open', CONFIG])
        self.hide()

    def reloadme(self, event):
        """ Reload the main window so shortcuts can be updated """
        self.run()

if __name__ == "__main__":
    OHMSHELL()
