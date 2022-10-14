# coding = utf-8
from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"线程{self.name},start")
        print(f"线程{self.name}")
        sleep(10)
        print(f"线程{self.name},end")


if __name__ == '__main__':
    # 创建线程
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    # 启动线程
    t1.start()
    t2.start()
