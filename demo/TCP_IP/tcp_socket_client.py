#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket

print u'AF_INET 指定使用 IPv4 协议，如果要用更先进的 IPv6，就指定为 AF_INET6 。 SOCK_STREAM 指定使用面向流的 TCP 协议'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print s.recv(1024)
for data  in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
