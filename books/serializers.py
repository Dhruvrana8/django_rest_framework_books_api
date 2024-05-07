from time import timezone

from rest_framework import serializers

from books.models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
       model = Books
       fields = ['id', 'name', 'author', 'create_at', 'modified_at']

    def create(self, validated_data):
        instance = Books._default_manager.create(**validated_data)
        return instance