# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AskForFriendMessage'
        db.delete_table(u'picwall_askforfriendmessage')

        # Deleting model 'PhotoWall'
        db.delete_table(u'picwall_photowall')

        # Removing M2M table for field manage_users on 'PhotoWall'
        db.delete_table(db.shorten_name(u'picwall_photowall_manage_users'))

        # Removing M2M table for field access_users on 'PhotoWall'
        db.delete_table(db.shorten_name(u'picwall_photowall_access_users'))

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

        # Deleting model 'WebSiteUser'
        db.delete_table(u'picwall_websiteuser')

        # Removing M2M table for field friends on 'WebSiteUser'
        db.delete_table(db.shorten_name(u'picwall_websiteuser_friends'))


    def backwards(self, orm):
        # Adding model 'AskForFriendMessage'
        db.create_table(u'picwall_askforfriendmessage', (
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sent_messages', to=orm['picwall.WebSiteUser'])),
            ('ask_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 23, 0, 0))),
            ('state', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=10)),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='received_messages', to=orm['picwall.WebSiteUser'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'picwall', ['AskForFriendMessage'])

        # Adding model 'PhotoWall'
        db.create_table(u'picwall_photowall', (
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=256)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photowalls', to=orm['picwall.WebSiteUser'])),
            ('access_permission', self.gf('django.db.models.fields.CharField')(default='private', max_length=10)),
            ('create_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 23, 0, 0))),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=32)),
            ('modify_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 23, 0, 0))),
            ('access_times', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'picwall', ['PhotoWall'])

        # Adding M2M table for field manage_users on 'PhotoWall'
        m2m_table_name = db.shorten_name(u'picwall_photowall_manage_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowall', models.ForeignKey(orm[u'picwall.photowall'], null=False)),
            ('websiteuser', models.ForeignKey(orm[u'picwall.websiteuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photowall_id', 'websiteuser_id'])

        # Adding M2M table for field access_users on 'PhotoWall'
        m2m_table_name = db.shorten_name(u'picwall_photowall_access_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowall', models.ForeignKey(orm[u'picwall.photowall'], null=False)),
            ('websiteuser', models.ForeignKey(orm[u'picwall.websiteuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photowall_id', 'websiteuser_id'])

        # Adding model 'PictureComment'
        db.create_table(u'picwall_picturecomment', (
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.WebSiteUser'])),
            ('pic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.Picture'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('published_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 23, 0, 0))),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'picwall', ['PictureComment'])

        # Adding model 'PhotoInformation'
        db.create_table(u'picwall_photoinformation', (
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.Picture'])),
            ('width', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('photowall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.PhotoWall'])),
            ('top', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('left', self.gf('django.db.models.fields.CharField')(max_length=16)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'picwall', ['PhotoInformation'])

        # Adding model 'PictureLabel'
        db.create_table(u'picwall_picturelabel', (
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_labels', to=orm['picwall.WebSiteUser'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'picwall', ['PictureLabel'])

        # Adding model 'Picture'
        db.create_table(u'picwall_picture', (
            ('upload_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(default='description', max_length=64)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.WebSiteUser'])),
            ('label', self.gf('django.db.models.fields.related.ForeignKey')(related_name='label_pics', to=orm['picwall.PictureLabel'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='name', max_length=32)),
        ))
        db.send_create_signal(u'picwall', ['Picture'])

        # Adding model 'PhotowallComment'
        db.create_table(u'picwall_photowallcomment', (
            ('pw', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.PhotoWall'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.WebSiteUser'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('published_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 23, 0, 0))),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'picwall', ['PhotowallComment'])

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


    models = {
        
    }

    complete_apps = ['picwall']