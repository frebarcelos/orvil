from django.db import models

class Report(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    bookId = models.CharField(max_length=50)
    userId = models.CharField(max_length=50, unique=True)
    report = models.CharField(max_length=200)
    summary = models.IntegerField()

    def __str__(self):
        return self.report

    class Meta:
        db_table = 'polls_reports'