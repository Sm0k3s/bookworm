from django.db import models

# Create your models here.

class BookCategory(models.Model):
    name = models.CharField(max_length=200, blank=True, default='', unique=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, blank=True, default='', unique=True)
    author = models.CharField(max_length=200, blank=True, default='')
    synopsis = models.CharField(max_length=300, blank=True, default='')
    category = models.ForeignKey(
        BookCategory,
        related_name='books',
        on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title
