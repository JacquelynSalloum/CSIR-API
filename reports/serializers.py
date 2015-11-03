from reports.models import CountryReport, Map, Section
from rest_framework import serializers
from django.contrib.auth.models import User


class CountryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryReport
        fields = ('id', 'title', 'subtitle')
        owner = serializers.ReadOnlyField(source='owner.username')


class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'country', 'map_url', 'report')


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'title', 'report', 'order', 'section', 'content')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',)