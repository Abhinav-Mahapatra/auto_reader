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
        text = get_clipboard_info()      
        speech = gTTS(text = text, lang = 'en', slow = False)
        speech.save("text.mp3")
        os.system("start text.mp3")    

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