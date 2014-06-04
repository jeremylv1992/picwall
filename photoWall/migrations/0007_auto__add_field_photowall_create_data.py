# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PhotoWall.create_data'
        db.add_column(u'photoWall_photowall', 'create_data',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 6, 4, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PhotoWall.create_data'
        db.delete_column(u'photoWall_photowall', 'create_data')


    models = {
        u'photoWall.photoimformation': {
            'Meta': {'object_name': 'PhotoImformation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo_wall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photoWall.PhotoWall']"}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photoWall.Picture']"}),
            'positionX': ('django.db.models.fields.FloatField', [], {}),
            'positionY': ('django.db.models.fields.FloatField', [], {})
        },
        u'photoWall.photowall': {
            'Meta': {'object_name': 'PhotoWall'},
            'access_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['photoWall.User']", 'symmetrical': 'False'}),
            'create_data': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 6, 4, 0, 0)'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator+'", 'to': u"orm['photoWall.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'photoWall.picture': {
            'Meta': {'object_name': 'Picture'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photoWall.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'src': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'photoWall.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['photoWall']