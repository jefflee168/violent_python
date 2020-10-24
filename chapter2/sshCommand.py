#!/usr/bin/python
# coding: utf8

import pexpect
from pexpect import expect, pxssh, spawn

PROMPT = ['# ', '>>> ', '> ', '\$ ']
def send_command(child, cmd):
    child = pexpect.spawn.sendline(cmd)
    #child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting?'
    connStr = 'ssh ' + user + '@' + host
    child = spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, \
                        '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, \
                             '[P|p]assword:'])
        if ret == 0:
            print('[-] Error Connecting')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host = '10.0.0.22'
    user = 'jeff'
    password = 'redhat'

    child = connect(user, host, password)
    send_command(child, 'grep jeff /etc/shadow')

if __name__ == '__main__':
    main()