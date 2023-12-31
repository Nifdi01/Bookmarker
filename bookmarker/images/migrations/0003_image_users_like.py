# Generated by Django 4.1.10 on 2023-08-23 11:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("images", "0002_alter_image_options_remove_image_users_like_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="users_like",
            field=models.ManyToManyField(
                blank=True, related_name="images_liked", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
