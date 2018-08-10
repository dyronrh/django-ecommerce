from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    desciption = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=5, decimal_places=4, default=0.00000)
    cant = models.IntegerField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title