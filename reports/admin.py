from django import forms
from django.contrib import admin
from redactor.widgets import RedactorEditor
from reports.models import CountryReport, Map, Section


class CountryReportAdmin(admin.ModelAdmin):
    model = CountryReport


class SectionAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        widgets = {
            'content': RedactorEditor(),
        }


class SectionAdmin(admin.ModelAdmin):
    form = SectionAdminForm


class MapAdmin(admin.ModelAdmin):
    model = Map

admin.site.register(CountryReport, CountryReportAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(Section, SectionAdmin)
