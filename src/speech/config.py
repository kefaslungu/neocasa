import configparser
import os

config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config = configparser.RawConfigParser()
config.read(config_path)

#volume = config["DEFAULT"]["volume"]
#pitch = config["DEFAULT"]["pitch"]
#rate = config["DEFAULT"]["rate"]
voice = config["DEFAULT"]["voice"]
bitrate= config["DEFAULT"]["bitrate"]
