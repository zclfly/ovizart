#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import hashlib

class Handler:
    def __init__(self):
        self._file_name = None

    def set_file(self, file_name):
        self._file_name = file_name

    def get_hash(self):
        md5 = hashlib.md5(self._file_name)
        return md5.hexdigest()