
from .models import BorrowingModel
from .serializers import BorrowingSerializer,MyPagination
from rest_framework.viewsets import ModelViewSet
from .throttles import CustomerUserThrottle

class BorrowingViewSet(ModelViewSet):
    throttle_classes=[CustomerUserThrottle]
    pagination_class=MyPagination
    queryset=BorrowingModel.objects.all()
    serializer_class=BorrowingSerializer
    
