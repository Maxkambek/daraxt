from rest_framework import serializers
from .models import TreeReport, ReportImage


class ReportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportImage
        fields = ['id', 'image', 'report']


class ReportSerializer(serializers.ModelSerializer):
    reports_images = ReportImageSerializer(many=True)

    class Meta:
        model = TreeReport
        fields = [
            'id',
            'company_stir',
            'company_name',
            'owner_fio',
            'owner_jshshir',
            'contract_number',
            'description',
            'type_tree',
            'count_tree',
            'phone',
            'number_report',
            'district',
            'address',
            'created_at'
        ]
