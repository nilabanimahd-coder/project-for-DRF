from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'borrowing'

router=DefaultRouter()
router.register("",views.BorrowingViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
