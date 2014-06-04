# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PhotoWall'
        db.create_table(u'photoWall_photowall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'photoWall', ['PhotoWall'])

        # Adding M2M table for field access_user on 'PhotoWall'
        m2m_table_name = db.shorten_name(u'photoWall_photowall_access_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowall', models.ForeignKey(orm[u'photoWall.photowall'], null=False)),
            ('user', models.ForeignKey(orm[u'photoWall.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photowall_id', 'user_id'])

        # Adding field 'Picture.width'
        db.add_column(u'photoWall_picture', 'width',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'PhotoWall'
        db.delete_table(u'photoWall_photowall')

        # Removing M2M table for field access_user on 'PhotoWall'
        db.delete_table(db.shorten_name(u'photoWall_photowall_access_user'))

        # Deleting field 'Picture.width'
        db.delete_column(u'photoWall_picture', 'width')


    models = {
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'width': ('django.db.models.fields.FloatField', [], {})
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