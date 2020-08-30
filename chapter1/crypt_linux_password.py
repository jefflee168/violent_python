#!/usr/bin/python

import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]

# 读取密码字典文件 dictionary.txt
dicFile = open('dictionary.txt', 'r')

for word in dicFile.readlines():
    word = word.strip('\n')
    cryptWord = crypt.crypt(word, salt)
    if (cryptWord == cry)
