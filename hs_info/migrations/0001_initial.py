# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HsInfo'
        db.create_table(u'hs_info_hsinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users_manage.Users'])),
            ('week_limited', self.gf('django.db.models.fields.IntegerField')(max_length=256, null=True, blank=True)),
            ('month_limited', self.gf('django.db.models.fields.IntegerField')(max_length=256, null=True, blank=True)),
            ('is_seller', self.gf('django.db.models.fields.BooleanField')()),
            ('sign_required', self.gf('django.db.models.fields.BooleanField')()),
            ('shop_type', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('reputation_gt', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('not_do', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('city_and_sector', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('chat_required', self.gf('django.db.models.fields.BooleanField')()),
            ('other_info', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('min_payment', self.gf('django.db.models.fields.IntegerField')(max_length=128)),
            ('max_payment', self.gf('django.db.models.fields.IntegerField')(max_length=128)),
        ))
        db.send_create_signal(u'hs_info', ['HsInfo'])


    def backwards(self, orm):
        # Deleting model 'HsInfo'
        db.delete_table(u'hs_info_hsinfo')


    models = {
        u'hs_info.hsinfo': {
            'Meta': {'object_name': 'HsInfo'},
            'chat_required': ('django.db.models.fields.BooleanField', [], {}),
            'city_and_sector': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_seller': ('django.db.models.fields.BooleanField', [], {}),
            'max_payment': ('django.db.models.fields.IntegerField', [], {'max_length': '128'}),
            'min_payment': ('django.db.models.fields.IntegerField', [], {'max_length': '128'}),
            'month_limited': ('django.db.models.fields.IntegerField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'not_do': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'other_info': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'reputation_gt': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'shop_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'sign_required': ('django.db.models.fields.BooleanField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users_manage.Users']"}),
            'week_limited': ('django.db.models.fields.IntegerField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'users_manage.users': {
            'Meta': {'object_name': 'Users'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hs_info']