# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)
user_model_label = '%s.%s' % (User._meta.app_label, User._meta.module_name)
user_ptr_name = '%s_ptr' % User._meta.object_name.lower()

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SubscriptionSettings.user'
        db.alter_column(u'mass_post_office_subscriptionsettings', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm[user_orm_label], unique=True))
        # Adding unique constraint on 'SubscriptionSettings', fields ['user']
        db.create_unique(u'mass_post_office_subscriptionsettings', ['user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'SubscriptionSettings', fields ['user']
        db.delete_unique(u'mass_post_office_subscriptionsettings', ['user_id'])


        # Changing field 'SubscriptionSettings.user'
        db.alter_column(u'mass_post_office_subscriptionsettings', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[user_orm_label]))

    models = {
        user_model_label: {
        },
        u'mass_post_office.mailinglist': {
            'Meta': {'object_name': 'MailingList'},
            'additional_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['%s']" % user_orm_label, 'null': 'True', 'symmetrical': 'False'}),
            'all_users': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'or_list': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'user_should_be_agree': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'mass_post_office.subscriptionsettings': {
            'Meta': {'object_name': 'SubscriptionSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subscribed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['%s']" % user_orm_label, 'unique': 'True'})
        }
    }

    complete_apps = ['mass_post_office']