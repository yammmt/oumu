#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import listen
import speak

print("Please talk to me!")

listen.julius_begin()
sleep(5) # waits for start-up of julius
speak.speak_with_jsay("おはようございます")
listen.connect_to_julius()

while(True):
    words_talked_to = listen.listen_to_julius()
    print(words_talked_to)
    speak.speak_with_jsay(words_talked_to)
    if "さよなら" in words_talked_to or "さようなら" in words_talked_to:
        exit()

