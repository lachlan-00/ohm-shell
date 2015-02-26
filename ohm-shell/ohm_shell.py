#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" OhM-shell
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
#import psutil

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

import checkconfig
import procman

from gi.repository import Gtk
from gi.repository import Gdk
#from gi.repository import GLib
from gi.repository import Wnck
from xdg.BaseDirectory import xdg_config_dirs

HOMEFOLDER = os.getenv('HOME')
CONFIG = xdg_config_dirs[0] + '/ohm-shell.conf'
HIDELIST = ['ohm_shell.py', 'ohm_shell.py', 'Desktop', 'ohm-shell: Activities',
            'ohm-shell: Overlay', 'xfce4-panel', 'xfce4-notifyd',
            'Top Expanded Edge Panel', 'plank']
THEMENAME = 'gnome'
MYTHEMEBASE = '/usr/share/icons/' + THEMENAME + '/'
MYTHEMEPATHS = checkconfig.checksetting(MYTHEMEBASE + '/index.theme',
                                        'Icon Theme', 'Directories')
ICONSEARCHPATHS = []
for path in MYTHEMEPATHS.split(','):
    if len(path) > 0:
        ICONSEARCHPATHS.append(MYTHEMEBASE + path)


class OHMSHELL(object):
    """ OHM-shell overlay """
    def __init__(self):
        """ Initialise the main window and start the program """
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/usr/share/ohm-shell/ohm-shell.ui")
        self.builder.connect_signals(self)
        self.conf = ConfigParser.RawConfigParser()
        # Load primary windows, labels and button objects
        self.mainwindow = self.builder.get_object("main_window")
        self.mainevent = self.builder.get_object("overlayactivityevent")
        self.maintimelabel = self.builder.get_object("overlaytimelabel")
        self.runentry = self.builder.get_object("runentry")
        self.appgrid = self.builder.get_object("app_grid")
        self.fileview = self.builder.get_object("fileview")
        self.contentlist = self.builder.get_object('filestore')
        self.contenttree = self.builder.get_object('fileview')
        self.gobutton = self.builder.get_object("gobutton")
        self.leftlabel = self.builder.get_object("leftlabel")
        self.rightlabel = self.builder.get_object("rightlabel")
        self.reloadbutton = self.builder.get_object("reloadbutton")
        self.optionbutton = self.builder.get_object("optionbutton")
        self.logoutbutton = self.builder.get_object("logoutbutton")
        self.restartbutton = self.builder.get_object("restartbutton")
        self.haltbutton = self.builder.get_object("haltbutton")
        self.closebutton = self.builder.get_object("closebutton")
        self.addfavbutton = self.builder.get_object("addfavbutton")
        self.delfavbutton = self.builder.get_object("delfavbutton")
        self.overflowlabel = self.builder.get_object("overflowlabel")
        # Load Overlay Dock Toolbar
        self.topdock = self.builder.get_object("main_dock")
        self.topdockevent = self.builder.get_object("maindockevent")
        self.toptimelabel = self.builder.get_object("overlaytimelabel")
        # Load Activities HotCorner
        self.hotwin = self.builder.get_object("hot_corner")
        self.hotevent = self.builder.get_object("hotevent")
        self.hotlabel = self.builder.get_object("hotlabel")
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
        self.window20 = self.builder.get_object("windowimage20")
        self.window21 = self.builder.get_object("windowimage21")
        self.window22 = self.builder.get_object("windowimage22")
        self.window23 = self.builder.get_object("windowimage23")
        self.window24 = self.builder.get_object("windowimage24")
        self.window25 = self.builder.get_object("windowimage25")
        self.window26 = self.builder.get_object("windowimage26")
        self.window27 = self.builder.get_object("windowimage27")
        self.winbutton0 = self.builder.get_object("winbutton0")
        self.winbutton1 = self.builder.get_object("winbutton1")
        self.winbutton2 = self.builder.get_object("winbutton2")
        self.winbutton3 = self.builder.get_object("winbutton3")
        self.winbutton4 = self.builder.get_object("winbutton4")
        self.winbutton5 = self.builder.get_object("winbutton5")
        self.winbutton6 = self.builder.get_object("winbutton6")
        self.winbutton7 = self.builder.get_object("winbutton7")
        self.winbutton8 = self.builder.get_object("winbutton8")
        self.winbutton9 = self.builder.get_object("winbutton9")
        self.winbutton10 = self.builder.get_object("winbutton10")
        self.winbutton11 = self.builder.get_object("winbutton11")
        self.winbutton12 = self.builder.get_object("winbutton12")
        self.winbutton13 = self.builder.get_object("winbutton13")
        self.winbutton14 = self.builder.get_object("winbutton14")
        self.winbutton15 = self.builder.get_object("winbutton15")
        self.winbutton16 = self.builder.get_object("winbutton16")
        self.winbutton17 = self.builder.get_object("winbutton17")
        self.winbutton18 = self.builder.get_object("winbutton18")
        self.winbutton19 = self.builder.get_object("winbutton19")
        self.winbutton20 = self.builder.get_object("winbutton20")
        self.winbutton21 = self.builder.get_object("winbutton21")
        self.winbutton22 = self.builder.get_object("winbutton22")
        self.winbutton23 = self.builder.get_object("winbutton23")
        self.winbutton24 = self.builder.get_object("winbutton24")
        self.winbutton25 = self.builder.get_object("winbutton25")
        self.winbutton26 = self.builder.get_object("winbutton26")
        self.winbutton27 = self.builder.get_object("winbutton27")
        self.winlabel0 = self.builder.get_object("winlabel0")
        self.winlabel1 = self.builder.get_object("winlabel1")
        self.winlabel2 = self.builder.get_object("winlabel2")
        self.winlabel3 = self.builder.get_object("winlabel3")
        self.winlabel4 = self.builder.get_object("winlabel4")
        self.winlabel5 = self.builder.get_object("winlabel5")
        self.winlabel6 = self.builder.get_object("winlabel6")
        self.winlabel7 = self.builder.get_object("winlabel7")
        self.winlabel8 = self.builder.get_object("winlabel8")
        self.winlabel9 = self.builder.get_object("winlabel9")
        self.winlabel10 = self.builder.get_object("winlabel10")
        self.winlabel11 = self.builder.get_object("winlabel11")
        self.winlabel12 = self.builder.get_object("winlabel12")
        self.winlabel13 = self.builder.get_object("winlabel13")
        self.winlabel14 = self.builder.get_object("winlabel14")
        self.winlabel15 = self.builder.get_object("winlabel15")
        self.winlabel16 = self.builder.get_object("winlabel16")
        self.winlabel17 = self.builder.get_object("winlabel17")
        self.winlabel18 = self.builder.get_object("winlabel18")
        self.winlabel19 = self.builder.get_object("winlabel19")
        self.winlabel20 = self.builder.get_object("winlabel20")
        self.winlabel21 = self.builder.get_object("winlabel21")
        self.winlabel22 = self.builder.get_object("winlabel22")
        self.winlabel23 = self.builder.get_object("winlabel23")
        self.winlabel24 = self.builder.get_object("winlabel24")
        self.winlabel25 = self.builder.get_object("winlabel25")
        self.winlabel26 = self.builder.get_object("winlabel26")
        self.winlabel27 = self.builder.get_object("winlabel27")
        # Load file chooser to add to dock
        self.addfavs = self.builder.get_object('addfavs')
        self.addfavok = self.builder.get_object('addfavok')
        self.addfavcancel = self.builder.get_object('addfavcancel')
        # Dock lists to update buttons and images together
        self.screen = None
        self.toolbarheight = None
        self.windowlist = None
        self.openwindows = None
        self.getwindowlist()
        ## get toolbar height for gnome-classic
        for windows in self.windowlist:
            if windows.get_name() == 'Top Expanded Edge Panel':
                self.toolbarheight = windows.get_geometry()[3]
        # Set up Open Windows overlay
        self.open = [[self.window0, self.winbutton0, self.winlabel0],
                     [self.window1, self.winbutton1, self.winlabel1],
                     [self.window2, self.winbutton2, self.winlabel2],
                     [self.window3, self.winbutton3, self.winlabel3],
                     [self.window4, self.winbutton4, self.winlabel4],
                     [self.window5, self.winbutton5, self.winlabel5],
                     [self.window6, self.winbutton6, self.winlabel6],
                     [self.window7, self.winbutton7, self.winlabel7],
                     [self.window8, self.winbutton8, self.winlabel8],
                     [self.window9, self.winbutton9, self.winlabel9],
                     [self.window10, self.winbutton10, self.winlabel10],
                     [self.window11, self.winbutton11, self.winlabel11],
                     [self.window12, self.winbutton12, self.winlabel12],
                     [self.window13, self.winbutton13, self.winlabel13],
                     [self.window14, self.winbutton14, self.winlabel14],
                     [self.window15, self.winbutton15, self.winlabel15],
                     [self.window16, self.winbutton16, self.winlabel16],
                     [self.window17, self.winbutton17, self.winlabel17],
                     [self.window18, self.winbutton18, self.winlabel18],
                     [self.window19, self.winbutton19, self.winlabel19],
                     [self.window20, self.winbutton20, self.winlabel20],
                     [self.window21, self.winbutton21, self.winlabel21],
                     [self.window22, self.winbutton22, self.winlabel22],
                     [self.window23, self.winbutton23, self.winlabel23],
                     [self.window24, self.winbutton24, self.winlabel24],
                     [self.window25, self.winbutton25, self.winlabel25],
                     [self.window26, self.winbutton26, self.winlabel26],
                     [self.window27, self.winbutton27, self.winlabel27]]
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
        self.fav10 = self.builder.get_object("favbutton10")
        self.fav11 = self.builder.get_object("favbutton11")
        self.fav12 = self.builder.get_object("favbutton12")
        self.fav13 = self.builder.get_object("favbutton13")
        self.fav14 = self.builder.get_object("favbutton14")
        self.fav15 = self.builder.get_object("favbutton15")
        self.fav16 = self.builder.get_object("favbutton16")
        self.fav17 = self.builder.get_object("favbutton17")
        self.fav18 = self.builder.get_object("favbutton18")
        self.fav19 = self.builder.get_object("favbutton19")
        self.fav20 = self.builder.get_object("favbutton20")
        self.image0 = self.builder.get_object("image0")
        self.image1 = self.builder.get_object("image1")
        self.image2 = self.builder.get_object("image2")
        self.image3 = self.builder.get_object("image3")
        self.image4 = self.builder.get_object("image4")
        self.image5 = self.builder.get_object("image5")
        self.image6 = self.builder.get_object("image6")
        self.image7 = self.builder.get_object("image7")
        self.image8 = self.builder.get_object("image8")
        self.image9 = self.builder.get_object("image9")
        self.image10 = self.builder.get_object("image10")
        self.image11 = self.builder.get_object("image11")
        self.image12 = self.builder.get_object("image12")
        self.image13 = self.builder.get_object("image13")
        self.image14 = self.builder.get_object("image14")
        self.image15 = self.builder.get_object("image15")
        self.image16 = self.builder.get_object("image16")
        self.image17 = self.builder.get_object("image17")
        self.image18 = self.builder.get_object("image18")
        self.image19 = self.builder.get_object("image19")
        self.image20 = self.builder.get_object("image20")
        self.cmd0 = None
        self.cmd1 = None
        self.cmd2 = None
        self.cmd3 = None
        self.cmd4 = None
        self.cmd5 = None
        self.cmd6 = None
        self.cmd7 = None
        self.cmd8 = None
        self.cmd9 = None
        self.cmd10 = None
        self.cmd11 = None
        self.cmd12 = None
        self.cmd13 = None
        self.cmd14 = None
        self.cmd15 = None
        self.cmd16 = None
        self.cmd17 = None
        self.cmd18 = None
        self.cmd19 = None
        self.name0 = None
        self.name1 = None
        self.name2 = None
        self.name3 = None
        self.name4 = None
        self.name5 = None
        self.name6 = None
        self.name7 = None
        self.name8 = None
        self.name9 = None
        self.name10 = None
        self.name11 = None
        self.name12 = None
        self.name13 = None
        self.name14 = None
        self.name15 = None
        self.name16 = None
        self.name17 = None
        self.name18 = None
        self.name19 = None
        self.fileitem = None
        self.favlist = None
        self.autostart = None
        self.showhotlabel = None
        self.appposition = None
        # remember pointer so hot corner doesn't continually open/close
        self.mask = None
        self.maskold = None
        # Connect UI
        self.mainwindow.connect("destroy", self.quit)
        self.mainwindow.connect("key-release-event", self.keycatch)
        self.mainwindow.connect("motion-notify-event", self.motion)
        self.mainevent.connect("button-release-event", self.button)
        self.topdock.connect("destroy", self.quit)
        self.topdock.connect("key-release-event", self.keycatch)
        self.topdock.connect("motion-notify-event", self.motion)
        self.hotwin.connect("motion-notify-event", self.motion)
        self.hotwin.connect("key-release-event", self.keycatch)
        self.hotevent.connect("button-release-event", self.button)
        self.topdockevent.connect("button-release-event", self.button)
        self.gobutton.connect("clicked", self.execute)
        self.addfavbutton.connect("clicked", self.choosefavs)
        self.delfavbutton.connect("clicked", self.delmode)
        self.addfavok.connect("clicked", self.addfavtoconf)
        self.addfavcancel.connect("clicked", self.cancelchoose)
        self.reloadbutton.connect("clicked", self.run)
        self.optionbutton.connect("clicked", self.openconf)
        self.logoutbutton.connect("clicked", self.sessionman)
        self.restartbutton.connect("clicked", self.sessionman)
        self.haltbutton.connect("clicked", self.sessionman)
        self.closebutton.connect("clicked", self.quit)
        # start
        self.run()
        Gtk.main()

    def run(self, *args):
        """ configure and show the main window """
        #format windows
        windowlist = [self.mainwindow, self.topdock, self.hotwin]
        # make windows undecorated and set options
        for windows in windowlist:
            windows.set_decorated(False)
            windows.set_decorated(False)
            windows.set_skip_taskbar_hint(True)
            windows.set_skip_pager_hint(True)
            windows.set_keep_above(True)
        self.hotwin.move(0, 0)
        self.hotwin.set_position(Gtk.Align.START)
        self.updatefavdock()
        self.updateopenwindows()
        self.initialloading()
        self.hotwin.show()
        #self.hotwin.grab_focus()
        self.mainwindow.hide()
        self.topdock.hide()
        return

    def initialloading(self):
        """ set up appearance and run startup commands according to config """
        # Show or hide the hotcorner Activities label
        if self.showhotlabel.lower() == 'true':
            self.hotevent.get_child().set_text('Activities')
        elif self.showhotlabel.lower() == 'false':
            self.hotevent.get_child().set_text('<')
        # allow moving the list of open apps to better fit dual monitors
        if (self.appposition.lower() == 'centre' or
                self.appposition.lower() == 'center'):
            self.leftlabel.set_visible(True)
            self.leftlabel.realize()
            self.rightlabel.set_visible(True)
            self.rightlabel.realize()
        elif self.appposition.lower() == 'left':
            self.leftlabel.set_visible(False)
            self.leftlabel.unrealize()
            self.rightlabel.set_visible(True)
            self.rightlabel.realize()
        elif self.appposition.lower() == 'right':
            self.leftlabel.set_visible(True)
            self.leftlabel.realize()
            self.rightlabel.set_visible(False)
            self.rightlabel.unrealize()
        # run autostart commands
        if self.autostart:
            self.autostart = self.autostart.split("    ")
            self.execute("autostart", None)
        return

    def updatefavdock(self):
        """ Read config and fill favourites list """
        tmpcount = 0
        checkconfig.checkconfig(CONFIG)
        self.conf.read(CONFIG)
        try:
            self.autostart = self.conf.get('options', 'autostart')
        except ConfigParser.NoOptionError:
            self.autostart = None
        try:
            self.appposition = self.conf.get('options', 'appposition')
        except ConfigParser.NoOptionError:
            self.appposition = 'Centre'
        try:
            self.showhotlabel = self.conf.get('options', 'showhotlabel')
        except ConfigParser.NoOptionError:
            self.showhotlabel = 'False'
        self.cmd0 = self.conf.get('dock', '0fav')
        self.cmd1 = self.conf.get('dock', '1fav')
        self.cmd2 = self.conf.get('dock', '2fav')
        self.cmd3 = self.conf.get('dock', '3fav')
        self.cmd4 = self.conf.get('dock', '4fav')
        self.cmd5 = self.conf.get('dock', '5fav')
        self.cmd6 = self.conf.get('dock', '6fav')
        self.cmd7 = self.conf.get('dock', '7fav')
        self.cmd8 = self.conf.get('dock', '8fav')
        self.cmd9 = self.conf.get('dock', '9fav')
        self.cmd10 = self.conf.get('dock', '10fav')
        self.cmd11 = self.conf.get('dock', '11fav')
        self.cmd12 = self.conf.get('dock', '12fav')
        self.cmd13 = self.conf.get('dock', '13fav')
        self.cmd14 = self.conf.get('dock', '14fav')
        self.cmd15 = self.conf.get('dock', '15fav')
        self.cmd16 = self.conf.get('dock', '16fav')
        self.cmd17 = self.conf.get('dock', '17fav')
        self.cmd18 = self.conf.get('dock', '18fav')
        self.cmd19 = self.conf.get('dock', '19fav')
        self.favlist = [[self.fav0, self.cmd0, self.image0, self.name0],
                        [self.fav1, self.cmd1, self.image1, self.name1],
                        [self.fav2, self.cmd2, self.image2, self.name2],
                        [self.fav3, self.cmd3, self.image3, self.name3],
                        [self.fav4, self.cmd4, self.image4, self.name4],
                        [self.fav5, self.cmd5, self.image5, self.name5],
                        [self.fav6, self.cmd6, self.image6, self.name6],
                        [self.fav7, self.cmd7, self.image7, self.name7],
                        [self.fav8, self.cmd8, self.image8, self.name8],
                        [self.fav9, self.cmd9, self.image9, self.name9],
                        [self.fav10, self.cmd10, self.image10, self.name10],
                        [self.fav11, self.cmd11, self.image11, self.name11],
                        [self.fav12, self.cmd12, self.image12, self.name12],
                        [self.fav13, self.cmd13, self.image13, self.name13],
                        [self.fav14, self.cmd14, self.image14, self.name14],
                        [self.fav15, self.cmd15, self.image15, self.name15],
                        [self.fav16, self.cmd16, self.image16, self.name16],
                        [self.fav17, self.cmd17, self.image17, self.name17],
                        [self.fav18, self.cmd18, self.image18, self.name18],
                        [self.fav19, self.cmd19, self.image19, self.name19]]
        for items in self.favlist:
            if not items[1] == "":
                tmpimage = self.conf.get('dock', (str(tmpcount) + 'icon'))
                items[0].set_visible(True)
                items[0].set_tooltip_text(items[1])
                items[0].connect("button-release-event", self.execute)
                items[2].set_from_file(tmpimage)
            else:
                items[0].set_visible(False)
                items[0].set_tooltip_text("")
            tmpcount = tmpcount + 1
        return

    def execute(self, actor, event):
        """ Execute commands in a subprocess """
        tmpcount = 0
        tmppid = None
        if event:
            if Gdk.ModifierType.BUTTON1_MASK == event.get_state():
                # show the overlay on left mouse clicks
                ###debug###print('execute: ' + time.asctime())
                for items in self.favlist:
                    if actor == items[0]:
                        print(items[0].get_tooltip_text())
                        # Switch to Active windows
                        if self.changewindow(items[0], event):
                            print('OHM: activating existing window ' +
                                  items[0].get_tooltip_text())
                            return True
                        tmpexec = (items[1]).split()
                        if not tmpexec:
                            tmpexec = [].append(items[1])
                        print('OHM: executing favourite')
                        tmppid = procman.startprocess(tmpexec)
                        if tmppid:
                            print(tmppid)
                            self.hide()
                            return True
                    tmpcount = tmpcount + 1
        if actor == "enter" or actor == self.gobutton:
            print('OHM: executing from runentry')
            runcmd = str.split(self.runentry.get_text())
            tmppid = procman.startprocess(runcmd)
            print(tmppid)
            self.runentry.set_text("")
        elif actor == "autostart":
            if self.autostart:
                for items in self.autostart:
                    # execute autorun programs as hidden shell commands
                    tmpexec = items.split()
                    if tmpexec:
                        print('OHM: executing autostart')
                        tmppid = procman.startprocess(tmpexec)
                        print(tmppid)
        elif actor == "kill":
            for items in self.autostart:
                temp = "/usr/bin/killall " + items.split()[0]
                os.system(temp)
        ###debug###print(tmppid)
        if tmppid:
            self.hide()
        return

    def sessionman(self, actor):
        """ session management processes """
        if actor == self.logoutbutton:
            tmppid = procman.startprocess(['gnome-session-quit',
                                           '--logout', '--force'])
        elif actor == self.restartbutton:
            tmppid = procman.startprocess(['gnome-session-quit',
                                           '--reboot'])
        elif actor == self.haltbutton:
            tmppid = procman.startprocess(['gnome-session-quit',
                                           '--power-off'])
        if tmppid:
            self.hide()
        return

    def keycatch(self, actor, event):
        """ Capture keys for execute or minimise """
        test_mask = (event.state & Gdk.ModifierType.SUPER_MASK ==
                     Gdk.ModifierType.SUPER_MASK)
        if event.get_state() and test_mask:
            if self.mainwindow.get_visible():
                ###debug###print('SUPER: hide overlay ' + time.asctime())
                self.hide()
                return
            elif not self.mainwindow.get_visible():
                ###debug###print('SUPER: show overlay ' + time.asctime())
                self.show()
                return
        elif event.get_keycode()[1] == 36:
            self.execute("enter", None)

    def button(self, actor, event):
        """ Catch mouse clicks"""
        if Gdk.ModifierType.BUTTON1_MASK == event.get_state():
            # show the overlay on left mouse clicks
            identity = actor.get_child().get_name()
            if identity == 'overlaylabel':
                ###debug###print('BUTTON: hide overlay ' + time.asctime())
                self.hide()
                return
            elif identity == 'hotlabel':
                ###debug###print('BUTTON: show overlay ' + time.asctime())
                self.show()
                return
        return

    def motion(self, actor, event):
        """ Hot Corner functionality """
        winname = actor.get_title()
        self.maskold = self.mask
        #self.mask = (self.hotwin.get_pointer())
        self.mask = (event.get_coords())
        # avoid repeatedly opening/closing activities
        if self.mask == (0.0, 0.0) and not self.maskold == (0.0, 0.0):
            ###debug###print('MOTION ' + time.asctime())
            if winname == 'ohm-shell: Overlay' or winname == ('ohm-shell:' +
                                                              ' Top Bar'):
                self.hide()
            if winname == 'ohm-shell: Activities':
                self.show()
        return

    def show(self, *args):
        """ show overlay window """
        ###debug###print('show: ' + time.asctime())
        self.updateopenwindows()
        self.updatefavdock()
        #mytime = time.strftime('%H') + ':' + time.strftime('%M')
        self.maintimelabel.set_text(time.asctime())
        self.toptimelabel.set_text(time.asctime())
        self.hotwin.set_keep_above(False)
        self.mainwindow.set_keep_above(True)
        self.topdock.set_keep_above(True)
        self.runentry.grab_focus()
        #resize for trenta/gnome-classic/compiz
        if self.toolbarheight:
            screenwidth = Wnck.Screen.get_width(Wnck.Screen.get_default())
            screenheight = Wnck.Screen.get_height(Wnck.Screen.get_default())
            self.mainwindow.set_size_request(screenwidth, (screenheight -
                                                       self.toolbarheight))
            self.topdock.set_size_request(screenwidth, self.toolbarheight)
            self.topdock.present()
            self.topdock.realize()
        self.mainwindow.maximize()
        self.mainwindow.fullscreen()
        self.mainwindow.present()
        self.mainwindow.realize()
        self.runentry.grab_focus()
        while Gtk.events_pending():
            Gtk.main_iteration()
        return

    def hide(self, *args):
        """ hide overlay window """
        ###debug###print('hide: ' + time.asctime())
        self.maintimelabel.set_text("")
        self.toptimelabel.set_text("")
        self.mainwindow.set_keep_above(False)
        self.mainwindow.hide()
        if self.toolbarheight:
            self.topdock.set_keep_above(False)
            self.topdock.hide()
        self.hotwin.present()
        self.hotwin.set_keep_above(True)
        while Gtk.events_pending():
            Gtk.main_iteration()
        return

    def quit(self, event):
        """ stop the process thread and close the program"""
        self.hotwin.destroy()
        self.mainwindow.destroy()
        self.execute("kill", None)
        Gtk.main_quit(event)
        return False

    def getwindowlist(self):
        """ get running windows and return true if the list has changed"""
        ###debug###print('UPDATE: running apps ' + time.asctime())
        firstrun = False
        oldwindows = None
        self.screen = Wnck.Screen.get_default()
        self.screen.force_update()
        #windowlist is the complete list of open windows
        self.windowlist = self.screen.get_windows()
        #openwindows is used to hide desktop windows like toolbars
        if not self.openwindows:
            print('FIRST')
            firstrun = True
            oldwindows = self.openwindows
        self.openwindows = []
        if not len(self.windowlist) == 0:
            for windows in self.windowlist:
                if not windows.get_name() in HIDELIST:
                    self.openwindows.append(windows)
        if oldwindows == self.openwindows and not firstrun:
            return False
        return True

    def updateopenwindows(self):
        """ Update the list of open windows on the overlay """
        winlist = self.getwindowlist()
        if not winlist:
            print('OHM: no change')
            return False
        count = 0
        # blank before filling dock
        for items in self.open:
            items[0].set_tooltip_text("")
            items[2].set_text("")
            items[0].set_visible(False)
            items[1].set_visible(False)
            items[2].set_visible(False)
        # fill dock with open windows
        for windows in self.openwindows:
            if not count == 28:
                text = windows.get_name()
                self.open[count][0].set_from_pixbuf(windows.get_icon())
                self.open[count][1].connect("button-release-event",
                                            self.changewindow)
                self.open[count][1].set_tooltip_text(text)
                self.open[count][2].set_line_wrap(True)
                self.open[count][2].set_text(text)
                self.open[count][0].set_visible(True)
                self.open[count][1].set_visible(True)
                self.open[count][2].set_visible(True)
                self.overflowlabel.set_text('')
                count = count + 1
            if count == 28:
                self.overflowlabel.set_text('WARNING: Out of room to display' +
                                            ' open windows')
        return True

    def activewindows(self, search):
        """ sort through open windows to activate """
        found = False
        foundwin = []
        # identify windows by title
        self.getwindowlist()
        for windows in self.windowlist:
            ###debug###print(dir(windows))
            tmpxid = windows.get_xid()
            tmppid = windows.get_pid()
            currentwindow = Wnck.Window.get(tmpxid)
            name = currentwindow.get_name().lower()
            pid = currentwindow.get_pid()
            # Activate windows with the same name from the overlay
            if search == name and tmppid == pid:
                foundwin.append(currentwindow)
                while Gtk.events_pending():
                    Gtk.main_iteration()
                #windows.activate(int(time.time()))
                found = True
        # search for split text in windows
        if not found:
            # if you can't find the exact window activate all matches
            print('OHM: looking for substrings')
            for windows in self.windowlist:
                ###debug###print(dir(windows))
                tmpxid = windows.get_xid()
                tmppid = windows.get_pid()
                currentwindow = Wnck.Window.get(tmpxid)
                name = currentwindow.get_name().lower()
                pid = currentwindow.get_pid()
                # Activate windows with the same name from the overlay
                if search == name.split()[0]:
                    foundwin.append(currentwindow)
                    while Gtk.events_pending():
                        Gtk.main_iteration()
                    #windows.activate(int(time.time()))
                    found = True
        if foundwin:
            for windows in foundwin:
                print('ACTIVATING: ' + windows.get_name())
                windows.activate(int(time.time()))
            return True
        # Error, Window not activated.
        return False

    def changewindow(self, actor, event):
        """ Activate windows that you select from the dock """
        tooltip = None
        if Gdk.ModifierType.BUTTON1_MASK == event.get_state():
            # show the overlay on left mouse clicks
                tooltip = actor.get_tooltip_text().lower()
        #found = False
        # identify open applications from clicked buttons
        if tooltip:
            #proclist = procman.getprocesses()
            print('LOOKING FOR: ' + tooltip)
            if self.activewindows(tooltip):
                self.mainwindow.hide()
                return True
            #procfound = False
            #procname = None
            #proccmd = None
            #self.getwindowlist()
            ##identify process by the tooltip
            #for proc in proclist:
            #    if not procfound:
            #        name = proc[1]
            #        cmd = proc[2]
            #        if cmd == []:
            #            cmd = name
            #        if tooltip in name or name.split()[0] in tooltip:
            #            procname = name.lower()
            #            procfound = True
            #        if tooltip in cmd or tooltip.split()[0] in cmd:
            #            proccmd = cmd
            #if procname or proccmd:
            #    print(procname)
            #    print(proccmd)
            #    for windows in self.windowlist:
            #        if not found:
            #            winname = windows.get_name().lower()
            #            # Activate open windows that match the shortcut.
            #            for items in self.favlist:
            #                if actor == items[0] and not found:
            #                    if procname in winname or winname in proccmd:
            #                        found = True
            #                    elif procname in items[1] or items[1] in
            #proccmd:
            #                        found = True
            #                    if found:
            #                        print("FOUNDPROCESS: " + winname)
            #                        print(procname)
            #                        print(proccmd)
            #                        print(tooltip)
            #                        windows.activate(int(time.time()))
            #if found:
            #    print('ERROR: ' + tooltip + ' missing')
            #    return False
        time.sleep(0.2)
        return False

    def openconf(self, *args):
        """ Open config file in default text editor """
        checkconfig.checkconfig(CONFIG)
        tmppid = procman.startprocess(['/usr/bin/xdg-open', CONFIG])
        if tmppid:
            self.hide()

    def addfavtoconf(self, actor):
        """ get desktop entry info """
        entry = 'Desktop Entry'
        filelist = []
        self.fileitem = self.addfavs.get_filename()
        filelist.append(checkconfig.checksetting(self.fileitem, entry, 'Name'))
        filelist.append(checkconfig.checksetting(self.fileitem, entry, 'Exec'))
        filelist.append(checkconfig.checksetting(self.fileitem, entry, 'Icon'))
        filelist.append(checkconfig.checksetting(self.fileitem, entry,
                                                 'Comment'))
        self.openconf()
        self.addfavs.hide()
        return

    def delmode(self, actor):
        """ allow live deleting of favourites """
        print(actor)
        return

    def choosefavs(self, actor):
        """ file chooser to pick favourites by *.desktop file """
        if actor == self.addfavbutton:
            self.addfavs.present()
        return

    def cancelchoose(self, actor):
        """ close the filechooser """
        if actor == self.addfavcancel:
            self.addfavs.hide()
if __name__ == "__main__":
    OHMSHELL()
