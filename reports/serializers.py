from reports.models import CountryReport, Maps, Section
from rest_framework import serializers


class CountryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryReport
        fields = ('id', 'title', 'subtitle')


class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maps
        fields = ('id', 'country', 'map_url', 'report')


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'title', 'report', 'order', 'section', 'content')
