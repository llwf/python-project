import time, threading, multiprocessing

def loop():
		print('thread %s is running...' % threading.current_thread().name)
		n = 0
		while n < 5:
			n = n + 1
			print('thread %s >>> %s' % (threading.current_thread().name, n))
			time.sleep(1)
		print('thread %s ended.' % threading.current_thread().name)
	
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target = loop, name = 'LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

balance = 99
lock = threading.Lock()
def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n
	balance = balance*n
	balance = balance/n
	
def run_thread(n):
	for i in range(1000000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()
			
start = time.time()
thread_list = []
for i in range(1, 1000):
	thread_list.append(threading.Thread(target = change_it, args = (i,)))
for t in thread_list:
	t.start()
for t in thread_list:
	t.join()	
end = time.time()
print('balance: %s spend time %s' % (balance, end - start))

print('++++++++++++++x*x:', 5^2)
def loop_dead():
	x = 0
	while True:
		x = x^1

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target = loop_dead)
	t.start()
	

	