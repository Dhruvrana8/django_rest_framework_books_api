from django.shortcuts import get_object_or_404
from rest_framework import status
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

    def post(self, request):
        data = request.data
        serializer = BooksSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def put(self, request):
        book_id = request.data.get('id')

        if not book_id:
            return Response({"error": "ID is required to update a book."}, status=status.HTTP_400_BAD_REQUEST)

        book = get_object_or_404(Books, id=book_id)

        serializer = BooksSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        book_id = request.data.get('id')

        if not book_id:
            return Response({"error": "ID is a required field to delete the book"}, status=status.HTTP_400_BAD_REQUEST)

        book = get_object_or_404(Books, id=book_id)
        book.delete()
        return Response({"message":"The Book had been deleted"})
