from rest_framework.generics import ListCreateAPIView

from .models import Books
from .serializers import BooksSerializer

class BooksAPIView(ListCreateAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
