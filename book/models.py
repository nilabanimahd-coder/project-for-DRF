from django.db import models
from django.contrib.auth.models import User

"""
admins
nila password:nil@1383
ali password:123456
reza password:rez@1388


"""

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    stock = models.IntegerField(default=5)
    category = models.ForeignKey( CategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
