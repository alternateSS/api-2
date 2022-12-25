from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    label = models.CharField(max_length=40)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.category}'


class Label(models.Model):
    name = models.CharField(max_length=40)
    office_address = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name} - {self.office_adress}'


class Category(models.Model):
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.category_name}'