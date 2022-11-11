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


class Trade(models.Model):
    type_tree = models.ForeignKey(TypeTree, on_delete=models.CASCADE)
    count_tree = models.PositiveIntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=221)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.phone


class TradeImage(models.Model):
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trades/')

    def __str__(self):
        return self.trade.phone


