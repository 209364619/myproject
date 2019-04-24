# coding=utf-8
import chardet


def get_file_encoding(filepath):
    '''
    获取文件默认编码格式
    存在问题：
        window记事本默认编码格式为ANSI编码，一般来说应该是GB2312但是也可能给你小小的surprise(初步猜测
        复制到pycharm的时候编码被改了)
    :param filepath: str 文件路径
    :return: str 编码
    '''
    with open(filepath, 'rb') as file:
        data = file.read()
        coder = chardet.detect(data)
        return coder['encoding']


def read_file_by_own_encode(filepath):
    '''

    :param filepath: 文件绝对路径
    :return: str 文件
    '''
    file = open(filepath, 'rb')
    data = file.read()
    coder = chardet.detect(data)
    print coder
    text = data.decode(coder.get('encoding'))
    print chardet.detect(text.encode('utf-8'))
    file.close()


if __name__ == '__main__':
    print(get_file_encoding('C:\Users\y500\Desktop\window.txt'))
