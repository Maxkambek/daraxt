from django.contrib import admin
from .models import TreeClassifier, TypeTree, Region, District, TreeDeliveryCompany, Trade


class TreeClassifierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class TreeTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'classifier']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region']


class TreeDeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']


class TradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'contract_number']


admin.site.register(TreeClassifier, TreeClassifierAdmin)
admin.site.register(TypeTree, TreeTypeAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(TreeDeliveryCompany, TreeDeliveryAdmin)
admin.site.register(Trade, TradeAdmin)
