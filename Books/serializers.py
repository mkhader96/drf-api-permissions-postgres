from rest_framework import serializers

from .models import Book,Manga
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields='__all__'

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Manga
        fields='__all__'