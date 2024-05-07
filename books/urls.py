from django.urls import path
from .views import BooksAPIView
urlpatterns = [
    path('/', BooksAPIView.as_view()),
]
