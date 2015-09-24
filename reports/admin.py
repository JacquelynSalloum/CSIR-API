from django.contrib import admin
from reports.models import CountryReport

class CountryReportAdmin(admin.ModelAdmin):
    model = CountryReport
    
    
admin.site.register(CountryReport)
