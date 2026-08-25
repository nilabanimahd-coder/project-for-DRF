from rest_framework import serializers
from .models import CategoryModel,BookModel

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CategoryModel
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=BookModel
        fields='__all__'
    