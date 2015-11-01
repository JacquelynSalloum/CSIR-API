from django import forms
from django.contrib import admin
from redactor.widgets import RedactorEditor
from reports.models import CountryReport, Map, Section


class SectionAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        widgets = {
            'content': RedactorEditor(),
        }


class SectionAdmin(admin.StackedInline):
    form = SectionAdminForm
    model = Section


class CountryReportAdmin(admin.ModelAdmin):
    model = CountryReport
    inlines = [SectionAdmin]


class MapAdmin(admin.ModelAdmin):
    model = Map

admin.site.register(CountryReport, CountryReportAdmin)
admin.site.register(Map, MapAdmin)
