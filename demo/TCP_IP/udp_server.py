#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''一个 Socket 依赖 4 项：服务器地址、服务器端口、客户端地址、
客户端端口来唯一确定一个 Socket'''


import socket, threading

print u'AF_INET 指定使用 IPv4 协议，如果要用更先进的 IPv6，就指定为 AF_INET6 。 SOCK_DGRAM 指定使用面向流的 UDP 协议'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

#print u'''调用 listen() 方法开始监听端口，传入的参数指定等待连接的最大数量5'''
#s.listen(5) #UDP不需要
print 'Bind UDP on 9999...'

while  True:
	data, addr = s.recvfrom(1024)
	print 'Received from %s:%s.' % addr
	s.sendto('Hello, %s!' % data, addr)


