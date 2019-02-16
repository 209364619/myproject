from django.shortcuts import render
from django.http import HttpResponseRedirect
import properties


def go_to_es(request):
    context = {}
    context['head_addr'] = properties.ELASTIC_HEAD_ADDR
    return render(request, "elasticsearch.html", context)


def go_to_dashboard(request):
    return HttpResponseRedirect(properties.KUBERNETES)


def go_to_grafna(request):
    return HttpResponseRedirect(properties.GRAFNA)


def go_to_tweets(request):
    return render(request, "tweets.html")
