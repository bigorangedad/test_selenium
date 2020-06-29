import _thread
import logging
import threading
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)

loops = [2, 4]

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def fun(self):
        self.func(*self.args)


def loop(nloop, nsec):
    """
    nloop: 第几个loop
    nsec: 第几秒，动态时间
    lock: 锁
    :param nloop:
    :param nsec:
    :param lock:
    :return:
    """
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())
    """
    释放锁 解锁
    """


def main():
    logging.info("start all at " + ctime())
    threads =[]
    """
    声明一个新的list
    """
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        """
        直接调重写的方法Mythread
        """
        threads.append(t)
        """
        因为threading.Thread不会立刻执行，需要调每一个Thread的start方法才会执行
        所以用一个线程的list把所有的线程包起来
        将每一个新生成的线程追加到list中
        """
    for i in nloops:
        threads[i].start()
        """
        然后调用每一个list中的线程，让他执行
        """
    for i in nloops:
        threads[i].join()
        """
        threading自带的方法,会等每一个threads[0 , 1 ...]结束，否则会卡在main方法里不结束，代替了锁的作用
        """
    logging.info("end all at " + ctime())



# def loop0():
#     logging.info("start loop0 at " + ctime())
#     sleep(4)
#
# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(2)

# def main():
#     logging.info("start all at " + ctime())
#     _thread.start_new_thread(loop0, ())
#     _thread.start_new_thread(loop1, ())
#     sleep(6)
#     # loop0()
#     # loop1()
#     # sleep(6)
#     logging.info("end all at " + ctime())

if __name__ == "__main__":
    main()
