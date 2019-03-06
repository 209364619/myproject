# coding=utf-8

from django.http import JsonResponse
from es_entity import EsHelper
from myproject.my_decorator.study_decorator import recorder


@recorder
def get_record_by_keyword(request):
    dict = {}
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        size = (int)(request.POST.get('size').encode('utf-8'))
        pageNum = (int)(request.POST.get('pageNum').encode('utf-8'))
        es_helper = EsHelper()
        rs = es_helper.search_by_keyword(keyword, size, pageNum)
    dict['status'] = 'success'
    dict['text'] = rs
    return JsonResponse(dict)
