from rest_framework import serializers
from .models import CategoryModel,BookModel

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CategoryModel
        fields='__all__'


class MaxPriceValidator:

    def __init__(self,max_price):
        self.max_price=max_price

    def __call__(self, value):
        if value > self.max_price:
            raise serializers.ValidationError("price is too high")
        
        return value
class minpricevalidator:

    def __init__(self,min_price):
        self.min_price=min_price
    
    def __call__(self, value):
        if value < self.min_price:
            raise serializers.ValidationError("priced not be negetive")
        
        return value

    
class BookSerializer(serializers.ModelSerializer):
    
    price_with_tax=serializers.SerializerMethodField()

    def get_price_with_tax(self,obj):
        return obj.price*1.1
    

    price =serializers.IntegerField(validators=[minpricevalidator(0),MaxPriceValidator(10000)])
    category=serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all())
    owner=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=BookModel
        fields=['id','owner','title','author','stock','price','price_with_tax','category']
        read_only_fields=['stock','owner']

