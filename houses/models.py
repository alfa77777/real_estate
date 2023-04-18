from django.conf import settings
from django.db import models


class House(models.Model):
    address = models.CharField(max_length=255, null=False)
    target = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="houses")
    amount_of_rooms = models.PositiveSmallIntegerField()
    price = models.FloatField()
    square_footage_meter = models.FloatField()
    builded_year = models.PositiveSmallIntegerField()
    updated_year = models.PositiveSmallIntegerField()
    owner = models.ForeignKey("Owner", on_delete=models.CASCADE, related_name='houses')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name="houses")
    image = models.ImageField()
    extra_info = models.TextField(default="")


class Category(models.Model):
    name = models.CharField(max_length=100)


class Owner(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


class Country(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
