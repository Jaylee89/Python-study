#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket

print u'AF_INET 指定使用 IPv4 协议，如果要用更先进的 IPv6，就指定为 AF_INET6 。 SOCK_STREAM 指定使用面向流的 TCP 协议'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print u'''SMTP 服务是 25 端口，FTP 服务是 21端口，等等。端口号小于 1024 的是 Internet 标准服务的端口'''
s.connect(('www.sina.com.cn', 80))

s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while  True:
    # 每次最多接收 1k 字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

s.close()

header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb')  as f:
    f.write(html)