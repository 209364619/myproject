# coding=utf-8
'''
python 中的dict可以直接使用str转化为字符串类型，转化后的字符串虽然类似json格式
但是与json字符串有区别，str转化的dict被双引号包裹，无法被python中的load方法解析。
'''


def test_get():
    dict = {"name": "zhangsan", "age": 15}
    # get方法的好处：key不存在返回None
    print dict.get('name')
    print dict.get('sex')
    # 使用中括号直接取值会有异常
    print dict['name']
    # print dict['sex'] #这里会发生异常


def str_between_load():
    import json
    dict = {'name': 'zhangsan', 'age': '15'}
    print dict
    print str(dict)
    print json.dumps(dict)  # 使用该方法导出的才是json字符串


if __name__ == '__main__':
    str_between_load()
dict = {
    "mane": "zhang",
    "age": "15",
    "friend": ['1', '2', '3', '4', '5']
}
