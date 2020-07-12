from datetime import date
from django.db import models


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    is_seller_of_the_month = models.BooleanField(default=False)
    hire_date = models.DateField(default=date.today)

    def __str__(self):
        return self.name
