# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PhotoInformation.width'
        db.add_column(u'picwall_photoinformation', 'width',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=16),
                      keep_default=False)

        # Adding field 'PhotoInformation.height'
        db.add_column(u'picwall_photoinformation', 'height',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=16),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PhotoInformation.width'
        db.delete_column(u'picwall_photoinformation', 'width')

        # Deleting field 'PhotoInformation.height'
        db.delete_column(u'picwall_photoinformation', 'height')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'picwall.photoinformation': {
            'Meta': {'object_name': 'PhotoInformation'},
            'height': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'photo_wall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.PhotoWall']"}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.pw_pic']"}),
            'top': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'picwall.photowall': {
            'Meta': {'object_name': 'PhotoWall'},
            'access_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'create_data': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 6, 6, 0, 0)'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator+'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'picwall.pic_comment': {
            'Meta': {'ordering': "('published_date',)", 'object_name': 'pic_comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.pw_pic']"}),
            'published_date': ('django.db.models.fields.DateField', [], {})
        },
        u'picwall.pw_pic': {
            'Meta': {'object_name': 'pw_pic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic_author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'pic_desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pic_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pic_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pic_upload_time': ('django.db.models.fields.DateTimeField', [], {}),
            'pic_url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'picwall.pw_user': {
            'Meta': {'object_name': 'pw_user'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        }
    }

    complete_apps = ['picwall']