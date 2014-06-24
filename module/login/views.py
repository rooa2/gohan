# -*- coding: utf-8 -*-
import datetime
import uuid

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from module.oauth.twitter_oauth import OauthTwitter


def index(request):
    params = {}
    return render_to_response('login/index.html', context_instance=RequestContext(request, params))


def account(request):
    if settings.DEBUG:
        now = datetime.datetime.now()
        expire = datetime.timedelta(days=settings.TOKEN_EXPIRE)
        expire_date = now + expire
        response = HttpResponseRedirect(reverse('main_index'))
        response.set_cookie('sessionid', value=uuid.uuid4(), expires=expire_date)
        return response
    auth_url = OauthTwitter().login(request)
    return HttpResponseRedirect(auth_url)


def callback(request):
    response = OauthTwitter().callback(request)
    return response


def logout(request):
    response = HttpResponseRedirect(reverse('login_index'))
    response.delete_cookie('sessionid')
    return response
