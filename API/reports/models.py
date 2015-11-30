from django.db import models


class Country(models.Model):
    # = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{name}'.format(name=self.name)


class CountryReport(models.Model):
    country = models.ForeignKey(Country)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{title}'.format(title=self.title)


class Map(models.Model):
    title = models.CharField(max_length=255)
    report = models.ForeignKey(CountryReport, related_name='maps')
    long = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='longitude')
    lat = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='latitude')
    default_zoom = models.IntegerField()

    def __str__(self):
        return '{title}'.format(title=self.title)


class MapPoint(models.Model):
    map = models.ForeignKey(Map, related_name='points')
    title = models.CharField(max_length=255)
    description = models.TextField()
    long = models.DecimalField(max_digits=10, decimal_places=6)
    lat = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return '{title}'.format(title=self.title)


class Section(models.Model):
    title = models.CharField(max_length=255)
    report = models.ForeignKey(CountryReport)
    order = models.PositiveIntegerField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    content = models.TextField(blank=True)

    def __str__(self):
        return '{title}'.format(title=self.title)
