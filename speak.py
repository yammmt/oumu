#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
            
def speak_with_jsay(sentence):
    cmd = './jsay' + ' ' + sentence
    subprocess.Popen(cmd, shell=True)

