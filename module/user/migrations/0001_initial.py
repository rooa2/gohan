# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('user_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('access_token_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('create_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('user', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('user_user')


    models = {
        'user.user': {
            'Meta': {'object_name': 'User'},
            'access_token_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['user']