from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    author = models.CharField(max_length=200, blank=True, default='')
    synopsis = models.CharField(max_length=300, blank=True, default='')
    category = models.CharField(max_length=200, blank=True, default='')
    publishing_date = models.DateTimeField()
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class BookCategory(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
