# coding=utf-8
import json


def test():
    '''
    unicode编码的字符串依旧会被解析为中文，输出在console上面(pycharm 控制台正常输出，windows cmd 中 中文输出有问题)

    1.定义一个unicode字符串（类型为unicode，但是内容的本质为中文字符串）
    2.定义一个字符串，（字符串的unicode编码对应着中文）

    #### decode('unicode_escape')####
    3.通过将2中的字符串进行解码，获得字符串（unicode）对应的中文信息。

    :return:
    '''
    s = u'\u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8'
    print s
    s = r'\u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8'
    print type(s), s
    print s.decode('unicode_escape')


def str_unicode():
    '''
    str 和unicode转化,字符串的内容并不会发生变化，改变的仅仅是编码格式
    1.定义一个中文字符串，文件顶部声明了默认字符编码格式为utf-8，因此该字符串的默认编码为utf-8

    2.将字符串转化为unicode字符串
    :return:
    '''
    import chardet
    test_str = '中国'
    print test_str, type(test_str)  # 输出中国
    print '字符串的编码为：', chardet.detect(test_str)
    # 将utf-8 str转化为unicode
    # 方法一：
    # unicode_str = test_str.decode('utf-8')
    # 方法二：
    unicode_str = unicode(test_str, 'utf-8')
    print unicode_str, type(unicode_str)
    # unicode已经不再有编码格式了，以下代码将会报错
    # print 'str转化为unicode字符串后编码为：', chardet.detect(unicode_str)


def chinese_to_unicode():
    # 将汉字转化为unicode
    '''
    1.utf-8的字符串先解码为unicode
    2.unicode 编码（encode,动词）为字符串
    :return:
    '''
    str1 = '中国'
    unicode_style1 = str1.decode('utf-8').encode('unicode_escape')
    unicode_style2 = str1.decode('utf-8').encode('unicode_escape')[2:]

    print unicode_style1
    print unicode_style2


def unicode_to_chinese():
    '''
    将表示中文的unicode字符串转化为中文
    1.将字符串按照unicode进行解码即可获得unicode包含的中文信息，返回结果为unicode编码
    2.根据需要，将unicode编码在转变会字符串
    :return:
    '''
    str1 = '\u4e2d\u56fd'
    chinese_unicode = str1.decode('unicode_escape')
    print type(chinese_unicode), chinese_unicode
    # 将unicode转化为字符串
    chinese_str = chinese_unicode.encode('utf-8')
    print type(chinese_str), chinese_str


def console_list_unicode():
    '''
    解决从数据库中取出的中文数据由于unicode编码导致的无法正常显示，
    1.将list转化为str
    2.去除unicode编码的标识符  'u
    3.将字符串中的unicode编码转化为中文
    4.将unicode字符串转化为list       ===》   unicode--》str---》list
    :return:
    '''
    origin_list = [u'\u7b2c\u5341\u4e8c\u5c4a\u9ece\u5df4\u5ae9\u603b\u7edf',
                   u'\u963f\u5bcc\u6c57\u524d\u8d22\u653f\u90e8\u957f', u'leader', u'\u653f\u5ba2',
                   u'\u767d\u5bab\u65b0\u95fb\u79d8\u4e66', u'\u653f\u8981', u'\u767d\u5bab\u5236\u7247\u4eba',
                   u'\u767d\u5bab\u987e\u95ee', u'\u963f\u5bcc\u6c57\u524d\u5185\u653f\u90e8\u957f',
                   u'\u514b\u6797\u987f']
    # 去除unicode标识 'u
    case_list_righ = str(origin_list).replace('u\'', '\'')

    # 输出中文 unicode 编码
    list_chinese_unicode = case_list_righ.decode("unicode-escape")
    print '转化后类型:', type(list_chinese_unicode)
    print list_chinese_unicode

    # 将unicode编码转化为字符串，再转化为list
    chinese_unicode_to_str = list_chinese_unicode.encode('utf-8')
    print type(chinese_unicode_to_str), chinese_unicode_to_str

    # 将字符串转化为list
    chinese_list = list(chinese_unicode_to_str)
    print type(chinese_list), chinese_list


if __name__ == '__main__':
    console_list_unicode()
