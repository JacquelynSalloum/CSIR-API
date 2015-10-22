import pytest
from reports.serializers import SectionSerializer
from model_mommy import mommy
from ChildSoldier.utils import dict_from_attrs, dict_with_keys


@pytest.mark.django_db
def test_series_serialization():
    section = mommy.make('reports.section')
    serializer = SectionSerializer(section)
    serialized_data = serializer.data

    fields = ['id', 'title', 'order', 'content']

    assert dict_from_attrs(section, fields) == dict_with_keys(serialized_data, fields)
