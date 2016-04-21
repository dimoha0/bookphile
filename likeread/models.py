from django.db import models
from django.utils import timezone

class AboutBook(models.Model):
    book_title=models.CharField(max_length=200)
    book_author=models.CharField(max_length=200)
    book_info=models.TextField(max_length=1000)
    book_year=models.IntegerField()


    book_comments_count=models.IntegerField(default=0)
    book_views_count=models.IntegerField(default=0)

    def __str__(self):
        return self.book_title
class Genre(models.Model):
    book_genre=models.CharField(max_length=100)
    book=models.ManyToManyField(AboutBook)
    def __str__(self):
        return self.book_genre



# Create your models here.
