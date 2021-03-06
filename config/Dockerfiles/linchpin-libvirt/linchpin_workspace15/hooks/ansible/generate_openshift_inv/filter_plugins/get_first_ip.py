#!/usr/bin/env python
import os
import sys

def get_first_ip(text):
    # "mac address='52:54:00:cb:8a:d7'/>"
    text = text.split("\n")
    text = text[1]
    text = text.split(" ")[0]
    return text

class FilterModule(object):
    ''' A filter to fix interface's name format '''
    def filters(self):
        return {
            'get_first_ip': get_first_ip
        }
