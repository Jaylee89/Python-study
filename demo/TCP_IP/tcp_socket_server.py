#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''一个 Socket 依赖 4 项：服务器地址、服务器端口、客户端地址、
客户端端口来唯一确定一个 Socket'''


import socket, threading

print u'AF_INET 指定使用 IPv4 协议，如果要用更先进的 IPv6，就指定为 AF_INET6 。 SOCK_STREAM 指定使用面向流的 TCP 协议'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 32568))

print u'''调用 listen() 方法开始监听端口，传入的参数指定等待连接的最大数量5'''
s.listen(5)
print 'Waiting for connection...'

while  True:
	# 接受一个新连接:
	sock, addr = s.accept()
	# 创建新线程来处理 TCP 连接:
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()

def  tcplink(sock, addr):
	print 'Accept new connection from %s:%s...' % addr
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit'  or  not data:
			break
		sock.send('Hello, %s!' % data)
	sock.close()
	print 'Connection from %s:%s closed.' % addr

