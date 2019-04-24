"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from loginUnit import login
import pageguide
from tweets import tweets_controller
from my_dwebsocket import controller
from my_elasticsearch import es_controller
from my_fdfs import fastdfs_controller
from my_hdfs import hdfs_controller

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', login.hello),
    url(r'^login_check/', login.login_check),
    url(r'^logout/', login.logout, name='logout'),
    url(r'^my_elasticsearch/', pageguide.go_to_es, name='es'),
    url(r'^kube_dashboard/', pageguide.go_to_dashboard, name='kubeDashboard'),
    url(r'^grafna/', pageguide.go_to_grafna, name='grafna'),
    url(r'^tweets/', pageguide.go_to_tweets, name='tweets'),
    url(r'^get_tweets_by_keyword', tweets_controller.get_tweets_by_api, name='get_tweets_by_keyword'),
    # websocket
    url(r'^websocket_test', controller.created_connection),
    url(r'^websocket_always', controller.always_connection),
    url(r'^get_tweets', controller.tweets_connect),
    # my_elasticsearch
    url(r'^search_by_keyword', es_controller.get_record_by_keyword, name='search_by_keyword'),
    url(r'^encrypt', pageguide.go_to_encrypt, name='encrypt'),

    # fastdfs
    url(r'fastdfs/', fastdfs_controller.jump_page, name='fastdfs'),
    url(r'^fdfs_upload/', fastdfs_controller.upload_file_by_buffer, name='fdfs_upload'),

    # hdfs
    url(r'hdfs/', hdfs_controller.jump_to_page, name='hdfs'),
    url(r'^$', login.navi_helper),
]
