from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class Division(models.Model):
    name = models.CharField(max_length=30)
    bn_name = models.CharField(max_length=50)
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        managed = True
        db_table = 'bd_geoinfo_division'


class District(models.Model):
    division = models.ForeignKey('Division')
    name = models.CharField(max_length=30)
    bn_name = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    website = models.CharField(max_length=100)
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        managed = True
        db_table = 'bd_geoinfo_district'


class CityArea(models.Model):
    district = models.ForeignKey(District)
    name = models.CharField(max_length=30)
    bn_name = models.CharField(max_length=50)
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        managed = True
        db_table = 'bd_geoinfo_cityarea'


class Upazila(models.Model):
    district = models.ForeignKey(District)
    name = models.CharField(max_length=30)
    bn_name = models.CharField(max_length=50)
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        managed = True
        db_table = 'bd_geoinfo_upazila'


class Union(models.Model):
    upazila = models.ForeignKey('Upazila')
    name = models.CharField(max_length=30)
    bn_name = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        managed = True
        db_table = 'bd_geoinfo_union'
