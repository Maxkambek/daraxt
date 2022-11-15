from django.db import models


class TreeClassifier(models.Model):
    name = models.CharField(max_length=221)

    def __str__(self):
        return self.name


class TypeTree(models.Model):
    classifier = models.ForeignKey(TreeClassifier, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TreeDelivery(models.Model):
    name = models.CharField(max_length=221)
    address = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Trade(models.Model):
    type_tree = models.ForeignKey(TypeTree, on_delete=models.CASCADE)
    count_tree = models.PositiveIntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=221)
    contract_number = models.CharField(max_length=30)
    contract_date = models.CharField(max_length=20)
    contract_file = models.FileField(upload_to='contract_files/')
    delivery_company = models.ForeignKey(TreeDelivery, on_delete=models.CASCADE)

    def __str__(self):
        return self.contract_number