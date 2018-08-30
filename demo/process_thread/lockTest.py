#!/usr/bin/env python
# -*- coding: utf8 -*-


import time, threading
# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()#lock
def  change_it(n):
	# 先存后取，结果应该为 0:
	global balance
	balance = balance + n
	balance = balance - n
def  run_thread(n):
	for i  in range(10):
		print 'run_thread(%d)\n' % (i)
		lock.acquire()#lock
		#time.sleep(1)
		try:
			print 'thread %s get this lock.' % threading.current_thread().name
			change_it(n)
		except Exception, e:
			print 'thread %s get can\'t lock.' % threading.current_thread().name
			print e
		finally:
			print 'thread %s release this lock.' % threading.current_thread().name
			lock.release()#lock
		
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(5,))
t3 = threading.Thread(target=run_thread, args=(5,))
t4 = threading.Thread(target=run_thread, args=(5,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print balance