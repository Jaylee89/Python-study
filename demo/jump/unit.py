# coding: utf-8
import os
import sys
import subprocess
import shutil
import time
import math
from PIL import Image, ImageDraw
import random
import json
import re
import datetime


def pull_screenshot():
    #process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
    #process = subprocess.Popen('adb shell screencap -p', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    #stderrinfo, stdoutinfo = process.communicate()
    #print('stderrinfo is -------> %s and stdoutinfo is -------> %s' % (stderrinfo, stdoutinfo))
    print('finish executing cmd....')
    command = 'adb shell screencap -p'
    out = timeout_command(command, 3)
    #return process.returncode

    print "out is (%s)" % out
    try:
        # screenshot = process.stdout.read()
        # screenshot = stdout.read()
        screenshot = out[0]
    except TypeError, msg:
        print 'TypeError is ', msg
        return None

    print 'screenshot is', screenshot
    if sys.platform == 'win32':
        screenshot = screenshot.replace(b'\r\n', b'\n')
    f = open('autojump.png', 'wb')
    f.write(screenshot)
    f.close()

def timeout_command(command, timeout):
    start = datetime.datetime.now()
    #process = subprocess.Popen(command, shell=True, bufsize=100000, stdout=subprocess.PIPE, stderr=subprocess.PIPE ) #close_fds=True, linux only
    process = subprocess.Popen(command, shell=True, bufsize=100000, stdout=subprocess.PIPE)  # close_fds=True, linux only
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            print 'xxxxxxxxxxxxxxx'
            try:
                process.terminate()
            except Exception, e:
                print 'process.poll() is None, error is ', e
                return None
            return None
    #out = process.communicate()[0]
    #out = process.stdout.read()
    out = process.communicate()
    if process.stdin:
        process.stdin.close()
    if process.stdout:
        process.stdout.close()
    if process.stderr:
        process.stderr.close()
    try:
        process.kill()
    except OSError:
        pass
    return out

def main():
    pull_screenshot()
    #code = pull_screenshot()
    #print 'code is ', code

if __name__ == '__main__':
    main()