from django.urls import path
from .views import BookListView,BookDetailView,MangaListView,MangaDetailView


urlpatterns = [
   path('book/', BookListView.as_view(), name='Book_list'),
   path('book/<int:pk>', BookDetailView.as_view(),name='Book_detail'),
   path('manga/', MangaListView.as_view(), name='Manga_list'),
   path('manga/<int:pk>', MangaDetailView.as_view(),name='Manga_detail')
]