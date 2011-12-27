import songretriever
import commands

class MocHandler(songretriever.MusicHandler):
    '''Handler moc (Music On Console) music player'''
    NAME = 'Music On Console'
    DESCRIPTION = 'Music handler for moc'
    AUTHOR = 'Adolfo Fitoria'
    WEBSITE = 'www.emesene.org'

    def __init__(self, session):
        songretriever.MusicHandler.__init__(self, session)

    def is_running(self):
        '''returns True if the player is running'''
        status = commands.getoutput('ps -e | grep mocp')
        return status != ''

    def is_playing(self):
        '''returns True if the player is playing a song'''
        command = "mocp -Q '%state' 2>/dev/null"
        if not self.is_running():
            return False

        status = commands.getoutput(command) 

        return status == 'PLAY' 

    def get_current_song(self):
        '''returns the current song or None if no song is playing'''
        command = "mocp -Q '%artist;%album;%song;%file' 2>/dev/null"
        output = commands.getoutput(command).split(';')
        if not self.is_running() or not self.is_playing():
            return None

        return songretriever.Song(output[0], output[1], 
                                  output[2], output[3])
