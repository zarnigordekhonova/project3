from django.db import models

# Create your models here.

class orders1(models.Model):
    size = models.IntegerField()
    color = models.CharField(max_length=255)
    type_clothe = models.CharField(max_length=255)
    price = models.IntegerField()


    def __str__(self):
        return f'{self.size} {self.color}'


class orders2(models.Model):
    payment_type = models.CharField(max_length=255)
    delivery_type = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.payment_type} {self.delivery_type}'
