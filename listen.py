#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import socket
from contextlib import closing
import commands

__julius_bufsize = 4096
__julius_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def julius_begin():
    cmd = 'julius -C dictation-kit-v4.3.1-linux/main.jconf -C dictation-kit-v4.3.1-linux/am-gmm.jconf -demo -module'
    subprocess.call(cmd, shell=True)

def connect_to_julius():
    julius_host = 'localhost'
    julius_port = 10500
    __julius_socket.connect((julius_host, julius_port))
    
def listen_to_julius():
    word_counter = 0
    julius_result_connected = ""

    while True:
        result_recv = __julius_socket.recv(__julius_bufsize)
        # print (result_recv)
        if "WORD" in result_recv:
            word_counter += 1;
            if word_counter >= 2:
                julius_result_connected += result_recv[7:-1]
        if "</RECOGOUT>" in result_recv:
            return julius_result_connected

