# -*- coding: utf-8 -*-

#    This file is part of emesene.
#
#    emesene is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    emesene is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with emesene; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import gtk
import gobject

import e3
import gui
from gui.base import Plus
import glib
import extension
from gui.gtkui import utils

class MusicButton(gtk.ToggleButton):
    """Show a text notification when contact is typing, like old emesene 1.x."""
    NAME = 'Music Button'
    DESCRIPTION = 'Activates/Deactivate music plugin'
    AUTHOR = 'Jose Rostagno'
    WEBSITE = 'www.emesene.org'

    def __init__(self, userpanel, arg):
        """constructor"""
        gtk.ToggleButton.__init__(self)
        self.session = userpanel.session
        music_image = utils.gtk_ico_image_load(gui.theme.emote_theme.emote_to_path('(8)', True),
            gtk.ICON_SIZE_MENU)
        self.set_image(music_image)
        self.set_relief(gtk.RELIEF_NONE)
        self.connect('toggled', self._on_button_toggled)
        self.music = extension.get_instance('listening to')
        enabled = self.session.config.get_or_set('music_enabled', False)
        self.set_active(enabled)
        if hasattr(extension, "subscribe"):
            extension.subscribe(self._on_extension_changed, 'listening to')

    def _on_button_toggled(self, button):
        '''called when the search button is toggled'''
        if button.get_active():
            self.music.start()
            self.set_tooltip_text(_('Disable Music Plugin'))
        else:
            self.music.stop()
            self.set_tooltip_text(_('Enable Music Plugin'))

    def _on_extension_changed(self, new_extension):
        if type(self.music) != new_extension:
            self.music.stop()
            self.music = None
            if new_extension:
                self.music = new_extension(self.session)
                if self.get_active():
                    self.music.start()

    def __del__(self):
        if hasattr(extension, "unsubscribe"):
            extension.unsubscribe(self._on_extension_changed,'listening to')
        if self.music:
            self.music.stop()
