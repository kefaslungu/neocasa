# -*- coding: utf-8 -*-
import winsound
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the sound file name (assuming it’s a WAV file)
screenshots= "screenshots.wav"
wait = "wait.wav"

# Create the full path to the sound file
screenshot_path = os.path.join(current_directory, screenshots)
wait_path = os.path.join(current_directory, wait)
#sound_path = os.path.join(current_directory, sound_file)
#sound_path = os.path.join(current_directory, sound_file)

def screenshot():
    # Play the sound using the full path
    winsound.PlaySound(screenshot_path  , winsound.SND_FILENAME)

def waiting():
    winsound.PlaySound(wait_path, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

#waiting()
#screenshot()