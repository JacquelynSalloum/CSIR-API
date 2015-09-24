from django.db import models
from django.db.models import ImageField


class CountryReport(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Maps(models.Model):
    country = models.CharField(max_length=255) # TODO: Countries enum limit
    map_url = models.CharField(max_length=255)
    report = models.ForeignKey(CountryReport)


class Section(models.Model):
    title = models.CharField(max_length=255)
    report = models.ForeignKey(CountryReport)
    section = models.ForeignKey('self', related_name='section_section', blank=True, null=True)


class Content(models.Model):
    text = models.TextField()
    section = models.ForeignKey(Section, related_name='content_section')


class Table(models.Model):
    section = models.ForeignKey(Section, related_name='table_section')


class Row(models.Model):
    table = models.ForeignKey(Table, related_name='row_table')
    label = models.CharField(max_length=255)


class Column(models.Model):
    table = models.ForeignKey(Table, related_name='column_table')
    label = models.CharField(max_length=255)


class TableItem(models.Model):
    row = models.ForeignKey(Row)
    column = models.ForeignKey(Column)


class TextTableItem(TableItem):
    text = models.CharField(max_length=255)


class ImageTableItem(TableItem):
    image_url = models.CharField(max_length=255)
