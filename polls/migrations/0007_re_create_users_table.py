from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('senha', models.CharField(max_length=128)),
            ],
        ),
    ]
