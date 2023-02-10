from django.db import models

# Create your models here.
class Film(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='Gallery')

    def __str__(self):
        return self.name