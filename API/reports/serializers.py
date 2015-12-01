from reports.models import CountryReport, Map, Section, MapPoint, Country
from rest_framework import serializers
from django.contrib.auth.models import User


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name',)


class SectionSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Section
        fields = ('id', 'order', 'report', 'title', 'content', 'children',)


class MapPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPoint
        fields = ('id', 'map', 'title', 'description', 'long', 'lat',)


class MapSerializer(serializers.ModelSerializer):
    points = MapPointSerializer(many=True)

    class Meta:
        model = Map
        fields = ('id', 'title', 'long', 'lat', 'default_zoom', 'points',)


class CountryReportRetrieveSerializer(serializers.ModelSerializer):
    section_set = serializers.SerializerMethodField('get_parent_sections')
    maps = MapSerializer(many=True)

    # This calls the sections serializer but filters it so that we only retrieve
    # sections that have no parents and belong to the given report.
    def get_parent_sections(self, obj):
        parent_sections = Section.objects.filter(parent=None, report=obj).order_by('order')
        serializer = SectionSerializer(parent_sections, many=True)
        return serializer.data

    class Meta:
        model = CountryReport
        fields = ('id', 'country', 'title', 'subtitle', 'section_set', 'maps',)


class CountryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryReport
        fields = ('id', 'country', 'title', 'subtitle',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email',)
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
