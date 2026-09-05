from rest_framework import serializers
from .models import BorrowingModel
from rest_framework.pagination import PageNumberPagination

class BorrowingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=BorrowingModel
        fields="__all__"

class MyPagination(PageNumberPagination):
    page_size = 2