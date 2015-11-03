from rest_condition import Or
from rest_framework import viewsets
from ChildSoldier.utils import get_guest_permissions_class
from rest_framework.generics import ListAPIView, RetrieveAPIView
from reports.models import Map, Section, CountryReport, MapPoint, Country
from rest_framework.permissions import IsAuthenticated
from reports.serializers import (MapSerializer, SectionSerializer, CountryReportSerializer, UserSerializer,
                                 MapPointSerializer, CountrySerializer)
from django.contrib.auth.models import User


class CountryReportViewSet(viewsets.ModelViewSet):
    permission_classes = (Or(IsAuthenticated, get_guest_permissions_class(['list', 'retrieve'])), )
    queryset = CountryReport.objects.all()
    serializer_class = CountryReportSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = (Or(IsAuthenticated, get_guest_permissions_class(['list', 'retrieve'])),)
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class MapViewSet(viewsets.ModelViewSet):
    permission_classes = (Or(IsAuthenticated, get_guest_permissions_class(['list', 'retrieve'])), )
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class MapPointViewSet(viewsets.ModelViewSet):
    permission_classes = (Or(IsAuthenticated, get_guest_permissions_class(['list', 'retrieve'])),)
    queryset = MapPoint.objects.all()
    serializer_class = MapPointSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.filter(parent=None)
    permission_classes = (Or(IsAuthenticated, get_guest_permissions_class(['list', 'retrieve'])), )
    serializer_class = SectionSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
