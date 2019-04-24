# coding=utf-8
from django.shortcuts import render


def jump_to_page(request):
    return render(request, 'hdfs.html')
