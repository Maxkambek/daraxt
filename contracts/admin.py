from django.contrib import admin
from .models import Contract, ContractWithPartner, ContractImage


class ContractInline(admin.TabularInline):
    model = ContractImage
    extra = 0


class ContractAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_contract', 'number_akt']
    inlines = [ContractInline]


class ContractWithPartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_contract', 'partner_name']


admin.site.register(Contract, ContractAdmin)
admin.site.register(ContractWithPartner, ContractWithPartnerAdmin)
