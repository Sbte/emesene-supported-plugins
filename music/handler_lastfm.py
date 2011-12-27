import songretriever

import socket
import xml.dom.minidom
import urllib

class LastfmHandler(songretriever.MusicHandler):
    '''a simple handler for lastfm web service'''
    NAME = 'LastFM'
    DESCRIPTION = 'Handler for lastfm music player'
    AUTHOR = 'Mariano Guerra'
    WEBSITE = 'www.emesene.org'

    def __init__(self, session):
        songretriever.MusicHandler.__init__(self, session)

        self.login = "Diftool80"
        self.update_interval = 60
        self.url = "http://ws.audioscrobbler.com/2.0/?method=\
                    user.getrecenttracks&api_key=fbb6f8beb8be\
                    b065baf549d57c73ac66&user=" + self.login + "&limit=1"
        self.track = None

        self.reconnect()

    def reconnect(self):
        '''reconnect, return True if connected'''
        # Discard previous track info
        self.track = None
        try:
            page = urllib.urlopen(self.url)
            doc = xml.dom.minidom.parse(page)
            self.track = doc.getElementsByTagName('track')[0]
        except IndexError:
            return False
        except IOError:
            return False
        except socket.error:
            return False

        return True

    def is_running(self):
        '''returns True if the player is running'''
        return self.reconnect()

    def is_playing(self):
        '''returns True if the player is playing a song'''
        if not self.is_running():
            return False

        return self.track.getAttribute('nowplaying') == "true"

    def get_current_song(self):
        '''returns the current song or None if no song is playing'''
        if not self.is_running() or not self.is_playing():
            return None

        element = self.track.getElementsByTagName('artist')
        artist = element[0].childNodes[0].nodeValue
        element = self.track.getElementsByTagName('album')
        album = element[0].childNodes[0].nodeValue
        element = self.track.getElementsByTagName('name')
        title = element[0].childNodes[0].nodeValue

        return songretriever.Song(artist, album, title)
