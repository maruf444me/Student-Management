from account.models import User
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        super().save(*args, **kwargs)