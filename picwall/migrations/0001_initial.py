# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'pw_pic'
        db.create_table(u'picwall_pw_pic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pic_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pic_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pic_desc', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pic_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pic_upload_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('pic_author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'picwall', ['pw_pic'])

        # Adding model 'pw_user'
        db.create_table(u'picwall_pw_user', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'picwall', ['pw_user'])

        # Adding model 'pic_comment'
        db.create_table(u'picwall_pic_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('pic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.pw_pic'])),
            ('published_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'picwall', ['pic_comment'])

        # Adding model 'PhotoWall'
        db.create_table(u'picwall_photowall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creator+', to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('createdDate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'picwall', ['PhotoWall'])

        # Adding M2M table for field access_users on 'PhotoWall'
        m2m_table_name = db.shorten_name(u'picwall_photowall_access_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowall', models.ForeignKey(orm[u'picwall.photowall'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photowall_id', 'user_id'])

        # Adding model 'PhotoInformation'
        db.create_table(u'picwall_photoinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.pw_pic'])),
            ('photo_wall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.PhotoWall'])),
            ('positionX', self.gf('django.db.models.fields.FloatField')()),
            ('positionY', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'picwall', ['PhotoInformation'])


    def backwards(self, orm):
        # Deleting model 'pw_pic'
        db.delete_table(u'picwall_pw_pic')

        # Deleting model 'pw_user'
        db.delete_table(u'picwall_pw_user')

        # Deleting model 'pic_comment'
        db.delete_table(u'picwall_pic_comment')

        # Deleting model 'PhotoWall'
        db.delete_table(u'picwall_photowall')

        # Removing M2M table for field access_users on 'PhotoWall'
        db.delete_table(db.shorten_name(u'picwall_photowall_access_users'))

        # Deleting model 'PhotoInformation'
        db.delete_table(u'picwall_photoinformation')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo_wall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.PhotoWall']"}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.pw_pic']"}),
            'positionX': ('django.db.models.fields.FloatField', [], {}),
            'positionY': ('django.db.models.fields.FloatField', [], {})
        },
        u'picwall.photowall': {
            'Meta': {'object_name': 'PhotoWall'},
            'access_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'createdDate': ('django.db.models.fields.DateField', [], {}),
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