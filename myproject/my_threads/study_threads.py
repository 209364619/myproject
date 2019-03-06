# coding=utf-8
import thread, threading
import time


class MyThread(threading.Thread):
    '''
    继承Thread类，构造函数中实现父类的构造方法
    实现接口run接口
    '''
    num = None

    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        for i in range(self.num):
            name = threading.currentThread().getName()
            info = name + ":\t" + str(i)
            print info


def my_print(name, num=10):
    for i in range(num):
        info = name + ":\t" + str(i)
        print info
        time.sleep(0.5)


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))


def start1():
    # try:
    thread.start_new_thread(my_print, ("t1",))
    thread.start_new_thread(my_print, ("t2",))
    # except:
    #     print "exception"


def start2():
    t1 = threading.Thread(target=my_print, name='thread1', args=('t1',))
    t2 = threading.Thread(target=my_print, name='thread2', args=('t2',))
    t1.start()
    t2.start()


def start3():
    t1 = MyThread(5)
    t2 = MyThread(9)
    # t1.setName("thread-1")
    # t2.setName("thread-2")
    t2.start()
    t1.start()


def start4_join_setdaemon():
    '''
    join()：在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    setDaemon(True):
    :return:
    '''
    t1 = threading.Thread(target=my_print, args=("thread-1", 10))
    t2 = threading.Thread(target=my_print, args=("thread-2", 10))
    threads = []
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        # t.setDaemon(True) #该参数将会导致当父进程结束以后子进程全部被挂起，无法执行
        t.start()
        t.join()  # 在该进程执行完成以前父进程将会被阻塞掉，
    # t1.join() #在t1 join()之后，t1线程将会获得执行权
    # t2.join()


gl_num = 1


def print_gl_num():
    global gl_num
    time.sleep(0.001)
    print threading.currentThread().getName(), ":", gl_num
    gl_num += 1


def start5_unlock():
    for i in range(10):
        t = threading.Thread(target=print_gl_num, args=())
        t.start()
    print 'test5 finished!'


lock = threading.RLock()


def print_gl_num_lock():
    lock.acquire()  # 获得锁
    time.sleep(0.001)
    global gl_num
    print threading.currentThread().getName(), gl_num
    gl_num += 1
    lock.release()


def start6_lock():
    for i in range(10):
        t = threading.Thread(target=print_gl_num_lock, args=())
        t.start()


product = None


def start7_produce_consume():
    condition = threading.Condition()

    def produce():
        global product
        if condition.acquire():
            while True:
                if product is None:
                    print '生产...'
                    product = "anything"
                    # 通知消费者消费
                    condition.notify()
                condition.wait()
                # time.sleep(2)

    def consume():
        global product
        if condition.acquire():
            while True:
                if product is not None:
                    print "消费..."
                    product = None
                    # 通知生产者生产
                    condition.notify()
                condition.wait()
                # time.sleep(2)

    t1 = threading.Thread(target=produce, name='Produce', args=())
    t2 = threading.Thread(target=consume, name='Consumer', args=())
    t1.start()
    t2.start()
    print 'Main process finished'


if __name__ == '__main__':
    # start5_unlock()
    # start6_lock()
    start7_produce_consume()
    # time.sleep(5)
