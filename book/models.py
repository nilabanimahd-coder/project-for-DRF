from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.ForeignKey( CategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
