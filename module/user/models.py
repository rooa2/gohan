# -*- coding: utf-8 -*-

import datetime
from django.db import models
from django.conf import settings

class User(models.Model):
    user_id = models.IntegerField(u'ユーザーID', db_index=True)
    access_token_key = models.CharField(u'アクセストークンキー', max_length=255)
    access_token_secret = models.CharField(u'アクセストークンsecret', max_length=255)
    create_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    update_at = models.DateTimeField(u'更新日時', auto_now=True)

    @property
    def expire_date(self):
        expire = datetime.timedelta(days=settings.TOKEN_EXPIRE)
        return self.update_at + expire
