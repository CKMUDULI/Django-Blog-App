from PIL import Image
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(on_delete=models.CASCADE, to=User)
    bio = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    profession = models.CharField(null=True, blank=True, max_length=40)
    about_me = models.TextField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.user.username} Profile"
