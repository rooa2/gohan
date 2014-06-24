# -*- coding: utf-8 -*-

import tweepy

from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from module.user.api import create_user

class OauthTwitter(object):

    def get_oauth_handler(self):
        return tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)


    def get_api(self, access_token):
        handler = self.get_oauth_handler()
        handler.set_access_token(access_token.key, access_token.secret)
        return tweepy.API(auth_handler=handler)


    def post(self, request, tweet):
        handler = self.get_oauth_handler()
        access_token = request.session.get('access_token')
        api = self.get_api(access_token)
        api.update_status(tweet)


    def login(self, request):
        handler = self.get_oauth_handler()
        auth_url = handler.get_authorization_url()
        request.session['request_token'] = (handler.request_token.key, handler.request_token.secret)
        return auth_url


    def callback(self, request):
        verifier = request.GET.get('oauth_verifier')
        handler = self.get_oauth_handler()

        token = request.session.get('request_token')
        del request.session['request_token']
        handler.set_request_token(token[0], token[1])
        handler.get_access_token(verifier)

        request.session['access_token'] = handler.access_token
        create_user(request, self.get_api(handler.access_token).me())
        response = HttpResponseRedirect(reverse('main_index'))
        return response
