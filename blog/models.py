from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now=True)
    # date_posted = models.DateTimeField(auto_now_add=True)
    # date_posted = models.DateTimeField(default=timezone.now)
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={'pk': self.pk})

    def get_short_content(self, max_length=75):
        if len(self.content) <= max_length:
            return self.content
        return f"{self.content[:max_length]} ..."
