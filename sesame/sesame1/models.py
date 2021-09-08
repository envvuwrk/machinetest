from django.db import models


# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.name)
