from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Books
from .serializers import BooksSerializer

class BooksAPIView(APIView):
    def get(self, request):
        data = Books.objects.all()
        serializer = BooksSerializer(data, many=True)
        if serializer.is_valid:
            return Response(serializer.data)
        else:
            return Response(serializer.errors())

    def post(self,request):
        data= request.data
        serializer = BooksSerializer(data= data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

