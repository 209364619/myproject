# coding=utf-8
from django.shortcuts import render
from pymongo import MongoClient


def login(request):
    return render(request, "index.html")


def login_check(request):
    context = {}
    username = request.POST.get('username')
    password = request.POST.get('password')
    print username, password
    if username is None:
        context['info'] = '用户名不能为空！'
    else:
        from myproject import properties
        client = MongoClient(properties.MONGO_ADDR, properties.MONGO_PORT)
        userdb = client['users']
        users = userdb['user']
        user = users.find_one()
        if user is None:
            context['info'] = "用户不存在！"
        else:
            if user['password'] == password:
                request.session['username'] = username
                context['info'] = 'success!'
                return render(request, "navi.html", context)
            else:
                context['info'] = '密码错误！'
    return render(request, "index.html", context)


def logout(request):
    del request.session['username']
    return render(request, 'index.html', None)


def hello(request):
    return render(request, "hello.html")


def navi_helper(request):
    rs = request.session.get('username', None)
    print rs
    if rs is not None:
        return render(request, "navi.html", None)
    else:
        return render(request, "index.html", None)
