# Generated by Django 2.2.2 on 2019-06-28 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_book_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category',
            new_name='categories',
        ),
    ]
