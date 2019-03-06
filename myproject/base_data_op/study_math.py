# coding=utf-8

# python 乘方
def test1(di, mi):
    return di ** mi


'''
    python 函数参数个数
    *arg 表示的是一个tuple
    **karg表示可以传入一个字典
'''


def test2_tuple(name, *args):
    print "Myname is :", name
    for item in args:
        print "this is an item in tuple:", item


def test3_dict(name, **kwargs):
    print "Myname is :", name
    for key in kwargs:
        print key, ':\t', kwargs[key]


if __name__ == '__main__':
    # print test1(3,3) # 3的3次方
    # test2_tuple("python",('cat','dog','elephant'))
    kwargs = {'animals': 'dog', 'book': 'python', 'game': 'snake'}
    test3_dict(name='python', **kwargs)
