from django.contrib import admin
from .models import TreeReport


class TreeReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'company_stir']


admin.site.register(TreeReport, TreeReportAdmin)
