from django.db import models

# Create your models here.
class task(models.Model):
    name=models.CharField(max_length=200)
    pr=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name