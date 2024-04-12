from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_create_books_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookId', models.CharField(max_length=50)),
                ('userId', models.EmailField(max_length=50)),
                ('report', models.CharField(max_length=200)),
                ('summary', models.IntegerField()),
            ],
        ),
    ]
