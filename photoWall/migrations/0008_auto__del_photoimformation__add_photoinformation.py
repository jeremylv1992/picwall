# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PhotoImformation'
        db.delete_table(u'photoWall_photoimformation')

        # Adding model 'PhotoInformation'
        db.create_table(u'photoWall_photoinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photoWall.Picture'])),
            ('photo_wall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photoWall.PhotoWall'])),
            ('positionX', self.gf('django.db.models.fields.FloatField')()),
            ('positionY', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'photoWall', ['PhotoInformation'])


    def backwards(self, orm):
        # Adding model 'PhotoImformation'
        db.create_table(u'photoWall_photoimformation', (
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photoWall.Picture'])),
            ('positionX', self.gf('django.db.models.fields.FloatField')()),
            ('positionY', self.gf('django.db.models.fields.FloatField')()),
            ('photo_wall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photoWall.PhotoWall'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'photoWall', ['PhotoImformation'])

        # Deleting model 'PhotoInformation'
        db.delete_table(u'photoWall_photoinformation')


    models = {
        u'photoWall.photoinformation': {
            'Meta': {'object_name': 'PhotoInformation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo_wall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photoWall.PhotoWall']"}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photoWall.Picture']"}),
            'positionX': ('django.db.models.fields.FloatField', [], {}),
            'positionY': ('django.db.models.fields.FloatField', [], {})
        },
        u'photoWall.photowall': {
            'Meta': {'object_name': 'PhotoWall'},
            'access_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['photoWall.User']", 'symmetrical': 'False'}),
            'create_data': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 6, 5, 0, 0)'}),
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