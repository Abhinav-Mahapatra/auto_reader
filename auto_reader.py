# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 02:24:48 2020

@author: Abhinav Mahapatra
"""

import pythoncom, pyHook
import win32clipboard
from gtts import gTTS 
import os


def OnKeyboardEvent(event):
    if event.KeyID == 120:
        # keyID at F9, triggers the recoding at F9
        text = get_clipboard_info()
        # Converting the text into speech
        speech = gTTS(text = text, lang = 'en', slow = False)
        # Saving the speech in a mp3 file
        speech.save("text.mp3")
        # Running the speech in the default player 
        os.system("start text.mp3")
        
    elif event.KeyID == 121:
        # Removing the recoding file at F10
        print('Removing The recoding')
        os.remove("text.mp3")
        return 0

def get_clipboard_info():
    # get clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

try:
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.KeyDown = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()
except KeyboardInterrupt:
    pass