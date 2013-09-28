from django.db import models
from django.db.models.signals import post_save

from core.lists import INSTRUMENT_CHOICES, STYLE_CHOICES
from users.models import User

class MusicProfile(models.Model):
    user = models.OneToOneField(User)

    instruments = models.CommaSeparatedIntegerField(max_length=10, choices=INSTRUMENT_CHOICES, default=None, null=True)

    skill_rating = models.IntegerField(default=0)

    styles = models.CommaSeparatedIntegerField(max_length=10, choices=STYLE_CHOICES, default=None, null=True)

    zipcode = models.CharField(blank=True, null=True, max_length=16)

    def __unicode__(self):
        return u'%s\'s profile' % (self.user.username,)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MusicProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User, dispatch_uid="users-profilecreation-signal")


class Instrument(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return u'Instrument: %s' % (self.name,)


class Influence(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return u'Influence: %s' % (self.name,)


class UserInfluence(models.Model):
    user = models.ForeignKey(User, related_name='user_influence')
    influence = models.ForeignKey(Influence, related_name='influence_set')

    def __unicode__(self):
        return u'%s influence: %s' % (self.user.username, self.influence.name,)


class UserInstrument(models.Model):
    user = models.ForeignKey(User, related_name='user_instrument')
    instrument = models.ForeignKey(Instrument, related_name='instrument_set')
    skill_level = models.DecimalField(max_digits=3,decimal_places=2)

    def __unicode__(self):
        return u'%s plays: %s' % (self.user.username, self.instrument.name,)


class UserRating(models.Model):
    rater = models.ForeignKey(User, related_name='ratings_set')
    user = models.ForeignKey(User, related_name='user_rating')
    score = models.DecimalField(max_digits=3, decimal_places=2)

    def __unicode__(self):
        return u'%s rates %s as %f' % (self.rater.username, self.user.username, self.score)

