from reports.models import CountryReport, Map, Section, MapPoint
from rest_framework import serializers
from django.contrib.auth.models import User


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class SectionSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Section
        fields = ('id', 'order', 'title', 'content', 'parent', 'children')


class CountryReportSerializer(serializers.ModelSerializer):
    section_set = serializers.SerializerMethodField('get_parent_sections')

    # This calls the sections serializer but filters it so that we only retrieve
    # sections that have no parents.
    def get_parent_sections(self, obj):
        parent_sections = Section.objects.get(parent=None, pk=obj.pk)
        serializer = SectionSerializer(parent_sections)
        return serializer.data

    class Meta:
        model = CountryReport
        fields = ('id', 'title', 'subtitle', 'section_set')


class MapPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPoint
        fields = ('id', 'map', 'title', 'description', 'long', 'lat',)


class MapSerializer(serializers.ModelSerializer):
    points = MapPointSerializer(many=True)

    class Meta:
        model = Map
        fields = ('id', 'title', 'long', 'lat', 'default_zoom', 'points')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)
