from reports.models import CountryReport, Map, Section
from rest_framework import serializers


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


class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'map', 'title', 'description', 'long', 'lat',)

