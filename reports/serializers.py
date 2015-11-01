from reports.models import CountryReport, Map, Section
from rest_framework import serializers


class CountryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryReport
        fields = ('id', 'title', 'subtitle')


class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'country', 'map_image', 'report')


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'title', 'report', 'order', 'section', 'content')
