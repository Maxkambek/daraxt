from django.db import models
from trades.models import TypeTree, District


class TreeReport(models.Model):
    company_stir = models.CharField(max_length=20)
    company_name = models.CharField(max_length=221)
    owner_fio = models.CharField(max_length=221)
    owner_jshshir = models.CharField(max_length=16)
    contract_number = models.CharField(max_length=22)
    description = models.TextField()
    type_tree = models.ForeignKey(TypeTree, on_delete=models.CASCADE)
    count_tree = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    number_report = models.CharField(max_length=20)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.company_name


class ReportImage(models.Model):
    report = models.ForeignKey(TreeReport, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reports/')

    def __str__(self):
        return self.report.company_name
