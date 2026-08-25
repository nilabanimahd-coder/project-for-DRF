from django.urls import path
from . import views

urlpatterns = [
    path("category/",views.CategoryListView.as_view(),name="category"),
    path("",views.BookListView.as_view(),name="books"),
    path("<int:pk>/",views.BookDetailView.as_view(),name="book")

]