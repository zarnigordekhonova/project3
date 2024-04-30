from django.db import models

# Create your models here.

class customer_info1(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    adress = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.name} {self.surname}'


class customer_info2(models.Model):
    size = models.IntegerField()
    length_clothe = models.IntegerField
    color = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.size} {self.color}'
