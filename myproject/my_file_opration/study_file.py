# coding=utf-8
import time
import json

'''
python 文件读写操作

使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。


'''


def write():
    f = open("test.txt", 'w')
    for i in range(10):
        current = time.asctime(time.localtime())
        dict = {}
        dict['time'] = current
        f.write(json.dumps(dict) + '\n')
        time.sleep(1)
    f.close()


def read_line1():
    f = open('test.txt', 'r')
    line = f.readline()
    while line:
        each = json.loads(line)
        print type(line), "\t", line
        line = f.readline()
    f.close()


def read_line2():
    f = open('test.txt', 'r')
    for line in f:
        print line
    f.close()


if __name__ == '__main__':
    read_line2()
