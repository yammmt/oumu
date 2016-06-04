#!/usr/bin/python
# -*- coding: utf-8 -*-

import listen
import speak

print("Please talk to me!")

#listen.julius_begin()
words_talked_to = listen.listen_to_julius()
print(words_talked_to)

speak.speak_with_jsay(words_talked_to)
