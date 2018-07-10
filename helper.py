#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a helper module '

__author__ = 'Lu Jian'

import hashlib


def generateUserAccount():
    return "newName"


'''
type: 
    0 - numeric
    1 - alpha
    2 - 1 && 2
'''


def generatePassword(len, type=0):
    return (x for x in range(0,99999999))


def md5Encode(password):
    if isinstance(password,int):
        password=str(password)
    m = hashlib.md5()
    m.update(password)

    return m.hexdigest()
