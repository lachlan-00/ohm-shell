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
import ConfigParser
import subprocess

import checkconfig

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib
from gi.repository import Wnck
from xdg.BaseDirectory import xdg_config_dirs

HOMEFOLDER = os.getenv('HOME')
CONFIG = xdg_config_dirs[0] + '/ohm-shell.conf'
HIDELIST = ['ohm-shell.py', 'Desktop', 'xfce4-panel', 'xfce4-notifyd',
            'Top Expanded Edge Panel', 'plank']


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
        self.activitylabel = self.builder.get_object("mainevent")
        self.mainactivitylabel = self.builder.get_object("mainactivityevent")
        self.runentry = self.builder.get_object("runentry")
        self.appgrid = self.builder.get_object("app_grid")
        self.fileview = self.builder.get_object("fileview")
        self.contentlist = self.builder.get_object('filestore')
        self.contenttree = self.builder.get_object('fileview')
        self.gobutton = self.builder.get_object("gobutton")
        self.timelabel = self.builder.get_object("timelabel")
        self.leftlabel = self.builder.get_object("leftlabel")
        self.rightlabel = self.builder.get_object("rightlabel")
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
        self.toolbarheight = None
        for windows in self.windowlist:
            # activate window that has the same name
            if windows.get_name() == 'Top Expanded Edge Panel':
                self.toolbarheight = windows.get_geometry()[3]
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
        self.favimage10 = self.builder.get_object("image10")
        self.favimage11 = self.builder.get_object("image11")
        self.favimage12 = self.builder.get_object("image12")
        self.favimage13 = self.builder.get_object("image13")
        self.favimage14 = self.builder.get_object("image14")
        self.favimage15 = self.builder.get_object("image15")
        self.favimage16 = self.builder.get_object("image16")
        self.favimage17 = self.builder.get_object("image17")
        self.favimage18 = self.builder.get_object("image18")
        self.favimage19 = self.builder.get_object("image19")
        self.favimage20 = self.builder.get_object("image20")
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
        self.favcmd10 = None
        self.favcmd11 = None
        self.favcmd12 = None
        self.favcmd13 = None
        self.favcmd14 = None
        self.favcmd15 = None
        self.favcmd16 = None
        self.favcmd17 = None
        self.favcmd18 = None
        self.favcmd19 = None
        self.addfavbutton = self.builder.get_object("addfavbutton")
        self.favlist = None
        self.autostart = None
        self.showhotlabel = None
        self.appposition = None
        # remember pointer so hot corner doesn't continually open/close
        self.pointermask = None
        self.pointermaskold = None
        # Connect UI
        self.window.connect("destroy", self.quit)
        self.window.connect("key-release-event", self.keycatch)
        self.window.connect("motion-notify-event", self.motion)
        self.activities.connect("motion-notify-event", self.motion)
        self.activities.connect("key-release-event", self.keycatch)
        self.activitylabel.connect("button-release-event", self.button)
        self.mainactivitylabel.connect("button-release-event", self.button)
        self.gobutton.connect("clicked", self.execute)
        self.addfavbutton.connect("clicked", self.openconf)
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
        Gtk.main()

    def run(self, *args):
        """ configure and show the main window """
        self.processfav()
        self.initialloading()
        self.activities.show()
        #self.activities.grab_focus()
        self.window.hide()
        return

    def initialloading(self):
        """ set up appearance and run startup commands according to config """
        # Show or hide the hotcorner Activities label
        if self.showhotlabel.lower() == 'true':
            self.activitylabel.set_visible(True)
        elif self.showhotlabel.lower() == 'false':
            self.activitylabel.set_visible(False)
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
            self.execute("autostart")
        return

    def processfav(self):
        """ Read config and fill favourites dock """
        tmpcount = 0
        checkconfig.checkconfig(CONFIG)
        self.conf.read(CONFIG)
        try:
            self.autostart = self.conf.get('conf', 'autostart')
        except ConfigParser.NoOptionError:
            self.autostart = None
        try:
            self.appposition = self.conf.get('conf', 'appposition')
        except ConfigParser.NoOptionError:
            self.appposition = 'Centre'
        try:
            self.showhotlabel = self.conf.get('conf', 'showhotlabel')
        except ConfigParser.NoOptionError:
            self.showhotlabel = 'False'
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
        self.favcmd10 = self.conf.get('conf', '10fav')
        self.favcmd11 = self.conf.get('conf', '11fav')
        self.favcmd12 = self.conf.get('conf', '12fav')
        self.favcmd13 = self.conf.get('conf', '13fav')
        self.favcmd14 = self.conf.get('conf', '14fav')
        self.favcmd15 = self.conf.get('conf', '15fav')
        self.favcmd16 = self.conf.get('conf', '16fav')
        self.favcmd17 = self.conf.get('conf', '17fav')
        self.favcmd18 = self.conf.get('conf', '18fav')
        self.favcmd19 = self.conf.get('conf', '19fav')
        self.favlist = [[self.fav0, self.favcmd0, self.favimage0],
                        [self.fav1, self.favcmd1, self.favimage1],
                        [self.fav2, self.favcmd2, self.favimage2],
                        [self.fav3, self.favcmd3, self.favimage3],
                        [self.fav4, self.favcmd4, self.favimage4],
                        [self.fav5, self.favcmd5, self.favimage5],
                        [self.fav6, self.favcmd6, self.favimage6],
                        [self.fav7, self.favcmd7, self.favimage7],
                        [self.fav8, self.favcmd8, self.favimage8],
                        [self.fav9, self.favcmd9, self.favimage9],
                        [self.fav10, self.favcmd10, self.favimage10],
                        [self.fav11, self.favcmd11, self.favimage11],
                        [self.fav12, self.favcmd12, self.favimage12],
                        [self.fav13, self.favcmd13, self.favimage13],
                        [self.fav14, self.favcmd14, self.favimage14],
                        [self.fav15, self.favcmd15, self.favimage15],
                        [self.fav16, self.favcmd16, self.favimage16],
                        [self.fav17, self.favcmd17, self.favimage17],
                        [self.fav18, self.favcmd18, self.favimage18],
                        [self.fav19, self.favcmd19, self.favimage19]]
        for items in self.favlist:
            if not items[1] == "":
                tmpimage = self.conf.get('conf', (str(tmpcount) + 'favicon'))
                items[0].set_visible(True)
                items[0].set_tooltip_text(items[1])
                items[0].connect("clicked", self.execute)
                items[2].set_from_file(tmpimage)
            else:
                items[0].set_visible(False)
                items[0].set_tooltip_text("")
            tmpcount = tmpcount + 1
        return

    def execute(self, actor):
        """ Execute commands in a subprocess """
        tmpcount = 0
        for items in self.favlist:
            if actor == items[0]:
                print(items[0].get_tooltip_text())
                if self.changewindow(items[0]):
                    # Switch to Active windows
                    self.hide()
                    return
                tmpexec = (items[1]).split()
                if not tmpexec:
                    tmpexec = [].append(items[1])
                print(tmpexec)
                try:
                    self.hide()
                    subprocess.Popen(tmpexec)
                    return
                except OSError:
                    #no file found
                    print('No File Found')
                    return False
                except TypeError:
                    #malformed entry
                    print('Bad file name')
                    return False
            tmpcount = tmpcount + 1
        if actor == "enter" or actor == self.gobutton:
            try:
                self.hide()
                subprocess.Popen(str.split(self.runentry.get_text()))
                self.runentry.set_text("")
            except OSError:
                #no file found
                print('No File Found')
                self.runentry.set_text("")
                return False
            except TypeError:
                #malformed entry
                print('Bad file name')
                self.runentry.set_text("")
                return False
        elif actor == "autostart":
            if self.autostart:
                for items in self.autostart:
                    try:
                        # execute autorun programs as hidden shell commands
                        tmpexec = items.split()
                        if tmpexec:
                            subprocess.Popen(tmpexec)
                    except OSError:
                        #couldn't find the file to execute
                        pass
                    except TypeError:
                        #malformed entry
                        pass
        elif actor == "kill":
            for items in self.autostart:
                temp = "/usr/bin/killall " + items.split()[0]
                os.system(temp)
        elif actor == self.restartbutton:
            subprocess.Popen(['gksu', 'reboot'])
        elif actor == self.haltbutton:
            subprocess.Popen(['gksu', 'halt'])
        self.hide()
        return

    def keycatch(self, actor, event):
        """ Capture keys for execute or minimise """
        test_mask = (event.state & Gdk.ModifierType.SUPER_MASK ==
                     Gdk.ModifierType.SUPER_MASK)
        if event.get_state() and test_mask:
            self.showorhide()
        elif event.get_keycode()[1] == 36:
            self.execute("enter")

    def button(self, actor, event):
        """ Catch mouse clicks"""
        if Gdk.ModifierType.BUTTON1_MASK == event.get_state():
            # show the overlay on left mouse clicks
            if actor.get_child().get_text() == "Activities":
                self.showorhide()
        return

    def motion(self, actor, event):
        """ Hot Corner functionality """
        self.pointermaskold = self.pointermask
        self.pointermask = (str(self.activities.get_pointer()[0]) +
                            str(self.activities.get_pointer()[1]))
        # avoid repeatedly opening/closing activities
        if self.pointermask == '00' and not self.pointermaskold == '00':
            self.showorhide()
        return

    def showorhide(self, *args):
        """ Show or hide the overlay depending on visibility """
        if self.window.get_visible():
            self.hide()
        elif not self.window.get_visible():
            self.show()
        time.sleep(0.5)

    def show(self, *args):
        """ show overlay window """
        self.updatedock()
        mytime = time.strftime('%H') + ':' + time.strftime('%M')
        self.timelabel.set_text(mytime)
        self.activities.set_keep_above(True)
        #self.window.grab_focus()
        #self.runentry.grab_focus()
        GLib.idle_add(self.bring_to_front)
        while Gtk.events_pending():
            Gtk.main_iteration()
        self.screen.force_update()
        self.windowlist = self.screen.get_windows()
        for windows in self.windowlist:
            # activate window that has the same name
            if windows.get_name() == 'ohm-shell: Activities':
                windows.activate(int(time.time()))
                #overlayxid = wins.get_xid()
        #overlayxid.activate(int(time.time()))
        return

    def bring_to_front(self):
        """ Present window using Glib.Idle_add """
        #resize for trenta/gnome-classic/compiz
        if self.toolbarheight:
            screenwidth = Wnck.Screen.get_width(Wnck.Screen.get_default())
            screenheight = Wnck.Screen.get_height(Wnck.Screen.get_default())
            self.window.set_size_request(screenwidth, (screenheight - self.toolbarheight))
            #self.window.resize(screenwidth, screenheight)
        self.window.maximize()
        self.window.fullscreen()
        self.window.present()
        self.window.realize()
        return

    def hide(self, *args):
        """ hide overlay window """
        self.timelabel.set_text("")
        self.window.set_keep_above(False)
        self.window.hide()
        self.window.unrealize()
        self.activities.set_keep_above(True)
        while Gtk.events_pending():
            Gtk.main_iteration()
        return

    def quit(self, *args):
        """ stop the process thread and close the program"""
        self.activities.destroy()
        self.window.destroy()
        self.execute("kill")
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
        tooltip = actor.get_tooltip_text()
        self.screen.force_update()
        self.windowlist = self.screen.get_windows()
        for windows in self.windowlist:
            # activate window that has the same name
            if windows.get_name() == tooltip:
                self.window.hide()
                windows.activate(int(time.time()))
                return True
            else:
                # Activate open windows that match the shortcut.
                for items in self.favlist:
                    if (actor == items[0] and tooltip in windows.get_name()):
                        self.window.hide()
                        windows.activate(int(time.time()))
                        return True
        # couldn't open window
        return False

    def openconf(self, *args):
        """ Open config file in default text editor """
        checkconfig.checkconfig(CONFIG)
        subprocess.Popen(['/usr/bin/xdg-open', CONFIG])
        self.hide()

    def reloadme(self, event):
        """ Reload the main window so shortcuts can be updated """
        self.run()

if __name__ == "__main__":
    OHMSHELL()
