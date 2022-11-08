from django.db import models

class User(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ShortLink(models.Model):
    source_link = models.CharField(max_length=1024, null=False)
    short_link = models.CharField(max_length=42, null=False)
    jumps = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
