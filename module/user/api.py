# -*- coding: utf-8 -*-
from module.user import models

def create_user(request, me):
    access_token = request.session.get('access_token')
    user ,_ = models.User.objects.get_or_create(user_id=me.id, access_token_key=access_token.key, access_token_secret=access_token.secret)
    return user
