# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Notdo.notdo'
        db.add_column(u'hs_info_notdo', 'notdo',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hs_info.HsInfo'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'HsInfo.not_do'
        db.add_column(u'hs_info_hsinfo', 'not_do',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field not_do on 'HsInfo'
        db.delete_table(db.shorten_name(u'hs_info_hsinfo_not_do'))


    def backwards(self, orm):
        # Deleting field 'Notdo.notdo'
        db.delete_column(u'hs_info_notdo', 'notdo_id')

        # Deleting field 'HsInfo.not_do'
        db.delete_column(u'hs_info_hsinfo', 'not_do')

        # Adding M2M table for field not_do on 'HsInfo'
        m2m_table_name = db.shorten_name(u'hs_info_hsinfo_not_do')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hsinfo', models.ForeignKey(orm[u'hs_info.hsinfo'], null=False)),
            ('notdo', models.ForeignKey(orm[u'hs_info.notdo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hsinfo_id', 'notdo_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hs_info.hsinfo': {
            'Meta': {'object_name': 'HsInfo'},
            'chat_required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'city_and_sector': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_seller': ('django.db.models.fields.BooleanField', [], {}),
            'max_payment': ('django.db.models.fields.IntegerField', [], {'default': '999', 'max_length': '128'}),
            'min_payment': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '128'}),
            'month_limited': ('django.db.models.fields.IntegerField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'not_do': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'other_info': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'reputation_gt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shop_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sign_required': ('django.db.models.fields.BooleanField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'week_limited': ('django.db.models.fields.IntegerField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'hs_info.notdo': {
            'Meta': {'object_name': 'Notdo'},
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notdo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hs_info.HsInfo']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hs_info']