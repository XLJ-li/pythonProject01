#coding = utf-8
from threading import Thread
from time import sleep


def func1(name):
    print(f"线程{name},start")
    print(f"线程{name}")
    sleep(10)
    print(f"线程{name},end")


if __name__ == '__main__':
    # 创建线程
    t1 = Thread(target=func1, args=("t1",))
    t2 = Thread(target=func1, args=("t2",))
    # 启动线程
    t1.start()
    t2.start()
