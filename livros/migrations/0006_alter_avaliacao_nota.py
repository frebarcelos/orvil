# Generated by Django 5.0.4 on 2024-04-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0005_usuario_resenha_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
