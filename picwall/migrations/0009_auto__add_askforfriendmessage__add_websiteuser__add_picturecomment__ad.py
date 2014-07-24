# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AskForFriendMessage'
        db.create_table(u'picwall_askforfriendmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sent_messages', to=orm['picwall.WebSiteUser'])),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='received_messages', to=orm['picwall.WebSiteUser'])),
            ('ask_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 24, 0, 0))),
            ('state', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=10)),
        ))
        db.send_create_signal(u'picwall', ['AskForFriendMessage'])

        # Adding model 'WebSiteUser'
        db.create_table(u'picwall_websiteuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='webuser', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'picwall', ['WebSiteUser'])

        # Adding M2M table for field friends on 'WebSiteUser'
        m2m_table_name = db.shorten_name(u'picwall_websiteuser_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_websiteuser', models.ForeignKey(orm[u'picwall.websiteuser'], null=False)),
            ('to_websiteuser', models.ForeignKey(orm[u'picwall.websiteuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_websiteuser_id', 'to_websiteuser_id'])

        # Adding model 'PictureComment'
        db.create_table(u'picwall_picturecomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.Picture'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.WebSiteUser'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('published_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 24, 0, 0))),
        ))
        db.send_create_signal(u'picwall', ['PictureComment'])

        # Adding model 'PhotoInformation'
        db.create_table(u'picwall_photoinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.Picture'])),
            ('photowall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.PhotoWall'])),
            ('left', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('top', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('width', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'picwall', ['PhotoInformation'])

        # Adding model 'PictureLabel'
        db.create_table(u'picwall_picturelabel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_labels', to=orm['picwall.WebSiteUser'])),
        ))
        db.send_create_signal(u'picwall', ['PictureLabel'])

        # Adding model 'Picture'
        db.create_table(u'picwall_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='name', max_length=32)),
            ('description', self.gf('django.db.models.fields.CharField')(default='description', max_length=64)),
            ('upload_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.WebSiteUser'])),
            ('label', self.gf('django.db.models.fields.related.ForeignKey')(related_name='label_pics', to=orm['picwall.PictureLabel'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'picwall', ['Picture'])

        # Adding model 'PhotowallComment'
        db.create_table(u'picwall_photowallcomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pw', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.PhotoWall'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.WebSiteUser'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('published_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 24, 0, 0))),
        ))
        db.send_create_signal(u'picwall', ['PhotowallComment'])

        # Adding model 'PhotoWall'
        db.create_table(u'picwall_photowall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photowalls', to=orm['picwall.WebSiteUser'])),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=256)),
            ('access_permission', self.gf('django.db.models.fields.CharField')(default='private', max_length=10)),
            ('create_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 24, 0, 0))),
            ('modify_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 24, 0, 0))),
            ('access_times', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'picwall', ['PhotoWall'])

        # Adding M2M table for field access_users on 'PhotoWall'
        m2m_table_name = db.shorten_name(u'picwall_photowall_access_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowall', models.ForeignKey(orm[u'picwall.photowall'], null=False)),
            ('websiteuser', models.ForeignKey(orm[u'picwall.websiteuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photowall_id', 'websiteuser_id'])

        # Adding M2M table for field manage_users on 'PhotoWall'
        m2m_table_name = db.shorten_name(u'picwall_photowall_manage_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowall', models.ForeignKey(orm[u'picwall.photowall'], null=False)),
            ('websiteuser', models.ForeignKey(orm[u'picwall.websiteuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photowall_id', 'websiteuser_id'])


    def backwards(self, orm):
        # Deleting model 'AskForFriendMessage'
        db.delete_table(u'picwall_askforfriendmessage')

        # Deleting model 'WebSiteUser'
        db.delete_table(u'picwall_websiteuser')

        # Removing M2M table for field friends on 'WebSiteUser'
        db.delete_table(db.shorten_name(u'picwall_websiteuser_friends'))

        # Deleting model 'PictureComment'
        db.delete_table(u'picwall_picturecomment')

        # Deleting model 'PhotoInformation'
        db.delete_table(u'picwall_photoinformation')

        # Deleting model 'PictureLabel'
        db.delete_table(u'picwall_picturelabel')

        # Deleting model 'Picture'
        db.delete_table(u'picwall_picture')

        # Deleting model 'PhotowallComment'
        db.delete_table(u'picwall_photowallcomment')

        # Deleting model 'PhotoWall'
        db.delete_table(u'picwall_photowall')

        # Removing M2M table for field access_users on 'PhotoWall'
        db.delete_table(db.shorten_name(u'picwall_photowall_access_users'))

        # Removing M2M table for field manage_users on 'PhotoWall'
        db.delete_table(db.shorten_name(u'picwall_photowall_manage_users'))


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
        u'picwall.askforfriendmessage': {
            'Meta': {'ordering': "('ask_date',)", 'object_name': 'AskForFriendMessage'},
            'ask_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 24, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'received_messages'", 'to': u"orm['picwall.WebSiteUser']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_messages'", 'to': u"orm['picwall.WebSiteUser']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '10'})
        },
        u'picwall.photoinformation': {
            'Meta': {'object_name': 'PhotoInformation'},
            'height': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'photowall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.PhotoWall']"}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.Picture']"}),
            'top': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'picwall.photowall': {
            'Meta': {'object_name': 'PhotoWall'},
            'access_permission': ('django.db.models.fields.CharField', [], {'default': "'private'", 'max_length': '10'}),
            'access_times': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'access_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'access_pws'", 'symmetrical': 'False', 'to': u"orm['picwall.WebSiteUser']"}),
            'create_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 24, 0, 0)'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photowalls'", 'to': u"orm['picwall.WebSiteUser']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manage_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'manage_pws'", 'symmetrical': 'False', 'to': u"orm['picwall.WebSiteUser']"}),
            'modify_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 24, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'})
        },
        u'picwall.photowallcomment': {
            'Meta': {'ordering': "('published_date',)", 'object_name': 'PhotowallComment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.WebSiteUser']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 24, 0, 0)'}),
            'pw': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.PhotoWall']"})
        },
        u'picwall.picture': {
            'Meta': {'object_name': 'Picture'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.WebSiteUser']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'description'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'label_pics'", 'to': u"orm['picwall.PictureLabel']"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '32'}),
            'upload_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'picwall.picturecomment': {
            'Meta': {'ordering': "('published_date',)", 'object_name': 'PictureComment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.WebSiteUser']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.Picture']"}),
            'published_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 24, 0, 0)'})
        },
        u'picwall.picturelabel': {
            'Meta': {'object_name': 'PictureLabel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_labels'", 'to': u"orm['picwall.WebSiteUser']"})
        },
        u'picwall.websiteuser': {
            'Meta': {'object_name': 'WebSiteUser'},
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': u"orm['picwall.WebSiteUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'webuser'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['picwall']