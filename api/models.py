from django.db import models
from django.utils.text import slugify

# Create your models here.
class Item(models.Model):
    name = models.CharField(unique=True, max_length=50)
    inventory = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name