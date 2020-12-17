from django.db import models


# Create your models here.
class Brand(models.Model):
    name          = models.CharField(max_length=50)
    created_at    = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name          = models.CharField(max_length=50)
    price         = models.IntegerField()
    description   = models.TextField()
    new           = models.BooleanField()
    image         = models.ImageField(upload_to='productos', null=True)
    brand         = models.ForeignKey(Brand, on_delete=models.PROTECT)
    fabr_date     = models.DateField()
    created_at    = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

