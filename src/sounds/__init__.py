# -*- coding: utf-8 -*-
import winsound
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the sound file name
screenshots= "screenshots.wav"
wait = "wait.wav"
snap = "snap.wav"

# Create the full path to the sound file
screenshot_path = os.path.join(current_directory, screenshots)
wait_path = os.path.join(current_directory, wait)
snap_path = os.path.join(current_directory, snap)
#sound_path = os.path.join(current_directory, sound_file)

def snap():
    # Play the sound using the full path
    winsound.PlaySound(snap_path  , winsound.SND_FILENAME)

def screenshot():
    # Play the sound using the full path
    winsound.PlaySound(screenshot_path  , winsound.SND_FILENAME)

def waiting():
    winsound.PlaySound(wait_path, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
