# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def search_list():
    '''
    list遍历，查找元素对应下标，元素是否存在
    :return:
    '''
    my_list = ['一', '二', '三']

    # 查找根据下标查找list
    for i in range(len(my_list)):
        print i
        print my_list[i]

    # 根据元素查找所在list的下标
    print "根据元素查找所在list的下标"
    print my_list.index('一')
    target = '六'
    if target in my_list:
        print target, '在list中'
    else:
        print target, "不在list中"


# str 内容list转化为整形
def list_to_int():
    l1 = ["231231", "", "23213123"]
    for item in l1:
        if not item == "":
            rs = int(item)
            print rs


# list append 一个list
def append_list():
    '''
    list 每次只会append一个list的元素
    如果append的为list，list将会被认为是一个元素
    :return:
    '''
    list = [1, 2, 3, 4]
    list.append([5, 6, 7, 8])
    print list
    print len(list)


def list_and_str():
    '''

    :return:
    '''
    # 将list转化为str
    test_lsit = ['第十二届黎巴嫩总统', '阿富汗前财政部长', '政客', '白宫新闻秘书', '政要', '白宫制片人', '白宫顾问', '阿富汗前内政部长', '克林顿']
    list_to_str = ' '.join(test_lsit)
    print type(list_to_str), list_to_str

    # 将str转化为list
    str_to_list = list_to_str.split()
    print type(str_to_list)
    # 暂未解决直接print中文list在console中输出ascii。
    # 使用迭代输出即可查看中文,python3中将不会存在这个问题
    for item in str_to_list:
        print item
if __name__ == '__main__':
    mylist = []
    mylist.append('啦啦啦')
    print(mylist)
    mylist.append('啦啦啦')
    print(mylist)
    for item in mylist:
        print item
