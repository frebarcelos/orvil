# Generated by Django 5.0.4 on 2024-04-19 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='Title',
            new_name='title',
        ),
    ]
