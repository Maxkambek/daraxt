from rest_framework import serializers
from .models import Contract, ContractImage, ContractWithPartner


class ContractImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractImage
        fields = ['id', 'image', 'contract']


class ContractSerializer(serializers.ModelSerializer):
    contracts_images = ContractImageSerializer(many=True)

    class Meta:
        model = Contract
        fields = [
            'id',
            'status',
            'number_contract',
            'date_contract',
            'number_akt',
            'date_akt',
            'company_stir',
            'name_company',
            'owner_jshshir',
            'owner_fio',
            'phone',
            'number_report',
            'description',
            'created_at',
            'contracts_images'
        ]


class ContractSerializerReport(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'id',
            'number_contract',
            'date_contract',
            'name_company',
            'created_at'
            'status',
        ]


class ContractWithPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractWithPartner
        fields = [
            'id',
            'status',
            'number_contract',
            'date_contract',
            'number_akt',
            'date_akt',
            'company_stir',
            'name_company',
            'owner_jshshir',
            'owner_fio',
            'partner_stir',
            'partner_name',
            'partner_owner_jshshir',
            'partner_fio',
            'description',
            'created_at'
        ]


class ContractWithPartnerSerializerReport(serializers.ModelSerializer):
    class Meta:
        model = ContractWithPartner
        fields = [
            'id',
            'status',
            'number_contract',
            'date_contract',
            'name_company',
            'partner_name',
            'created_at'
        ]
