from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from reports.models import Map, Section, CountryReport
from reports.serializers import MapsSerializer, SectionSerializer, CountryReportSerializer
from django.contrib.auth.models import User
from serializers import UserSerializer

class CountryReportViewSet(viewsets.ModelViewSet):
    queryset = CountryReport.objects.all()
    serializer_class = CountryReportSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MapsViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapsSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer