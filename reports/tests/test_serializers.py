import pytest
import reports.serializers
from model_mommy import mommy
from ChildSoldier.utils import dict_from_attrs, dict_with_keys


@pytest.mark.django_db
def test_country_serialization():
    country = mommy.make('reports.country')
    serializer = reports.serializers.CountrySerializer(country)
    serialized_data = serializer.data

    fields = ['id', 'name', ]

    assert dict_from_attrs(country, fields) == dict_with_keys(serialized_data, fields)


@pytest.mark.django_db
def test_section_serialization():
    section = mommy.make('reports.section')
    serializer = reports.serializers.SectionSerializer(section)
    serialized_data = serializer.data

    fields = ['id', 'title', 'order', 'content', ]

    assert dict_from_attrs(section, fields) == dict_with_keys(serialized_data, fields)


@pytest.mark.django_db
def test_map_point_serialization():

    # long and lat are hardcoded because the decimal field from model-mommy doen't work. Something like strings...
    map_point = mommy.make('reports.mapPoint', long='111.111111', lat='222.222222')
    serializer = reports.serializers.MapPointSerializer(map_point)
    serialized_data = serializer.data

    # map is a map object, tested below
    # fields = ['id', 'map', 'title', 'description', 'long', 'lat', ]
    fields = ['id', 'title', 'description', 'long', 'lat', ]

    assert dict_from_attrs(map_point, fields) == dict_with_keys(serialized_data, fields)


@pytest.mark.django_db
def test_map_serialization():

    # long and lat are hardcoded because the decimal field from model-mommy doen't work. Something like strings...
    map = mommy.make('reports.map', long='111.111111', lat='222.222222', default_zoom=1)
    serializer = reports.serializers.MapSerializer(map)
    serialized_data = serializer.data
    fields = ['id', 'title', 'long', 'lat', 'default_zoom', ]

    assert dict_from_attrs(map, fields) == dict_with_keys(serialized_data, fields)


@pytest.mark.django_db
def test_country_report_retrieve_serialization():
    country_report_retrieve = mommy.make('reports.countryReport',)
    serializer = reports.serializers.CountryReportRetrieveSerializer(country_report_retrieve)
    serialized_data = serializer.data

    # country will be the country_id, not the country name
    # fields = ['id', 'country', 'title', 'subtitle', 'section_set', 'maps',]
    fields = ['id', 'title', 'subtitle', ]

    assert dict_from_attrs(country_report_retrieve, fields) == dict_with_keys(serialized_data, fields)


@pytest.mark.django_db
def test_country_report_serialization():
    country_report = mommy.make('reports.countryReport')
    serializer = reports.serializers.CountryReportSerializer(country_report)
    serialized_data = serializer.data

    # Country is a country object, tested elsewhere
    # fields = ['id', 'country', 'title', 'subtitle', ]
    fields = ['id', 'title', 'subtitle', ]

    assert dict_from_attrs(country_report, fields) == dict_with_keys(serialized_data, fields)


@pytest.mark.django_db
def test_user_serialization():
    user = mommy.make('auth.user')
    serializer = reports.serializers.UserSerializer(user)
    serialized_data = serializer.data

    fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']

    assert dict_from_attrs(user, fields) == dict_with_keys(serialized_data, fields)
