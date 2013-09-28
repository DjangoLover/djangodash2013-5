# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MusicProfile'
        db.create_table(u'music_musicprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.User'], unique=True)),
            ('instruments', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(default=None, max_length=10, null=True)),
            ('skill_rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('styles', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(default=None, max_length=10, null=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
        ))
        db.send_create_signal(u'music', ['MusicProfile'])

        # Adding model 'Instrument'
        db.create_table(u'music_instrument', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'music', ['Instrument'])

        # Adding model 'Influence'
        db.create_table(u'music_influence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'music', ['Influence'])

        # Adding model 'UserInfluence'
        db.create_table(u'music_userinfluence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_influence', to=orm['users.User'])),
            ('influence', self.gf('django.db.models.fields.related.ForeignKey')(related_name='influence_set', to=orm['music.Influence'])),
        ))
        db.send_create_signal(u'music', ['UserInfluence'])

        # Adding model 'UserInstrument'
        db.create_table(u'music_userinstrument', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_instrument', to=orm['users.User'])),
            ('instrument', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instrument_set', to=orm['music.Instrument'])),
            ('skill_level', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal(u'music', ['UserInstrument'])

        # Adding model 'UserRating'
        db.create_table(u'music_userrating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rater', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratings_set', to=orm['users.User'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_rating', to=orm['users.User'])),
            ('score', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal(u'music', ['UserRating'])


    def backwards(self, orm):
        # Deleting model 'MusicProfile'
        db.delete_table(u'music_musicprofile')

        # Deleting model 'Instrument'
        db.delete_table(u'music_instrument')

        # Deleting model 'Influence'
        db.delete_table(u'music_influence')

        # Deleting model 'UserInfluence'
        db.delete_table(u'music_userinfluence')

        # Deleting model 'UserInstrument'
        db.delete_table(u'music_userinstrument')

        # Deleting model 'UserRating'
        db.delete_table(u'music_userrating')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'music.influence': {
            'Meta': {'object_name': 'Influence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'music.instrument': {
            'Meta': {'object_name': 'Instrument'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'music.musicprofile': {
            'Meta': {'object_name': 'MusicProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruments': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'default': 'None', 'max_length': '10', 'null': 'True'}),
            'skill_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'styles': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'default': 'None', 'max_length': '10', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.User']", 'unique': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'})
        },
        u'music.userinfluence': {
            'Meta': {'object_name': 'UserInfluence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'influence': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'influence_set'", 'to': u"orm['music.Influence']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_influence'", 'to': u"orm['users.User']"})
        },
        u'music.userinstrument': {
            'Meta': {'object_name': 'UserInstrument'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrument': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instrument_set'", 'to': u"orm['music.Instrument']"}),
            'skill_level': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_instrument'", 'to': u"orm['users.User']"})
        },
        u'music.userrating': {
            'Meta': {'object_name': 'UserRating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rater': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings_set'", 'to': u"orm['users.User']"}),
            'score': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_rating'", 'to': u"orm['users.User']"})
        },
        u'users.user': {
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
        }
    }

    complete_apps = ['music']