from django.db import models
from redactor.fields import RedactorField


class CountryReport(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{title}'.format(title=self.title)


class Map(models.Model):
    title = models.CharField(max_length=255)
    report = models.ForeignKey(CountryReport)
    long = models.DecimalField(max_digits=9,decimal_places=6)
    lat = models.DecimalField(max_digits=8,decimal_places=6)
    default_zoom = models.IntegerField()

    def __str__(self):
        return '{title}'.format(title=self.title)


class MapPoint(models.Model):
    map = models.ForeignKey(Map)
    title = models.CharField(max_length=255)
    description = models.TextField()
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=8, decimal_places=6)


class Section(models.Model):
    title = models.CharField(max_length=255)
    report = models.ForeignKey(CountryReport)
    order = models.PositiveIntegerField()
    section = models.ForeignKey('self', related_name='section_section', blank=True, null=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return '{title}'.format(title=self.title)
