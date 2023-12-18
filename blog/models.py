from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = models.TextField( null=True)
    author = models.CharField(max_length=255, null=True)
    slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title