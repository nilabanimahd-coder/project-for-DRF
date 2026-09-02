"""from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import BorrowingSerializer
from .models import BorrowingModel
# Create your views here.

#create,list
class BorrowingView(ListCreateAPIView):
    queryset=BorrowingModel.objects.all()
    serializer_class=BorrowingSerializer

#retieve,update,destroy
class BorrowingUpadateView(RetrieveUpdateDestroyAPIView):
    queryset=BorrowingModel.objects.all()
    serializer_class=BorrowingSerializer"""

from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import BorrowingModel
from .serializers import BorrowingSerializer

class BorrowingView(
    ListModelMixin,
    CreateModelMixin,
    GenericAPIView
):
    queryset=BorrowingModel.objects.all()
    serializer_class=BorrowingSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class BorrowingUpadateView(
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericAPIView):

    queryset=BorrowingModel.objects.all()
    serializer_class=BorrowingSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
