# Generated by Django 5.1.4 on 2024-12-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctaloge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default='', upload_to='books/'),
            preserve_default=False,
        ),
    ]
