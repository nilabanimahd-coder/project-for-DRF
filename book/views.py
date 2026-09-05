from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CategorySerializer,BookSerializer
from rest_framework import status
from .models import CategoryModel,BookModel
from django.shortcuts  import get_object_or_404
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permission import IsOwnerOrAdmin,IsAdminOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken,BlacklistedToken
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
    authentication_classes=[SessionAuthentication,JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get(self,request):
        books=BookModel.objects.all()
        ser=BookSerializer(books,many=True,context={"request": request})
        return Response(ser.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        ser=BookSerializer(data=request.data)
        if ser.is_valid():
            ser.save(owner=request.user)
            return Response (ser.data,status=status.HTTP_201_CREATED)
        
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    authentication_classes=[SessionAuthentication,TokenAuthentication]
    permission_classes=[IsOwnerOrAdmin]

    def get(self,request,pk):
        book=get_object_or_404(BookModel,id=pk)
        self.check_object_permissions(self.request,book)
        ser=BookSerializer(book)
        return Response(ser.data,status=status.HTTP_200_OK)
    
    def put (self,request,pk):
        book=get_object_or_404(BookModel,id=pk)
        self.check_object_permissions(self.request,book)
        ser=BookSerializer(book,data=request.data)
        if ser.is_valid() :
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch (self,request,pk):
        book=get_object_or_404(BookModel,id=pk)
        self.check_object_permissions(self.request,book)
        ser=BookSerializer(book,data=request.data,partial=True)
        if ser.is_valid() :
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        book=get_object_or_404(BookModel,id=pk)
        self.check_object_permissions(self.request,book)
        book.delete()
        return Response({'massage':'book delete'},status=status.HTTP_204_NO_CONTENT)
    
class LogoutApiview(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        user=request.user
        tokens=OutstandingToken.objects.filter(user=user)

        for token in tokens:
            try:
                BlacklistedToken.objects.get_or_create(token=token)
            except Exception:
                pass

        return Response({"massage":"logout success"}, status=status.HTTP_205_RESET_CONTENT)
        
