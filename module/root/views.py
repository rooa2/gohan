# -*- coding: utf-8 -*-
import datetime
import uuid

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    params = {}
    return render_to_response('root/index.html', context_instance=RequestContext(request, params))

