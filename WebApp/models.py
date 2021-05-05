from django.db import models


# Create your models here.
class ItemsList(models.Model):
    itemname=models.CharField(max_length=100)
    ingredients=models.TextField()
    process=models.TextField()
    image = models.FileField(null='True', blank='True')



    def __str__(self):
        return self.itemname