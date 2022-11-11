from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name


class ShortLink(models.Model):
    source_link = models.URLField(null=False)
    short_link = models.CharField(max_length=42, null=False)
    jumps = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_jump_at = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=15)

    def __str__(self):
        return f'id: {self.pk}   {self.source_link}  -->  {self.short_link}'
