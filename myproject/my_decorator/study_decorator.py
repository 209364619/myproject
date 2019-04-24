# coding=utf-8

import time
import logging
import json


def timeit(func):
    '''
    函数执行时间装饰器
    :param func:
    :return:
    '''

    def wapper(num):
        start = time.time()
        func(num)
        end = time.time()
        message = {}
        message['execute_time'] = end - start
        message['start_time'] = start
        message['end'] = end

        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.INFO)

        handler = logging.FileHandler('log.txt')
        handler.setLevel(level=logging.INFO)

        formater = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-: %(message)s')
        # formater = logging.Formatter('%(message)s')
        handler.setFormatter(formater)

        logger.addHandler(handler)

        logger.info(message)

    return wapper


@timeit
def foo(num):
    print 'in foo()'
    for i in range(num):
        sum = i ** i


##-----------------------------------------------------------------##
def bread(func):
    def wapper():
        print "</'''       '''\>"
        func()
        print "<\______/>"

    return wapper


def ingredients(func):
    def wrapper():
        print "#tomatoes#"
        func()
        print "~salad~"

    return wrapper


@bread
@ingredients
def sandwich(food="--ham--"):
    print food


##-----------------------------------------------------------------##

def client_ip(func):
    '''
    获取用户登录ip装饰器
    :param func:
    :return:
    '''

    def wapper(request):
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        print ip
        rs = func(request)
        return rs

    return wapper


def log_file_name():
    format_time_str = time.strftime('%Y_%m_%d', time.localtime(time.time()))
    log_dir = format_time_str + ".log"
    return log_dir


def login_ip(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def recorder(func):
    def wapper(request):
        start = time.time()
        response = func(request)
        end = time.time()
        es_excute_time = end - start

        client_ip = login_ip(request)

        message = {"login_ip": client_ip, "start_time": start, "es_search_time": es_excute_time}
        message = json.dumps(message)

        log_filename = log_file_name()

        handler = logging.FileHandler(log_filename)
        handler.setLevel(level=logging.INFO)

        formater = logging.Formatter('%(message)s')
        handler.setFormatter(formater)

        logger.addHandler(handler)
        logger.info(message)
        logger.removeHandler(handler)
        return response

    return wapper


@recorder
def writer(msg):
    print msg


if __name__ == '__main__':
    w = recorder(writer("lalal"))
    # writer('using python grammar suger')
