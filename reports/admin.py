from django.contrib import admin
from reports.models import CountryReport, Map, Section


class CountryReportAdmin(admin.ModelAdmin):
    model = CountryReport

class SectionAdmin(admin.ModelAdmin):
    model = Section

class MapsAdmin(admin.ModelAdmin):
    model = Map

admin.site.register(CountryReport)
admin.site.register(Map)
admin.site.register(Section)
