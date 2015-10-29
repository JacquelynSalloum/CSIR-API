from rest_framework import viewsets
from reports.models import Map, Section, CountryReport
from reports.serializers import MapsSerializer, SectionSerializer, CountryReportSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class CountryReportViewSet(viewsets.ModelViewSet):
    permission_classes = (Or(IsAuthenticated, get_guest_permissions_class(['list', 'retrieve'])), )
    queryset = CountryReport.objects.all()
    serializer_class = CountryReportSerializer


class MapsViewSet(viewsets.ModelViewSet):
    permission_classes = (Or(IsAuthenticated, get_guest_permissions_class(['list', 'retrieve'])), )
    queryset = Map.objects.all()
    serializer_class = MapsSerializer


class SectionViewSet(viewsets.ModelViewSet):
    permission_classes = (Or(IsAuthenticated, get_guest_permissions_class(['list', 'retrieve'])), )
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

