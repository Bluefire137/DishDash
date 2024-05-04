from django.db import models
from django.urls import reverse


class Dishes(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    type = models.CharField(max_length=50)
    time_to_cook = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    link = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'dish_slug': self.slug})
