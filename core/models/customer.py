"""Customer model"""
from django.db import models


class Gender(models.TextChoices):
    Male = "Male"
    Female = "Female"

    @classmethod
    def has_value(cls, value):
        return value in cls.values


class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)

    gender = models.CharField(choices=Gender.choices, max_length=6, null=False, blank=False)

    company = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)

    title = models.CharField(max_length=50, blank=False, null=False)

    lng = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Customer: '{self.first_name, self.last_name}'"