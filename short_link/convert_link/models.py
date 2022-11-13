from django.db import models


class ShortLink(models.Model):
    source_link = models.URLField(null=False)
    short_link = models.CharField(max_length=42, null=False, verbose_name='Коротке посилання')
    jumps = models.IntegerField(default=0, verbose_name='Кількість переходів')
    deleted = models.BooleanField(default=False, verbose_name='Видалено')
    last_jump_at = models.DateTimeField(null=True, verbose_name='Останній перехід')
    owner = models.CharField(max_length=15, verbose_name='ID/IP власника')

    class Meta:
        verbose_name = 'Коротке посилання'
        verbose_name_plural = 'Короткі посилання'
    # def __str__(self):
    #     return f'{self.short_link} >>> {self.source_link}  ({self.owner})'
