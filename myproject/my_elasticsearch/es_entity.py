# coding=utf-8

from elasticsearch_dsl import Search
from elasticsearch import Elasticsearch
from django.http import JsonResponse

ELASTIC_ADDR = "192.168.8.200"
ELASTIC_PORT = 9201


class EsHelper:
    client = None
    index = None

    def __init__(self):
        self.client = Elasticsearch([{"host": ELASTIC_ADDR, "port": ELASTIC_PORT}])
        self.index = 'tweets*'

    def replace_highlight(self, sentence):
        a = sentence.replace("<em>", "<font color=\"#FF0000\">")
        b = a.replace("</em>", "</font>")
        return b

    def search_by_keyword1(self, keyword):
        s = Search(using=self.client, index=self.index)
        s = s.query('match', text=keyword)
        s = s.highlight('text')
        response = s.execute()
        rs_list = []
        rs_dict = {}
        for hit in response:
            for highlight_result in hit.meta.highlight.text:
                rs_list.append(self.replace_highlight(highlight_result))
        return rs_list

    def search_by_keyword(self, keyword, size=10, pageNum=1):
        s = Search(using=self.client, index=self.index)
        s = s.query('match', text=keyword)
        s = s[(pageNum - 1) * size:pageNum * size]
        s = s.highlight('text')
        response = s.execute()
        rs_list = []
        rs_dict = {}
        for hit in response:
            for highlight_result in hit.meta.highlight.text:
                rs_list.append(self.replace_highlight(highlight_result))
        return rs_list


if __name__ == '__main__':
    es_helper = EsHelper()
    list = es_helper.search_by_keyword('中国')
    print len(list)
