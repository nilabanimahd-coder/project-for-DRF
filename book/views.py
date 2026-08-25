from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CategorySerializer,BookSerializer
from rest_framework import status
from .models import CategoryModel,BookModel
from django.shortcuts  import get_object_or_404

# Create your views here.

class CategoryListView(APIView):
    
    def get(self,request):
        categories=CategoryModel.objects.all()
        ser=CategorySerializer(categories,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)

    def post(self,request):
        ser=CategorySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        

class BookListView(APIView):

    def get(self,request):
        books=BookModel.objects.all()
        ser=BookSerializer(books,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        ser=BookSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response (ser.data,status=status.HTTP_201_CREATED)
        
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
        
    def get(self,request,pk):
        book=get_object_or_404(BookModel,id=pk)
        ser=BookSerializer(book)
        return Response(ser.data,status=status.HTTP_200_OK)
    
    def put (self,request,pk):
        book=get_object_or_404(BookModel,id=pk)
        ser=BookSerializer(book,data=request.data)
        if ser.is_valid() :
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch (self,request,pk):
        book=get_object_or_404(BookModel,id=pk)
        ser=BookSerializer(book,data=request.data,partial=True)
        if ser.is_valid() :
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        book=get_object_or_404(BookModel,id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
