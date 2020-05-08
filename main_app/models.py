from django.db import models
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class Item(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('home')

    