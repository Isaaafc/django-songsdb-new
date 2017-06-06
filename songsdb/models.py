from __future__ import unicode_literals

from django.db import models

# Create your models here
class Author(models.Model):
    def __unicode__(self):
        return "%s"%self.author_name
    author_name = models.CharField(max_length=50)

class Publisher(models.Model):
    def __unicode__(self):
        return "%s"%self.publisher_name
    publisher_name = models.CharField(max_length=50)

class Type(models.Model):
    def __unicode__(self):
        return "%s"%self.desc
    desc = models.CharField(max_length=50)

class Song(models.Model):
    def __unicode__(self):
        return "%s"%self.song_name
    song_name = models.CharField(max_length=50)
    document_link = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    author = models.ForeignKey(Author)
    publisher = models.ForeignKey(Publisher)
    song_type = models.ForeignKey(Type)

class WTime(models.Model):
    def __unicode__(self):
        return "%s"%self.user_id
    user_id = models.IntegerField()
    time_stamp = models.DateTimeField()
    online = models.BooleanField()
