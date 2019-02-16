# ！coding=utf-8
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.query import MultiMatch
from myproject import properties

import json

es_host = properties.ELASTIC_ADDR
es_port = properties.ELASTIC_PORT
tweets_index = properties.ELASTIC_TWEETS_INDEX

client = Elasticsearch(hosts=[{"host": es_host, "port": es_port}])


# 索引 doc_type 记录数添加
def test1():
    body1 = {
        "name": "zhangsan",
        "age": 23,
        "favorite": "张三喜欢篮球，足球，乒乓球，羽毛球，排球！",
        "sport": "篮球，足球，乒乓球，羽毛球，排球",
    }

    body2 = {
        "name": "lisi",
        "age": 34,
        "favorite": "李四喜欢篮球，足球，乒乓球，羽毛球，排球！，李四喜欢吃火锅",
        "sport": "篮球",
    }

    body3 = {
        "name": "王五",
        "age": 18,
        "favorite": "王五喜欢电子竞技，期待穿越火线",
        "sport": "gaming",
    }

    client.index(index='test-index', doc_type='test-doc', body=body1)
    client.index(index='test-index', doc_type='test-doc', body=body2)
    client.index(index='test-index', doc_type='test-doc', body=body3)


# 获取查询语句
def get_dsl(s):
    print json.dumps(s.to_dict(), ensure_ascii=False, indent=4)


def get_readable_rs(dict):
    json_str = json.dumps(dict, ensure_ascii=False, indent=4, encoding='utf-8')
    print json_str


# 单字段全文检索
def single_match():
    '''
    单一字段匹配
    :return:
    '''
    s = Search(using=client, index='test-index')
    s = s.query('match', favorite="李四")
    get_dsl(s)
    response = s.execute()
    for hit in response:
        hit_dic = hit.to_dict()
        get_readable_rs(hit_dic)


# 多字段全文检索
def test2():
    s = Search(using=client, index='test-index')
    q = Q('multi_match', query='李四', fields=['favorite', 'sport'])
    s = s.query(q)
    # s = s.query('multi_match', query='火', fields=['favorite','sport'])
    print json.dumps(s.to_dict(), ensure_ascii=False, indent=4)
    response = s.execute()
    for hit in response:
        hit_dict = hit.to_dict()
        print json.dumps(hit_dict, ensure_ascii=False, indent=4)


# 通过query 删除记录，出错，未解决
def test3():
    s = Search(using=client, index='test-index').query('match', sport='gaming')
    get_dsl(s)
    # print '检索匹配记录：'
    # response = s.execute()
    # for hit in response:
    #     get_readable_rs(hit.to_dict())
    # get_dsl(s)
    print '删除记录：'
    s.delete()
    print '删除后记录：'
    response = s.execute()
    for hit in response:
        get_readable_rs(hit.to_dict())


def test4():
    pass


def test5():
    s = Search(using=client, index='test-index')

    # s[from:end] 选取end - from 条
    s = s[1:3]
    get_dsl(s)

    response = s.execute()
    for hit in response:
        get_readable_rs(hit.to_dict())


def test6():
    s = Search(using=client, index='test-index')

    s = s.query('match', sport='足球')
    s = s.highlight('sport')
    response = s.execute()
    for hit in response:
        from elasticsearch_dsl.utils import AttrList
        rs = hit.meta.highlight.sport


if __name__ == '__main__':
