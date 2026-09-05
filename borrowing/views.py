
from .models import BorrowingModel
from .serializers import BorrowingSerializer
from rest_framework.viewsets import ModelViewSet
from .throttles import CustomerUserThrottle

class BorrowingViewSet(ModelViewSet):
    throttle_classes=[CustomerUserThrottle]
    queryset=BorrowingModel.objects.all()
    serializer_class=BorrowingSerializer
    
