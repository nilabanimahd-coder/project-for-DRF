from django.urls import path
from . import views

app_name = 'borrowing'

urlpatterns = [
    path("createlist/",views.BorrowingView.as_view()),
    path("<int:pk>/",views.BorrowingUpadateView.as_view()),
]