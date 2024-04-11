from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_re_create_users_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.EmailField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
    ]
