from django.db import models


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


req_opt = [
    [0, 'consulta'],
    [1, 'reclamo'],
    [2, 'sugerencia'],
    [3, 'felicitaciones'],
]


class Contact(models.Model):
    name     = models.CharField(max_length=50)
    email    = models.EmailField()
    subject  = models.IntegerField(choices=req_opt)
    message  = models.TextField()
    advice   = models.BooleanField()

    def __str__(self):
        return self.name
