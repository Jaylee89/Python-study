#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import hashlib

class SHA():
    def __init__(self):
        self.__hash = hashlib.sha512()
    def getSha512(self, name):
        self.__hash.update(name.encode('utf-8'))
        return self.__hash.hexdigest()

if __name__ == "__main__":
    print(SHA().getSha512("您好"))