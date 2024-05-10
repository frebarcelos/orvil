# Generated by Django 5.0.3 on 2024-03-27 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40)),
                ('nome_completo', models.CharField(max_length=60)),
                ('Equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.equipe')),
            ],
        ),
    ]