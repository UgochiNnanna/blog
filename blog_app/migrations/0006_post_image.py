# Generated by Django 4.0 on 2024-01-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_rename_reels_reel'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post_image/'),
        ),
    ]
