from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import BookSerializer,MangaSerializer
# Create your views here.
from .models import Book,Manga
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly

class BookListView(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    permission_classes=[IsOwnerOrReadOnly]

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    permission_classes=[IsOwnerOrReadOnly]



class MangaListView(ListCreateAPIView):
    queryset=Manga.objects.all()
    serializer_class= MangaSerializer
    permission_classes=[AllowAny]


class MangaDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Manga.objects.all()
    serializer_class= MangaSerializer
