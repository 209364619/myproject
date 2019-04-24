# coding=utf-8
from study_tweets_api import Tweets
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def get_tweets_by_api(request):
    keyword = None
    num = None
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        num = request.POST['num']
    result = {}
    # 通过关键词采集推文
    op = Tweets()
    # 采集数量默认为1
    if num is None:
        num = 5

    if keyword:
        rs = op.get_tweet_by_key_word(keyword=keyword, num=num)
        if rs['status'] == 'success':
            result['status'] = 'success'

        else:
            result['status'] = 'false'
            result['msg'] = '采集失败'
    else:
        result['msg'] = '未输入关键词'
    return JsonResponse(result)
