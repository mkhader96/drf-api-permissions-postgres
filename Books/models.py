from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    book_name = models.CharField(max_length=255, null=False, blank=True)
    book_purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    book_description = models.TextField()
    book_author = models.CharField(max_length=255, null=False, blank=True)
    book_genre = models.CharField(max_length=255, null=False, blank=True)
    book_rating = models.IntegerField()
 
    def __str__(self):
        return self.book_name

class Manga(models.Model):
    manga_name = models.CharField(max_length=255, null=False, blank=True)
    manga_purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    manga_description = models.TextField()
    manga_genre = models.CharField(max_length=255, null=False, blank=True)
    manga_rating = models.IntegerField()

    def __str__(self):
        return self.manga_name
