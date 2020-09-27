#!/usr/bin/python
# coding: utf8

from socket import *
import optparse
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((tgtHost, tgtPort))
        conn.send('ViolentPython\r\n')
        results = conn.recv(100)
        screenLock.acquire()
        print('[+] %d/tcp open.' % tgtPort)
        print('[+] ' + str(results))
    except:
        screenLock.acquire()
        print('[-] %d/tcp closed.' % tgtPort)
    finally:
        screenLock.release()
        conn.close()

def portSCan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s' Unknown host" % tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n Scan results for: ' + tgtName[0])
    except:
        print('\n Scan results for: ' + tgtIP)

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parse = optparse.OptionParser('usage %prog ' +                                  '-H <target host> -p <target port>')
    parse.add_option('-H', dest='tgtHost', type='string',                      help='specify target host')
    parse.add_option('-p', dest='tgtPort', type='string',                     help='specify target port[s] seperated by comma')

    (options, args) = parse.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parse.usage)
        exit(0)

    portSCan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
