from reports.models import CountryReport, Maps, Section
from rest_framework import serializers

class CountryReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CountryReport
        fields = ('title', 'subtitle', 'created_at', 'updated_at')

class MapsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maps
        fields = ('country', 'map_url', 'report')

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('title', 'report', 'order', 'section', 'content')
