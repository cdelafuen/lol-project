# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from lol.collector.models import Champion


def home(request):
    champions = Champion.objects.all().order_by('name')
    return render_to_response('base.html', locals(), RequestContext(request))