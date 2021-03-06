# Generated by Django 4.0.1 on 2022-06-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
