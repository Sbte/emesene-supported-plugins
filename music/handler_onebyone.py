# -*- coding: utf-8 -*-

#   This file is part of emesene.
#
#    Emesene is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
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

import base_windows_handler

class OneByOneHandler( base_windows_handler.WindowsPlayerHandler ):
    NAME = 'OneByOne'
    DESCRIPTION = 'Handler for OneByOne music player'
    AUTHOR = 'Ariel Juodziukynas'
    WEBSITE = 'www.emesene.org'
    def __init__(self, session):
        base_windows_handler.WindowsPlayerHandler.__init__( self, session )
        self.windowClass = '1by1WndClass'
        self.isRunning()

    def splitStr(self, string):
        return string.split(' - ',1)[1].rsplit('.',1)[0]
        
    def isPlaying( self ):
        title = self.getWindowTitle()
        return title != '1by1 - The Directory Player' and title != ""
