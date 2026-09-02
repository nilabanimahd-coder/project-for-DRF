from rest_framework import serializers
from .models import BorrowingModel

class BorrowingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=BorrowingModel
        fields="__all__"

