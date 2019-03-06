# coding=utf-8
from dwebsocket import accept_websocket, require_websocket
from django.shortcuts import render


# 建立websocket连接
@require_websocket
def created_connection(request):
    message = request.websocket.wait()
    request.websocket.send(message)


@accept_websocket
def always_connection(request):
    if request.is_websocket():
        for message in request.websocket:
            request.websocket.send(message)  # 发送消息到客户端
    else:
        try:  # 如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'index.html')


@accept_websocket
def tweets_connect(request):
    if request.is_websocket():
        for item in list:
            request.websocket.send(item)
