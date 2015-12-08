from django.contrib.auth.models import User
from model_mommy import mommy
import pytest
from rest_framework import status
from reports.models import Country, Section, Map, CountryReport
from reports.views import CountryViewSet, UserView, MapViewSet, SectionViewSet, CountryReportViewSet

import pytest
from rest_framework.test import APIRequestFactory

@pytest.mark.django_db
def test_retrieve_country():
    request = APIRequestFactory().get("")
    view = CountryViewSet.as_view({'get': 'retrieve'})
    country = mommy.make(Country)
    response = view(request, pk=country.pk)

    assert status.HTTP_200_OK == response.status_code
    assert country.pk == response.data['id']

@pytest.mark.django_db
def test_list_country():
    request = APIRequestFactory().get("")
    view = CountryViewSet.as_view({'get': 'list'})
    country = mommy.make(Country)
    response = view(request)

    assert status.HTTP_200_OK == response.status_code

@pytest.mark.django_db
def test_retrieve_report():
    request = APIRequestFactory().get("")
    view = CountryReportViewSet.as_view({'get': 'retrieve'})
    country_report = mommy.make(CountryReport)
    response = view(request, pk=country_report.pk)

    assert status.HTTP_200_OK == response.status_code
    assert country_report.pk == response.data['id']

@pytest.mark.django_db
def test_list_report():
    request = APIRequestFactory().get("")
    view = CountryReportViewSet.as_view({'get': 'list'})
    country_report = mommy.make(CountryReport)
    response = view(request)

    assert status.HTTP_200_OK == response.status_code

@pytest.mark.django_db
def test_retrieve_section():
    request = APIRequestFactory().get("")
    view = SectionViewSet.as_view({'get': 'retrieve'})
    section = mommy.make(Section)
    response = view(request, pk=section.pk)

    assert status.HTTP_200_OK == response.status_code

@pytest.mark.django_db
def test_list_section():
    request = APIRequestFactory().get("")
    view = SectionViewSet.as_view({'get': 'list'})
    section = mommy.make(Section)
    response = view(request)

    assert status.HTTP_200_OK == response.status_code

@pytest.mark.django_db
def test_retrieve_map():
    request = APIRequestFactory().get("")
    view = MapViewSet.as_view({'get': 'retrieve'})
    map = mommy.make(Map)
    response = view(request, pk=map.pk)

    assert status.HTTP_200_OK == response.status_code
    assert map.pk == response.data['id']

@pytest.mark.django_db
def test_list_map():
    request = APIRequestFactory().get("")
    view = MapViewSet.as_view({'get': 'list'})
    map = mommy.make(Map)
    response = view(request)

    assert status.HTTP_200_OK == response.status_code

@pytest.mark.django_db
def test_list_user_not_allowed_as_guest():
    request = APIRequestFactory().get("")
    view = UserView.as_view({'get': 'list'})
    user = mommy.make(User)
    response = view(request)

    assert status.HTTP_403_FORBIDDEN == response.status_code

@pytest.mark.django_db
def test_retrieve_user_not_allowed_as_guest():
    request = APIRequestFactory().get("")
    view = UserView.as_view({'get': 'retrieve'})
    user = mommy.make(User)
    response = view(request, pk=user.pk)

    assert status.HTTP_403_FORBIDDEN == response.status_code