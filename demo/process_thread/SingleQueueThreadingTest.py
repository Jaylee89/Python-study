#!/usr/bin/env python
# -*- coding: utf8 -*-

#参考这个文件
#https://www.ibm.com/developerworks/cn/aix/library/au-threadingpython/

import Queue 
import threading 
import urllib2 
import time 
from BeautifulSoup import BeautifulSoup 

hosts = ["http://192.168.29.100:8887/authentication/logon/logon.html", 
		"http://192.168.29.100:8887/authentication/logoff/logoff.html", 
		"http://192.168.29.100:8887/banking/balance/balance.html", 
		"http://192.168.29.100:8887/banking/billPayment/billPay.html", 
		"http://192.168.29.100:8887/banking/transfer/transfer.html",
		"http://192.168.29.100:8887/banking/rates/rates.html",
		"http://192.168.29.100:8887/banking/securitymessage/securityMessage.html",
		"http://192.168.29.100:8887/banking/transfer/transfer.html",
		] 

start=time.time()
queue = Queue.Queue() 

class ThreadUrl(threading.Thread): 
	"""Threaded Url Grab""" 
	def __init__(self, queue): 
		threading.Thread.__init__(self) 
		self.queue = queue

	def run(self): 
		while True: 
			#grabs host from queue 
			host = self.queue.get() 

			print 'host-->', host
			#grabs urls of hosts and then grabs chunk of webpage 
			url = urllib2.urlopen(host) 
			chunk = url.read()

			soup = BeautifulSoup(chunk) 
			print soup.findAll(['title']) , '\n'
			#signals to queue job is done 
			self.queue.task_done() 

def main(): 
	#spawn a pool of threads, and pass them queue instance 
	for i in range(5): 
		t = ThreadUrl(queue) 
		t.setDaemon(True) 
		t.start() 

	#populate queue with data 
	for host in hosts: 
		queue.put(host) 

	#wait on the queue until everything has been processed 
	queue.join() 

main() 
print "Elapsed Time: %s" % (time.time() - start)