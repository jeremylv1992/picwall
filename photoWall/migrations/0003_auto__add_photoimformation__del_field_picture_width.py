# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PhotoImformation'
        db.create_table(u'photoWall_photoimformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photoWall.Picture'])),
            ('photo_wall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photoWall.PhotoWall'])),
            ('positionX', self.gf('django.db.models.fields.FloatField')()),
            ('positionY', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'photoWall', ['PhotoImformation'])

        # Deleting field 'Picture.width'
        db.delete_column(u'photoWall_picture', 'width')


    def backwards(self, orm):
        # Deleting model 'PhotoImformation'
        db.delete_table(u'photoWall_photoimformation')


        # User chose to not deal with backwards NULL issues for 'Picture.width'
        raise RuntimeError("Cannot reverse this migration. 'Picture.width' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Picture.width'
        db.add_column(u'photoWall_picture', 'width',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


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
            'access_user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['photoWall.User']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'photoWall.picture': {
            'Meta': {'object_name': 'Picture'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photoWall.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'photoWall.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['photoWall']