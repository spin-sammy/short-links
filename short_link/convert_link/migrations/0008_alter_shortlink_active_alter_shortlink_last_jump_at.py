# Generated by Django 4.1.2 on 2022-11-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert_link', '0007_alter_shortlink_options_remove_shortlink_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlink',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
        migrations.AlterField(
            model_name='shortlink',
            name='last_jump_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Останній перехід'),
        ),
    ]
