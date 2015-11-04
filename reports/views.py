from rest_condition import Or
from rest_framework import viewsets
from rest_framework.response import Response
from ChildSoldier.utils import get_guest_permissions_class, IsStaffOrTargetUser
from rest_framework.generics import get_object_or_404
from reports.models import Map, Section, CountryReport, MapPoint, Country
from rest_framework.permissions import IsAuthenticated, AllowAny
from reports.serializers import (MapSerializer, SectionSerializer, CountryReportSerializer, UserSerializer,
                                 MapPointSerializer, CountrySerializer, CountryReportRetrieveSerializer)
from django.contrib.auth.models import User


class CountryReportViewSet(viewsets.ModelViewSet):
    permission_classes = (Or(IsAuthenticated, get_guest_permissions_class(['list', 'retrieve'])), )
    serializer_class = CountryReportSerializer
    queryset = CountryReport.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = CountryReport.objects.all()
        serializer = CountryReportSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = CountryReport.objects.all()
        countryreport = get_object_or_404(queryset, pk=pk)
        serializer = CountryReportRetrieveSerializer(countryreport)
        return Response(serializer.data)


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


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),
