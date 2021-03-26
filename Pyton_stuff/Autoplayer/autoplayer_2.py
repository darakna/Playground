import os
os.environ['PATH'] = os.environ['PATH'] + r";.\vlc"
import vlc
import time
from datetime import datetime
import sys
import threading

class Spinner:
    busy = False
    delay = 0.5

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False




def logtofile(text):
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
    fhandler = open(logfilename, "a+")
    fhandler.write("[" + dt_string + "] - " + text + "\n")
    print("[" + dt_string + "] - " + text + "\n")
    fhandler.close()

def init_player():
    # define VLC instance
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

    # Define VLC player
    player = instance.media_player_new()

    # Define VLC media
    media = instance.media_new(url)

    # Set player media
    player.set_media(media)
    player.audio_set_volume(95)

    # Play the media
    player.play()
    time.sleep(1)
    value = player.is_playing()
    logtofile("Started VLC audiostream: " + url)
    return player


def watch_play(player):
    autostarter = 0
    while(1):
        print("\b..", end="")
        sys.stdout.flush()
        time.sleep(60)
        value = player.is_playing()
        if value == 0:
            player.play()
            time.sleep(1)
            logtofile("Restarting VLC audiostream... ")
            value = player.is_playing()
            logtofile("Restarted VLC audiostream: " + str(value))
            if value == 0:
                autostarter += 1
            else:
                autostarter = 0
        if autostarter >= 3:
            logtofile("Autostarter failed " + str(autostarter) + " times: ")
            player.stop()
            player = init_player()
            autostarter = 0
            value = player.is_playing()
            logtofile("Connection reinitialised: " + str(value))



logfilename = "vlc_logfile.log"

logtofile("Started VLC app")
url = 'https://live.magicfm.ro:8443/magicfm.aacp'

player = init_player()

with Spinner():
    watch_play(player)
