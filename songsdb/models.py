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
    document_link2 = models.CharField(max_length=200, null=True, blank=True)
    document_link3 = models.CharField(max_length=200, null=True, blank=True)
    media_link = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=3, null=True, blank=True)
    year = models.SmallIntegerField()
    author = models.ForeignKey(Author)
    publisher = models.ForeignKey(Publisher)
    song_type = models.ForeignKey(Type)


class WTime(models.Model):
    user_id = models.IntegerField()
    time_stamp = models.DateTimeField()
    online = models.BooleanField()
