from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
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
    serializer_class=BorrowingSerializer



