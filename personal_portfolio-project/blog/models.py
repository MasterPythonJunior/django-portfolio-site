from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField()

    def __str__(self):
        return self.title
