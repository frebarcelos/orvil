# Generated by Django 5.0.4 on 2024-04-20 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0004_livro_authors'),
    ]

    operations = [
                migrations.CreateModel(
            name='Resenha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('texto', models.TextField()),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=5)),
                ('resenha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.resenha')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.usuario')),
            ],
        ),
    ]
