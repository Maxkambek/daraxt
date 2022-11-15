from django.db import models


class Contract(models.Model):
    number_contract = models.CharField(max_length=64)
    date_contract = models.CharField(max_length=20)
    number_akt = models.CharField(max_length=50)
    date_akt = models.CharField(max_length=20)
    company_stir = models.CharField(max_length=20)
    name_company = models.CharField(max_length=300)
    owner_jshshir = models.CharField(max_length=16)
    owner_fio = models.CharField(max_length=221)
    phone = models.CharField(max_length=15)
    number_report = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.number_contract

    class Meta:
        verbose_name = 'Contracts'
        verbose_name_plural = 'Contracts'


class ContractImage(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='contracts/')

    def __str__(self):
        return self.contract.number_contract


class ContractWithPartner(models.Model):
    number_contract = models.CharField(max_length=64)
    date_contract = models.CharField(max_length=20)
    number_akt = models.CharField(max_length=50)
    date_akt = models.CharField(max_length=20)
    company_stir = models.CharField(max_length=20)
    name_company = models.CharField(max_length=300)
    owner_jshshir = models.CharField(max_length=16)
    owner_fio = models.CharField(max_length=221)
    partner_stir = models.CharField(max_length=20)
    partner_name = models.CharField(max_length=221)
    partner_owner_jshshir = models.CharField(max_length=16)
    partner_fio = models.CharField(max_length=221)
    description = models.TextField()

    def __str__(self):
        return self.number_contract

    class Meta:
        verbose_name = 'ContractWithPartner'
        verbose_name_plural = 'ContractWithPartner'