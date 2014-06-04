# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PhotoWall.creator'
        db.add_column(u'photoWall_photowall', 'creator',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='creator+', to=orm['photoWall.User']),
                      keep_default=False)

        # Adding field 'PhotoWall.description'
        db.add_column(u'photoWall_photowall', 'description',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=256),
                      keep_default=False)

        # Removing M2M table for field access_user on 'PhotoWall'
        db.delete_table(db.shorten_name(u'photoWall_photowall_access_user'))

        # Adding M2M table for field access_users on 'PhotoWall'
        m2m_table_name = db.shorten_name(u'photoWall_photowall_access_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowall', models.ForeignKey(orm[u'photoWall.photowall'], null=False)),
            ('user', models.ForeignKey(orm[u'photoWall.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photowall_id', 'user_id'])


    def backwards(self, orm):
        # Deleting field 'PhotoWall.creator'
        db.delete_column(u'photoWall_photowall', 'creator_id')

        # Deleting field 'PhotoWall.description'
        db.delete_column(u'photoWall_photowall', 'description')

        # Adding M2M table for field access_user on 'PhotoWall'
        m2m_table_name = db.shorten_name(u'photoWall_photowall_access_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowall', models.ForeignKey(orm[u'photoWall.photowall'], null=False)),
            ('user', models.ForeignKey(orm[u'photoWall.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photowall_id', 'user_id'])

        # Removing M2M table for field access_users on 'PhotoWall'
        db.delete_table(db.shorten_name(u'photoWall_photowall_access_users'))


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