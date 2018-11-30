from django.shortcuts import render
import properties


def go_to_es(request):
    context = {}
    context['head_addr'] = properties.ELASTIC_HEAD_ADDR
    return render(request, "elasticsearch.html", context)
