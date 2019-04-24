# coding=utf-8
from fdfs_client.client import Fdfs_client
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

client = Fdfs_client('F:\python workspace\myproject\myproject\my_fdfs\client.conf')


def jump_page(request):
    return render(request, 'fdfs.html')


def upload_file_by_buffer(request):
    upload_info = {}
    if request.method == 'POST':
        file = request.FILES.get('upload_file')
        upload_info = client.upload_by_buffer(file.read())
    else:
        pass
    return JsonResponse(upload_info)


def upload_file_by_file_name(file_path):
    upload_info = client.upload_by_filename(file_path)
    print upload_info


from django.core.files.uploadedfile import TemporaryUploadedFile

if __name__ == '__main__':
    upload_file_by_file_name('QQ20190324112411.jpg')
